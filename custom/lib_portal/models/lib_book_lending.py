
from odoo import fields, models


class LibBookLending(models.Model):
    _name = "lib.book.lending"
    _description = "Library Book Lending Mangement"
    
   # name = fields.Char('Plan Name', required=True, translate=True)
    # number_of_months = fields.Integer('# Months', required=True)
    # active = fields.Boolean('Active', default=True)
    # sequence = fields.Integer('Sequence', default=10)