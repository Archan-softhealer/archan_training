#-*- coding: utf-8 -*-
# Copyright (C) Softhealer Technologies.

from odoo import  models

class test(models.Model):
    _inherit = "sale.order"

class inherit_sal_order_line(models.Model):
    _inherit = 'sale.order.line'
    
    
    
    def open_alternative_product_wizard(self):
        return {
            'name': 'Alternative Product Wizard',
            'type': 'ir.actions.act_window',
            'view_mode': 'form',
            'res_model': 'alternative.product.wizard',
            'target': 'new',
        }