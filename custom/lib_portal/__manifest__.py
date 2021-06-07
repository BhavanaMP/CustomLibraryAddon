{
    'name' : 'Library Portal',
    'version' : '1.1',
    'author' : 'bloopark', 
    'summary': 'Library Management System',
    'description': """
    Module to digitalise and manage the library operations
    """,
    'depends' : [
        'product',
        'contacts',
        'hr'
        ],
    'sequence' : 1,
    'installable': True,
    'application': True,
    'auto_install': False,
    'category' : 'Library',
    'data' : [ 
        'security/ir.model.access.csv',
        'views/libraryManagement.xml',

    ],

}
