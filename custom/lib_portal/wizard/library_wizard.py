from odoo import api, models, fields


class LibraryWizard(models.TransientModel):
    _name="lib.wizard"
    _inherit = 'stock.scrap'
    
    book_id = fields.Many2one('product.template', string='Book Name', 
                              required=True)
    shelf_id = fields.Char(related='book_id.default_code')
    text = fields.Text("Are you sure to scrap the selected Book?")
    
    def action_scrap_warning_show(self):
        self.do_scrap()
        return True
    
    def do_scrap(self):
        print("Hey")
        return super(LibraryWizard, self) .do_scrap () 
    
    @api.model
    def create(self, vals_list):
         for scrap in self:
             raise Warning ("Are you sure to scrap the %s?"%scrap.product_id) 
         create_ref = super(StockScrap, self).create(vals_list)
         return create_ref