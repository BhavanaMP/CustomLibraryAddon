from odoo import api, fields, models


class ProductTemplate(models.Model):
    _name = "product.template"
    _inherit = 'product.template'
    
    authorName = fields.Text('Author')
    bookDescription = fields.Text('Book Description')
    publcationDate = fields.Date('Publication Date')
    bookLanguage = fields.Text(string='Book Language')
    shelfID = fields.Integer('Shelf Location')
    reservationState = fields.Selection([
        ('available', 'Available to Lend'),
        ('not_available', 'Not available')
        ], string='Book Status', default='available') #create a compute field here to check the availabiliity status

    
    