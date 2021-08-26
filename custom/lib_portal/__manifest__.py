{
    'name': 'Library Portal',
    'version': '14.0.1.1.0',
    'author': 'bloopark',
    'summary': 'Library Management System',
    'description': """
      Module to digitalise and manage the library operations
    """,
    'category': 'Library',
    'depends': ['product', 'contacts', 'hr', 'mail', 'stock'],
    'data': [
        'security/security.xml',
        'data/res.partner.csv',
        'data/library_cron.xml',
        'data/lib_data.xml',
        'report/bookings_detail_report.xml',
        'data/mail_template.xml',
        'security/ir.model.access.csv',
        'wizard/library_wizard_view.xml',
        'wizard/bookings_report_wizard.xml',
        'views/res_partner.xml',
        'views/product_template.xml',
        'views/lib_issue_book.xml',
        'views/stock_scrap_views.xml',
        'views/stock_picking_views.xml',
        'report/res_partner_report.xml',

    ],
    'demo' : [
        
         'demo/lib_demo.xml',
    ],
    'sequence': 1,
    'installable': True,
    'application': True,
    'auto_install': False,

}
