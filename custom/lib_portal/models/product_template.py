from odoo import api, fields, models


class ProductTemplate(models.Model):
    _inherit = 'product.template'

    is_book = fields.Boolean(string='Is a Book', default=False, store=True)
    author_id = fields.Many2one('res.partner',
                                string='Author',
                                domain=['&', ('is_company', '=', False),
                                        ('is_author', '=', True)])
    author_name = fields.Char(related='author_id.name', store=True)
    description = fields.Text(string='Book Description')
    categ_id = fields.Many2one('product.category', string='Book Genre')
    publication_date = fields.Date(string='Publication Date')
    book_language = fields.Many2one('res.lang', string='Book Language')
    barcode = fields.Char(string='Book ISBN')
    publisher_id = fields.Many2one('res.partner',
                                   string='Publisher',
                                   domain=['&', ('is_company', '=', True),
                                           ('is_publisher', '=', True)])
    issue_id = fields.Many2one('issue.book', string='Issue Reference',
                               )
    partner_id = fields.Many2one('res.partner',
                                 domain=[('is_company', '=', False)])
    quantity_id = fields.Many2one('stock.quant')
    qty_available = fields.Float(related='quantity_id.available_quantity',
                                 store=True)
    booking_ids = fields.One2many('issue.book', 'book_id')

    @api.onchange('is_book')
    def is_book_onchange(self):
        if self.is_book == True:
            self.type = 'product'

    def action_stock_scrap(self):
        action = self.env.ref('stock.action_stock_scrap').read()[0]
        action['domain'] = [('product_id', '=', self.product_variant_id.id)]
        action['context'] = {'default_product_id': self.product_variant_id.id,
                             'search_default_product_id': self.product_variant_id.id}
        return action
