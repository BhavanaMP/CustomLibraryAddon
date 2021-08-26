from odoo import models, fields


class StockReturnPicking(models.TransientModel):
    _inherit = "stock.return.picking"

    def _create_returns(self):

        res = super(StockReturnPicking, self)._create_returns()
        picking = self.env['stock.picking'].browse(res)
        issue_id = self.env['issue.book'].search([
            ('id', '=', picking.library_id.id)])
        partner_id = self.env['res.partner'].browse(issue_id.partner_id.id)
        if fields.Date.context_today(self) <= issue_id.due_date:
            partner_id.reward_pts += 5
        else:
            partner_id.reward_pts -= 10
        issue_id.write({'state': 'return'})
        issue_id.send_return_email()
        return res
