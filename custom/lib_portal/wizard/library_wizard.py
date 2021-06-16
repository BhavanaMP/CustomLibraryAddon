from odoo import models, fields


class LibraryWizard(models.TransientModel):
    _name = 'library.wizard'
    _description = 'Wizard for Library Module'
    
    book_id = fields.Many2one('product.template',string='Book Name')
    # shelf_id = fields.Integer(book_id.shelf_id, readonly=True)
    
    def action_library_wizard_update(self):
        #function to update the shelf ID
        print(self.book_id.name)