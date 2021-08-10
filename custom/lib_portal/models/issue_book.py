from odoo.exceptions import ValidationError
from odoo import api, exceptions, fields, models
from datetime import datetime, timedelta
from dateutil.relativedelta import relativedelta

class IssueBook(models.Model):
    _name = "issue.book"
    _inherit = ['mail.thread', 'mail.activity.mixin']
    _description = "Library Book Lending Mangement"
    _rec_name = 'book_name'
    
    def _check_due_date(self):
        return fields.Date.context_today(self) + relativedelta(days=30)
    
    partner_id = fields.Many2one('res.partner', string = "Customer")
    customer_name = fields.Char(related='partner_id.name', 
                                string="Customer", store=True)
    book_id = fields.Many2one('product.template', string = "Book")
    book_name = fields.Char(related='book_id.name', string = "Book", 
                            store=True)
    is_author = fields.Boolean(related='partner_id.is_author')
    author_name = fields.Char(related='book_id.author_name', 
                              string = "Author", store=True)
    from_date = fields.Date(string='Start Date',
                           default=fields.Date.context_today)
    due_date = fields.Date(string="Return Date",
                           default=_check_due_date)
    employee_id = fields.Many2one('hr.employee', string='Employee')
    state = fields.Selection([('draft', 'Draft'),
                                        ('plan', 'Planned'),
                                         ('pick', 'Picked'),
                                         ('return', 'Returned'),
                                         ('late', 'Late')], 
                              string='Status',default='draft',
                              help="The current state of the booking:")
    
    def stock(self):
       
		
        #method for calling the stock picking
    
    @api.model
    def create(self, vals_list):
        bookissue_obj = super(IssueBook, self).create(vals_list)
        product = self.env['product.product']
        inventory_stock = self.env['stock.quant']
        product_id = product.search([
            ('product_tmpl_id', '=', bookissue_obj.book_id.id)]).id
        qty_available = inventory_stock.search([
            ('product_id', '=', product_id),('quantity', '>=', 0)]).quantity
        if qty_available <= 0.0 :
            raise ValidationError('Books are not available in stock to issue!!')
        return super().create(vals_list)
    
    @api.model
    def _compute_booking_state(self):
        print(type(dict(self._fields['state'].selection).get(self.state)))
        return dict(self._fields['state'].selection).get(self.state)
    
    @api.constrains('from_date', 'due_date')
    def _check_due_date(self):
        for record in self:
            if record.from_date and record.due_date and record.due_date <= record.from_date:
                raise ValidationError("Due date can't be earlier than the start date")
    
    @api.onchange('from_date')
    def on_change_from_date(self):
        if self.from_date and self.due_date and self.due_date < self.from_date:
            self.due_date = self.from_date

    @api.onchange('due_date')
    def _onchange_end_date(self):
        if self.due_date and self.due_date < self.from_date:
            self.from_date = self.due_date
            
    def action_set_status_planned(self):
        self.state='plan'
    
    def action_set_status_picked(self):
        self.state='pick'
    
    def action_set_status_returned(self):
        self.state='return'
        
    def action_set_status_late(self):
        self.state='late'
             
           
    