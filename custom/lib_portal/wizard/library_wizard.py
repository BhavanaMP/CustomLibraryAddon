from odoo import api, models, fields, _


class LibraryWizard(models.TransientModel):
    _name="stock.scrap.wizard"
    
    def action_scrap_warning(self):
        scrap_obj = self.env['stock.scrap'].browse(self.env.context.get('active_ids'))
        return scrap_obj.action_validate()
       