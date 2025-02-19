# -*- coding: utf-8 -*-
# Part of Softhealer. See LICENSE file for full copyright and licensing details.
{
    'name': 'sh_student_management',
    'version': '1.0',
    'summary': 'student management',
    'sequence': 2,
    'description': """
    all about student management like attendence etc..
    """,
    'category': 'Human Resources/Student',
    'website': 'https://www.odoo.com/app/',
    'depends': ['base_setup','web'],
    "data": [
        "security/ir.model.access.csv",
        "views/student_view.xml",
    ],
   
    'installable': True,
    'application': True,
    'assets': {
    },
    'license': 'LGPL-3',
}