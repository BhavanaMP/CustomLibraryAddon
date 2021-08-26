from odoo import api, models, fields, _


class BookingsReportWizard(models.TransientModel):
    _name = "bookings.report.wiz"

    from_date = fields.Date(string='Start Date')
    to_date = fields.Date(string='To Date')
    partner_id = fields.Many2one('issue.book')
    customer_ids = fields.One2many('bookings.report.wiz', 'partner_id')
