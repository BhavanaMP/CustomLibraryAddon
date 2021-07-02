from odoo import models, fields

class ResPartner(models.Model):
    _inherit = 'res.partner'
    
    def _isMember(self):
        """
        this Function is used to check the active customer membership details
        """
        return True

    date_of_birth = fields.Date(string='Date of Birth', 
                                default=fields.Date.context_today)
    date_of_death = fields.Date(string='Date of Death') 
    languages_known = fields.Many2many('res.lang', 'partner_lang_rel', 
                                       string='Known Languages')
	is_author = fields.Boolean(string='Is a Author', default=False, store=True)
    is_publisher = fields.Boolean(string='Is a Publisher', default=False, 
                                  store=True)
    is_member = fields.Char(compute='_isMember', string='Membership Status')
    book_ids = fields.One2many('product.template', 'author_id')
    publisher_ids = fields.One2many('product.template', 'publisher_id')  

