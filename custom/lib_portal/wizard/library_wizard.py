from odoo import api, models, fields, _


class LibraryWizard(models.TransientModel):
    _name = "stock.scrap.wizard"

    text = fields.Text()
    scrap_picking_return = fields.Boolean(default=False)

    def action_scrap_warning(self):
        if(self.scrap_picking_return):
            move_id = self.env['stock.move'].search(
                [('picking_id', 'in', self.env.context.get('active_ids'))])
            view = self.env.ref('stock.stock_scrap_form_view2')
            return {
                'name': _('Scrap'),
                'view_mode': 'form',
                'res_model': 'stock.scrap',
                'view_id': view.id,
                'views': [(view.id, 'form')],
                'type': 'ir.actions.act_window',
                'context': {'default_picking_id': self.id, 
                            'product_id': move_id.product_id.id, 
                            'default_company_id': move_id.company_id.id},
                'target': 'new',
            }
        else:
            scrap_obj = self.env['stock.scrap'].browse(
                self.env.context.get('active_ids'))
            return scrap_obj.action_validate()
