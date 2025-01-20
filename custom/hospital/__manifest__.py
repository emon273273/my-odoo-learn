{
    "name":"hospital",
    "author":"emon",
    "version":"1.0",
    "catagory":"Custom",
    "license":"LGPL-3",
<<<<<<< HEAD
    'depends': ['base', 'hr', 'product','account'],
    "data":[
        'views/pharmacy_views.xml',
        'security/ir.model.access.csv',
        'data/sequence_data.xml',
        'views/account_move_view.xml',
        'views/doctor.xml',
        'views/appointment_views.xml',
        'views/patient_registation.xml',
=======
    "data":[
        'security/ir.model.access.csv',
        'views/patient.xml',
        'views/doctor.xml',
>>>>>>> d7f0c7be20082c19d4b8ea941d85b61b12d13a58
        'views/menu.xml'
    ],
     'installable': True,
    'application': True,  # Makes it appear in the Apps menu
    'auto_install': False,
}