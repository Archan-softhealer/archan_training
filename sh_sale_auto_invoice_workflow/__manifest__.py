#-*- coding: utf-8 -*-
# Copyright (C) Softhealer Technologies.

{
    'name': "Sale Order Automatic Workflow",

    'summary': "Sale Order Automatic Workflow",

    'description': """
    """,

    'author': "SoftHealer",
    'website': "https://www.yourcompany.com",

    
    'category': 'Uncategorized',
    'version': '0.1',

    'depends': ['base','web' , 'mail','contacts' , 'account' , 'sale', 'mrp_subcontracting' , 'crm'],

    "data": [
        "security/sh_access_group.xml",
        "security/ir.model.access.csv",
        "views/sh_auto_sale_workflow_views.xml",
        "views/sh_sale_order_views.xml",
        "views/sh_menu_item_config.xml",
        "views/sh_res_config_settings_views.xml",
        
    ],
    'demo': [

    ],
}

