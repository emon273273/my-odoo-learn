{
    "name":"hospital",
    "author":"emon",
    "version":"1.0",
    "catagory":"Custom",
    "license":"LGPL-3",
    "data":[
        'security/ir.model.access.csv',
        'views/patient_front_desk.xml',
        'views/patient_emergency.xml',
        'views/doctor_emergency.xml',
        'views/doctor.xml',
        'views/menu.xml'
    ],
     'installable': True,
    'application': True,  # Makes it appear in the Apps menu
    'auto_install': False,
}