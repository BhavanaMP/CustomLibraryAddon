from odoo import api, fields, models, _


class StockScrap(models.Model):
    _inherit = 'stock.move'

    library_id = fields.Many2one('issue.book')
