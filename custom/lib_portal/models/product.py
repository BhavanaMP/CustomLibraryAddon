from odoo import api, models

class ProductProduct(models.Model):
    _name = "product.product"
    _description = "Product"
    # product model is inheritng the product.template which shows all the available lists
    _inherit = 'product.product'


