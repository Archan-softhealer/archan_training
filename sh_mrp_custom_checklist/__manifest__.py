#-*- coding: utf-8 -*-
# Copyright (C) Softhealer Technologies.

{
    'name': "Mrp Custom Checklist",

    'summary': "Mrp Custom Checklist",

    'description': """
    """,

    'author': "SoftHealer",
    'website': "https://www.yourcompany.com",

    
    'category': 'Manufacturing',
    'version': '0.1',

    'depends': ['mrp', 'stock' , 'mail'],

    "data": [
        "security/ir.model.access.csv",
        "security/sh_mrp_check_list_group.xml",
        "views/sh_import_mrp_custom_checklist_view.xml",
        "views/sh_manufacturing_checklist_template_views.xml",
        "views/sh_manufacturing_checklist_views.xml",
        "views/sh_mrp_production_views.xml",
        "reports/sh_mrp_report.xml"
    ],
}

