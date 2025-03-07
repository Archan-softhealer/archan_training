# -*- coding: utf-8 -*-
{
    'name': "timeSheet",

    'summary': "Short (1 phrase/line) summary of the module's purpose",

    'description': """
Long description of module's purpose
    """,

    'author': "My Company",
    'website': "https://www.yourcompany.com",
    'sequence': 1,

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/15.0/odoo/addons/base/data/ir_module_category_data.xml
    # for the full list
    'category': 'Uncategorized',
    'version': '0.1',

    # any module necessary for this one to work correctly
    'depends': ['base' , 'web' , 'mail' , 'base' , 'crm' , 'sale'],

    # always loaded
    "data": [
        "security/timesheet_security.xml",
        "security/ir.model.access.csv",
        "views/sh_tag_views.xml",
        "views/sh_task_views.xml",
        "views/sh_timesheet_views.xml",
        "views/sh_rejection_views.xml",
        "report/manifest_report_view.xml"
    ],
   
    # only loaded in demonstration mode
    'demo': [
        'demo/demo.xml',
    ],
}

