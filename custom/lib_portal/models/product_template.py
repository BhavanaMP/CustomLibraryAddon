from odoo import api, fields, models


class ProductTemplate(models.Model):
    _name = "product.template"
    _inherit = 'product.template'

    publisher = fields.Text(string='Book Publisher')
    barcode = fields.Char(string='Book ISBN')
    default_code = fields.Char(string='Shelf ID')
    type = fields.Selection([
        ('consu', 'Consumable'),
        ('service', 'Service')], string='Book Type', default='consu', required=True,
        help='A storable product is a product for which you manage stock. The Inventory app has to be installed.\n'
             'A consumable product is a product for which stock is not managed.\n'
             'A service is a non-material product you provide.')
    
    categ_id = fields.Many2one(string='Book Category')
    