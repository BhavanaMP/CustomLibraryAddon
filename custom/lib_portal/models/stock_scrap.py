from odoo import api, fields, models, _
from odoo.exceptions import UserError,Warning

class StockScrap(models.Model):
    _inherit = 'stock.scrap'