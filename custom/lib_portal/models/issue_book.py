from odoo.exceptions import ValidationError
from odoo import api, exceptions, fields, models
from datetime import datetime, timedelta
from dateutil.relativedelta import relativedelta

class IssueBook(models.Model):
    _name = "issue.book"
    _inherit = ['mail.thread', 'mail.activity.mixin']
    _description = "Library Book Lending Mangement"
    _rec_name = 'book_name'
    
    def _check_due_date(self):
        return fields.Date.context_today(self) + relativedelta(days=30)
    
    partner_id = fields.Many2one('res.partner', string = "Customer")
    customer_name = fields.Char(related='partner_id.name', 
                                string="Customer", store=True)
    book_id = fields.Many2one('product.template', string = "Book")
    book_name = fields.Char(related='book_id.name', string = "Book", 
                            store=True)
    author_name = fields.Char(related='book_id.author_name', 
                              string = "Author", store=True)
    from_date = fields.Date(string='Start Date',
                           default=fields.Date.context_today)
    due_date = fields.Date(string="Return Date",
                           default=_check_due_date)
    employee_id = fields.Many2one('hr.employee', string='Employee')
    state = fields.Selection(selection=[('plan', 'Planned'),
                                         ('pick', 'Picked'),
                                         ('late', 'Late'),
                                         ('return', 'Returned'),], 
                              string='Status',default='plan',
                              help="The current state of your book:")
    
    @api.constrains('due_date')
    def _check_due_date(self):
        for record in self:
            if record.due_date <= record.from_date:
                raise ValidationError("Due date cannot be before the start date")
         
    def getReservationState(self):
        state='plan' 
        #setting it temporarily.use the reservationState parameter from product
        if state == "plan":
            return True
        else:
            return False
    def sendMailConfirmation(self):
        #trigger mail using self.customer_email
        return True  

    def renewInfo(self):
        #check the res.partner for renew info
        return
    
    def bookIssueRecord(self):
        if self.getReservationState:
            #save the record in the table issue_book
            self.sendMailConfirmation()
            #add params like book id,start data,end date
            return
             
           
    