#-*- coding: utf-8 -*-
# Copyright (C) Softhealer Technologies.

{
    'name': "Sale Order History",

    'summary': "Sale Order History",

    'description': """
    """,

    'author': "SoftHealer",
    'website': "https://www.yourcompany.com",

    
    'category': 'Uncategorized',
    'version': '0.1',

    'depends': ['base','web' , 'mail','contacts' , 'account' , 'sale', 'mrp_subcontracting' , 'crm'],

    "data": [
        "security/ir.model.access.csv",
        "security/sh_access_group.xml",
        "views/sh_res_config_settings_views.xml",
        "views/sh_sale_order_views.xml"
    ],
}

