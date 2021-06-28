from odoo import models, fields


class LibraryWizard(models.TransientModel):
    _name = 'library.wizard'
    _description = 'Wizard for Library Module'
    
    book_id = fields.Many2one('product.template', string='Book Name', 
                              required=True)
    shelf_id = fields.Char(related='book_id.default_code')
    
    def action_library_wizard_show(self):
        #function to update the shelf ID
        print(self.shelf_id)
        return True