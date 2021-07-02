from odoo import api, fields, models, _
from odoo.exceptions import UserError,Warning

class StockScrap(models.Model):
    _inherit = 'stock.scrap'
    
    def do_scrap(self):
        for scrap in self:
            raise Warning("Are you sure to scrap the %s?"%scrap.product_id)
        obj = super (StockScrap, self) .do_scrap () 
        return obj
    
    @api.model
    def create(self, vals_list):
        for scrap in self:
            raise Warning ("Are you sure to scrap the %s?"%scrap.product_id) 
        create_ref = super(StockScrap, self).create(vals_list)
        return create_ref