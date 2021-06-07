from odoo import models, fields


class ResPartner(models.Model):
    _name = "res.partner"
    _inherit = 'res.partner'
    
    def _isMember(self):
        """
        this Function uses to get the ratification amount in words.
        """
        return True

    dob = fields.Date(string='Date of Birth')
    #dod = fields.Date('Date of Death') 
    languages_known = fields.Many2many(string='Known Languages')
    #interests = fields.Many2many(string='Interests')
     # <field name="bookLanguage" widget="many2many_tags" options="{'color_field': 'color', 'no_create_edit': True}" placeholder="Languages..."/> in xml
    isMember = fields.Char(compute='_isMember', string='Membership Status')
   
  
   

