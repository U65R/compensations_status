{
    'name': "Comensation status",
    'version': '15.0.4.0.0',
    'sequence': 1,

    'description': """
        Compensation statut module
    """,

    'author': "pluja",
    'website': "",
    
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