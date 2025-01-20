{
    "name":"hospital",
    "author":"emon",
    "version":"1.0",
    "catagory":"Custom",
    "license":"LGPL-3",
    'depends': ['base', 'hr', 'product','account'],
    "data":[
        'views/pharmacy_views.xml',
        'security/ir.model.access.csv',
        'data/sequence_data.xml',
        'views/account_move_view.xml',
        'views/doctor.xml',
        'views/appointment_views.xml',
        'views/patient_registation.xml',
        'views/menu.xml'
    ],
     'installable': True,
    'application': True,  # Makes it appear in the Apps menu
    'auto_install': False,
}