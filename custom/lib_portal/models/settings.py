from odoo import models, fields, api,  _


class LibrarySettings(models.TransientModel):
    _inherit = 'res.config.settings'

    email = fields.Char(string='Common Mail Address',
                        default='magdeburgcitylibrary@example.com')
    lend_duration = fields.Char(string='Lend Period', default=30)
    lend_limit = fields.Char(string='Lend Limit', default=4)

    def set_values(self):
        res = super(LibrarySettings, self).set_values()
        self.env['ir.config_parameter'].set_param(
            'lib_portal.email', self.email)
        self.env['ir.config_parameter'].set_param(
            'lib_portal.lend_duration', self.lend_duration)
        self.env['ir.config_parameter'].set_param(
            'lib_portal.lend_limit', self.lend_limit)
        return res

    @api.model
    def get_values(self):
        res = super(LibrarySettings, self).get_values()
        email = self.env['ir.config_parameter'].sudo(
        ).get_param('lib_portal.email')
        lend_duration = self.env['ir.config_parameter'].sudo(
        ).get_param('lib_portal.lend_duration')
        lend_limit = self.env['ir.config_parameter'].sudo(
        ).get_param('lib_portal.lend_limit')
        res.update(
            email=email,
            lend_duration=lend_duration,
            lend_limit=lend_limit,
        )
        return res
