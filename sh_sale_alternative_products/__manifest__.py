#-*- coding: utf-8 -*-
# Copyright (C) Softhealer Technologies.

{
    'name': "Sale Alternative Product",

    'summary': "Sale Alternative Product",

    'description': """
       This module helps to Show alternative products that increase sale ratings. 
       Once need to define the product and automatically set it in other alternatives vice versa. 
       If alternative products are stored in the different warehouses also shown here.
    """,

    'author': "Softhealer pvt.ltd",
    'website': "https://www.softhealer.com",
    'sequence': 1,

    'category': 'Uncategorized',
    'version': '0.1',

    'depends': ['base' , 'web'  , 'crm' , 'sale'],

    "data": [
        "security/ir.model.access.csv",
        "security/group_security.xml",
        "views/sh_sale_order_line_views.xml",
        "views/sh_alternative_product_wizard_views.xml",
        "views/sh_alternative_product.xml"
    ],
   
    'demo': [
    ],
}
