from odoo import api, fields, models

class ProductTemplate(models.Model):
    _inherit = 'product.template'
    
    is_book = fields.Boolean(string='Book?', default=False)
    author_id = fields.Many2one('res.partner', 
                              string='Select Author', 
                              domain=[('is_company', '=', False)])
    author_name = fields.Char(related='author_id.name', store=True)
    book_description = fields.Text(string='Book Description')
    categ_id = fields.Many2one('product.category', string='Book Genre')
    publication_date = fields.Date(string='Publication Date')
    book_language = fields.Many2one('res.lang', string='Book Language')
    default_code = fields.Char(string='Shelf Location')
    barcode = fields.Char(string='Book ISBN')

    
    