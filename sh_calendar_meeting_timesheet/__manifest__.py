#-*- coding: utf-8 -*-
# Copyright (C) Softhealer Technologies.

{
    'name': "Calendar Meeting Timesheet",

    'summary': "Calendar Meeting Timesheet",

    'description': """
    """,

    'author': "SoftHealer",
    'website': "https://www.yourcompany.com",

    
    'category': 'Uncategorized',
    'version': '0.1',

    'depends': ['base_setup','web' ,'calendar', 'hr' , 'project','timesheet_grid'],

    "data": [
        "security/sh_timesheet_group.xml",
        "views/sh_res_config_settings_views.xml",
        "views/sh_calendar_event_views.xml",
    ]
}

