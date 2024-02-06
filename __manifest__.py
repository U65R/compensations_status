{
    'name': "Comensation status",
    'version': '15.0.4.0.0',
    'sequence': 1,

    'description': """
        Compensation status module
    """,

    'author': "My Company",
    'website': "http://abcd.ad",
    
    'category': 'Compensation',
    'license': 'LGPL-3',

    # any module necessary for this one to work correctly
    'depends': ['base'],

    # always loaded
    'data': [
        'security/ir.model.access.csv',
        'views/views.xml',
    ],
}
