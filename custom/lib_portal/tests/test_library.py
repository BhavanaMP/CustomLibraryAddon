# coding: utf-8
from datetime import datetime
from odoo.fields import Date
from dateutil.relativedelta import relativedelta
from odoo.tests import HttpCase, common, tagged


class TestModelLibrary(common.TransactionCase):

    def test_bookings(self):
        test_partner = self.env['res.partner'].create({
            'name': 'Test Customer'
        })
        test_product = self.env['product.template'].create({
            'name': 'Test Product',
            'type': 'product',
            'categ_id': '1'
        })
        test_employee = self.env['hr.employee'].create({
            'name': 'Test Employee'
        })
        test_booking = self.env['issue.book'].create({
            'name': "IB000111",
            'partner_id': test_partner.id,
            'book_id': test_product.id,
            'from_date': (datetime.now().date() + relativedelta(days=1)),
            'due_date': (datetime.now().date() + relativedelta(days=30)),
            'employee_id': test_employee.id
        })
        self.assertEqual(test_booking.name, 'IB000111')
        print("Name is indeed IB000111")
        self.assertEqual(test_booking.partner_id.id, test_partner.id)
        print("Partners are retrieving properly and test is success")
        self.assertEqual(test_booking.book_id.id, test_product.id)
        print("Products are retrieving properly and test is success")
