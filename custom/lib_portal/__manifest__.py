{
    'name' : 'Library Portal',
    'version' : '1.1',
    'author' : 'bloopark', 
    'summary': 'Library Management System',
    'description': """
    Module to digitalise and manage the library operations
    """,
    'category' : 'Library',
    'depends' : ['product', 'contacts', 'hr', 'mail'],
    'data' : [ 
        'security/ir.model.access.csv',
        'wizard/library_wizard_view.xml',
        'views/res_partner.xml',
        'views/product_template.xml',
        'views/libraryManagement.xml',
    ],
    'sequence' : 1,
    'installable': True,
    'application': True,
    'auto_install': False,

}
