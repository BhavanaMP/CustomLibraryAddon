
from odoo import models, fields


class Picking(models.Model):
    _inherit = 'stock.picking'

    library_id = fields.Many2one('issue.book')

    def button_validate(self):
        res = super(Picking, self).button_validate()
        if self.state == 'done':
            active_id = self._context.get('active_ids')
            issue_id = self.env['issue.book'].search([('id', 'in', active_id)])
            issue_id.state = 'pick'
        return res
