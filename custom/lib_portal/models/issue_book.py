from odoo.exceptions import UserError, ValidationError
from odoo import api, exceptions, fields, models, _
from datetime import datetime, timedelta
from dateutil.relativedelta import relativedelta


class IssueBook(models.Model):
    _name = "issue.book"
    _inherit = ['mail.thread', 'mail.activity.mixin']
    _description = "Library Book Request"
    _rec_name = 'name'

    def _check_due_date(self):
        return fields.Date.context_today(self) + relativedelta(days=30)

    name = fields.Char(string='Request Number', required=True, readonly=True,
                       default='New', copy=False)
    partner_id = fields.Many2one('res.partner', string="Requested By",
                                 required=True)
    customer_name = fields.Char(related='partner_id.name',
                                string="Customer", store=True)
    reward_pts = fields.Integer(related='partner_id.reward_pts',
                                string="Reward Points", store=True)
    book_id = fields.Many2one('product.template', string="Book", required=True,
                              domain=[('is_book', '=', True),
                                      ])
    book_name = fields.Char(related='book_id.name', string="Book",
                            store=True)
    product = fields.Many2one('product.product')
    image_1920 = fields.Binary(related='book_id.image_1920')
    is_author = fields.Boolean(related='partner_id.is_author')
    author_name = fields.Char(related='book_id.author_name',
                              string="Author", store=True)
    from_date = fields.Date(string="Request Date",
                            default=fields.Date.context_today, required=True)
    due_date = fields.Date(string="Return Date",
                           default=_check_due_date)
    employee_id = fields.Many2one('hr.employee', 
                                  string='Authorised By', required=True)
    move_id = fields.Many2one('stock.move')
    picking_id = fields.Many2one('stock.picking')
    state = fields.Selection([('draft', 'Draft'),
                              ('plan', 'Planned'),
                              ('pick', 'Picked'),
                              ('return', 'Returned'),
                              ('late', 'Late')],
                             string='Status', default='draft', copy=False,
                             track_visibility='onchange', readonly=True,
                             help="The current state of the booking:")
    notes = fields.Text(
        string='Internal Notes', translate=True)

    @api.model
    def _get_default_picking_type(self):
        picking_type_id = self.env['stock.picking.type'].search([
            ('code', '=', 'outgoing'), ], limit=1).id
        return picking_type_id

    @api.model
    def set_late_state(self):
        cron_obj = self.env['issue.book'].search([('state', '=', 'pick'), ])
        for record in cron_obj:
            if record.due_date < datetime.now().date():
                record.state = 'late'
                context = {
                    'subject': 'Overdue Notification of book',
                    'book_state': 'overdue',
                    'message': 'Please return the book as soon as possible.'
                }
                
                """Triggering an email to customer"""
                
                template_id = self.env.ref(
                    'lib_portal.email_template_status_late').id
                template = self.env['mail.template'].browse(template_id)
                template.with_context(context).send_mail(
                    record.id, force_send=True)

    @api.model
    def send_return_email(self):
        context = {
            'subject': 'Return Confirmation of book',
            'book_state': 'returned',
            'message': 'Thanks for returning the book'
        }
        template_id = self.env.ref('lib_portal.email_template_status_late').id
        template = self.env['mail.template'].browse(template_id)
        template.with_context(context).send_mail(self.id, force_send=True)

    def _get_product(self):
        product = self.env['product.product']
        product_id = product.search([
            ('product_tmpl_id', '=', self.book_id.id)]).id
        return product_id

    def _get_product_location(self):
        product = self.env['product.product']
        inventory_stock = self.env['stock.quant']
        product_id = product.search([
            ('product_tmpl_id', '=', self.book_id.id)], limit=1).id
        loc_id = inventory_stock.search([
            ('product_id', '=', product_id), ('quantity', '>', 0)],
            limit=1).location_id.id
        return loc_id

    def _prepare_move_values(self):
        self.ensure_one()
        return {
            'name': self.name,
            'origin': self.name,
            'product_id': self._get_product(),
            'product_uom': self.book_id.uom_id.id,
            'state': 'draft',
            'product_uom_qty': 1,
            'location_id': self._get_product_location(),
            'location_dest_id': 5,
            'picking_id': self.picking_id.id
        }

    def action_view_picking(self):
        if not self._get_product_location():
            raise ValidationError("Books are not available in stock to plan")
        pick = {
            'picking_type_id': self._get_default_picking_type(),
            'partner_id': self.partner_id.id,
            'origin': self.name,
            'location_id': self._get_product_location(),
            'location_dest_id': 5,
            'library_id': self.id,
        }
        picking = self.env['stock.picking'].create(pick)
        self.picking_id = picking.id
        action = self.env["ir.actions.actions"]._for_xml_id(
            "stock.action_picking_tree_ready")
        action['context'] = {'default_partner_id': self.partner_id.id,
                             'default_origin': self.name,
                             'default_picking_type_id': self._get_default_picking_type()}
        pick_ids = sum([self.picking_id.id])
        
        """choose the view_mode accordingly"""
        
        if pick_ids:
            res = self.env.ref('stock.view_picking_form', False)
            form_view = [(res and res.id or False, 'form')]
            if 'views' in action:
                action['views'] = form_view + \
                    [(state, view)
                     for state, view in action['views'] if view != 'form']
            else:
                action['views'] = form_view
            action['res_id'] = pick_ids or False
        move = self.env['stock.move'].create(self._prepare_move_values())
        move_ids = move._action_confirm()
        move_ids._action_assign()
        self.action_set_status_planned()
        move.write({'library_id': self.id,'picking_id': move.picking_id})
        self.write({'move_id': move.id})
        return action

    @api.model
    def create(self, vals_list):
        partner = self.env['res.partner'].browse(vals_list['partner_id'])
        if partner.reward_pts < 50:
            raise UserError("Books cannot be issued to the customer because there are not enough reward points")
        if vals_list.get('name', 'New') == 'New':
            vals_list['name'] = self.env['ir.sequence'].next_by_code(
                'lib.book.request') or 'New'
        return super(IssueBook, self).create(vals_list)

    @api.onchange('book_id')
    def on_change_book_id(self):
        if self.book_id and not self.book_id.is_book:
            raise ValidationError("The selected product is not a book.Please make sure to select the book to create the booking order")

    @api.constrains('from_date', 'due_date')
    def _check_due_date(self):
        for record in self:
            if record.from_date and record.due_date and record.from_date < fields.Date.context_today(self):
                raise ValidationError("Start date should not be earlier than current date")
            if record.from_date and record.due_date and record.due_date < record.from_date:
                raise ValidationError(
                    "Due date can't be earlier than the start date")

    @api.onchange('from_date')
    def on_change_from_date(self):
        if self.from_date and self.due_date and self.due_date < self.from_date:
            self.due_date = self.from_date

    @api.onchange('due_date')
    def _onchange_due_date(self):
        if self.due_date and self.due_date < self.from_date:
            if self.due_date >= fields.Date.context_today(self):
                self.from_date = self.due_date
            else:
                self.from_date = fields.Date.context_today(self)
                self.due_date = fields.Date.context_today(self)

    def action_set_status_planned(self):
        self.state = 'plan'

    def action_picked_inventory(self):
        return {
            'name': _('Picked'),
            'view_mode': 'form',
            'res_model': 'stock.picking',
            'res_id': self.picking_id.id,
            'domain': [('id', '=', self.picking_id.id)],
            'views': [(self.env.ref('stock.view_picking_form').id, 'form')],
            'type': 'ir.actions.act_window',
        }

    def action_set_status_picked(self, state):
        if state == 'done':
            self.state = 'pick'

    def action_set_status_returned(self):
        return {
            'name': _('Return'),
            'view_mode': 'form',
            'res_model': 'stock.picking',
            'res_id': self.picking_id.id,
            'domain': [('id', '=', self.picking_id.id)],
            'views': [(self.env.ref('stock.view_picking_form').id, 'form')],
            'type': 'ir.actions.act_window',
        }
