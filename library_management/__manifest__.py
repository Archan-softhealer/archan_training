# -*- coding: utf-8 -*-
# Part of Softhealer. See LICENSE file for full copyright and licensing details.
{
    'name': 'Library',
    'version': '1.0',
    'summary': 'Library management',
    'sequence': 2,
    'description': """
    all about Library management like books, author etc..
    """,
    'category': 'Human Resources/Library',
    'website': 'https://www.odoo.com/app/',
    'depends': ['base_setup','web'],
    "data": [
        "security/ir.model.access.csv",
        "views/library_book_views.xml",
        "views/library_category_views.xml",
        "views/library_member_views.xml",
        "views/library_borrowing_views.xml",
        "views/library_menu.xml",
    ], 
    'image':[
      'static/description/library.png'
    ],    
    'installable': True,
    'application': True,
    'assets': {
    },
    'license': 'LGPL-3',
}