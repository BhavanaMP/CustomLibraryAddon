from odoo import api, fields, models


class ProductTemplate(models.Model):
    _inherit = 'product.template'
    
    author_id = fields.Many2one('res.partner', 
                              string='Select Author', 
                              domain=[('is_company', '=', False)])
    author_name = fields.Char(related='author_id.name', store=True)
    book_description = fields.Text(string='Book Description')
    categ_id = fields.Many2one('product.category', string='Book Genre')
    publication_date = fields.Date(string='Publication Date')
    book_language = fields.Many2one('res.lang', string='Book Language')
    default_code = fields.Char(string='Shelf Location', required=True)
    barcode = fields.Char(string='Book ISBN', required=True)
    reserve_state = fields.Selection([('available', 'Available to Lend'),
                                     ('not_available', 'Not available')], 
                                    string='Book Status', default='available') 
    #create a compute field here to check the availabiliity status
    
    