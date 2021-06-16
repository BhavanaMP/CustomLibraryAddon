from odoo import fields, models
from datetime import datetime, timedelta
from dateutil.relativedelta import relativedelta

class IssueBook(models.Model):
    _name = "issue.book"
    _inherit = ['mail.thread', 'mail.activity.mixin']
    _description = "Library Book Lending Mangement"

    partner_id = fields.Many2one('res.partner', string = "Customer Name")
    customer_name = fields.Char(related='partner_id.name', 
                                string="Customer Name", store=True)
    book_id = fields.Many2one('product.template', string = "Select Book")
    book_name = fields.Char(related='book_id.name', string = "Book Name", 
                            store=True)
    author_name = fields.Char(related='book_id.author_name', 
                              string = "Author of the Book", store=True)
    from_date = fields.Date(string='Start Date',
                           default=fields.Date.context_today)
    due_date = fields.Date(string="Due Date",
                           default=fields.Date.context_today)
                         #.add(fields.Date.context_today,30))
                        #  + relativedelta(days=30))
    emp_id = fields.Many2one('hr.employee', string='Employee Issued')
    state = fields.Selection(string='Status', 
                             selection=[('available', 'Available'),
                                        ('notavailable', 'Not Available'),
                                        ('renew', 'Renewed')], 
                             default='available',
                             help="The current state of your book:")
    
    def getReservationState(self):
        state='Available' 
        #setting it temporarily.use the reservationState parameter from product
        if state == "Available":
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
             
           
    