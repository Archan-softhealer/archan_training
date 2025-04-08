#-*- coding: utf-8 -*-
# Copyright (C) Softhealer Technologies.

{
    'name': "Timesheet Backdate Entry Restriction",

    'summary': "Timesheet Backdate Entry Restriction",

    'description': """
    """,

    'author': "SoftHealer",
    'website': "https://www.yourcompany.com",

    
    'category': 'Uncategorized',
    'version': '0.1',

    'depends': ['project' , 'mail' , 'account' ,'timesheet_grid' , 'hr' , 'sale' , 'base_setup' , 'web' , 'sale_timesheet'],

    "data": [
        "security/sh_restricted_timesheet.xml",
        "views/sh_res_config_settings_views.xml"
    ],
}

