from odoo import models, fields

class ResPartner(models.Model):
    _inherit = 'res.partner'
    
    def _isMember(self):
        """
        this Function is used to check the active customer membership details
        """
        return True

    date_of_birth = fields.Date(string='Date of Birth', 
                                default=fields.Date.context_today, 
                                required=True)
    date_of_death = fields.Date(string='Date of Death') 
    languages_known = fields.Many2many('res.lang',string='Known Languages')
    # interest_ids = fields.Many2many('res.partner.category', string='Interests')
    is_member = fields.Char(compute='_isMember', string='Membership Status')
   
  
   

