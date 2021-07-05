{
    'name' : 'Library Portal',
    'version' : '14.0.1.1.0',
    'author' : 'bloopark', 
    'summary': 'Library Management System',
    'description': """
    Module to digitalise and manage the library operations
    """,
    'category' : 'Library',
    'depends' : ['product', 'contacts', 'hr', 'mail', 'stock'],
    'data' : [ 
       
        'data/res.partner.csv',
        'data/lib_data.xml',
        'demo/lib_demo.xml',
        'security/ir.model.access.csv',
        'wizard/library_wizard_view.xml',
        'views/res_partner.xml',
        'views/product_template.xml',
        'views/lib_issue_book.xml',
        'report/res_partner_report.xml'
        
    ],
    'demo' : [
        
         'demo/library_demo.xml',
    ],
    'sequence' : 1,
    'installable': True,
    'application': True,
    'auto_install': False,

}
