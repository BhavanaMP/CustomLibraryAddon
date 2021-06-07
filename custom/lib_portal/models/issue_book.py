
from odoo import fields, models
from datetime import datetime, timedelta

class IssueBook(models.Model):
    _name = "issue.book"
    _description = "Library Book Lending Mangement"


    fromDate = fields.Date('Start Date',default=datetime.today())
    toDate = fields.Date(string="Due Date",default=datetime.today()+timedelta(days=30))

    partner_id = fields.Many2one(
        'res.partner', string='Customer', readonly=True,
        required=True, change_default=True, index=True, tracking=1)
    customer_name = fields.Char(related='partner_id.name')
    customer_email = fields.Char('Email', related='partner_id.email')
    book_id = fields.Many2one('product.template')
    authorName = fields.Text('Author',related='book_id.authorName')
    book_name = fields.Char(related='book_id.name')
    emp_id = fields.Many2one('hr.employee', string='Employee')
    
    def getReservationState(self):
        state='Available' #setting it temporarily.use the reservationState parameter from product
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
            self.sendMailConfirmation()#add params like book id,start data,end date
            return
        
           
    