# -*- coding: utf-8 -*-
# Part of Softhealer. See LICENSE file for full copyright and licensing details.
{
    'name': 'Employee',
    'version': '1.0',
    'summary': 'Employee management',
    'sequence': 1,
    'description': """
    all about employee management like payroll, attendence etc..
    """,
    'category': 'Human Resources/Employees',
    'website': 'https://www.odoo.com/app/',
    'depends': ['base_setup','web'],
    "data": [
        "security/ir.model.access.csv",
        "views/employee_view.xml",
        "views/sh_department_views.xml",
        "views/sh_jobs_views.xml",
        "views/sh_category_views.xml",
        "views/sh_doctor_views.xml",
        "views/sh_patient_views.xml",
        "views/sh_diagnosis_views.xml",
        "views/sh_agecategory_views.xml",
        "views/menu_items.xml",
    ],
   
    'installable': True,
    'application': True,
    'assets': {
    },
    'license': 'LGPL-3',
}