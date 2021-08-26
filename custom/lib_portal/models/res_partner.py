from odoo import api, models, fields


class ResPartner(models.Model):
    _inherit = 'res.partner'

    date_of_birth = fields.Date(string='Date of Birth',
                                default=fields.Date.context_today)
    date_of_death = fields.Date(string='Date of Death')
    languages_known = fields.Many2many('res.lang', 'partner_lang_rel',
                                       string='Known Languages')
    is_author = fields.Boolean(string='Is a Author',
                               default=False, store=True)
    is_publisher = fields.Boolean(string='Is a Publisher', default=False,
                                  store=True)
    book_ids = fields.One2many('product.template', 'author_id')
    booking_ids = fields.One2many('issue.book', 'partner_id')
    publisher_ids = fields.One2many('product.template', 'publisher_id')
    reward_pts = fields.Integer(string='Reward Points', default=100)
