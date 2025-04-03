#-*- coding: utf-8 -*-
# Copyright (C) Softhealer Technologies.

from odoo import models,fields,api
class Sh_Sale_order_history(models.Model):
    _inherit = ["sale.order.line"]
   
    check_bool = fields.Boolean(readonly=False) 
    sh_date_order = fields.Datetime(related='order_id.date_order', string="Date Order",  readonly=False)
    sh_sale_line_reorder = fields.Boolean("Reorder")  

    def view_line_order(self):
        return{
            'type':'ir.actions.act_window',
            'res_model':'sale.order',
            'view_mode':'form',
            'res_id':self.order_id.id
        }
    def move_to_line_order(self):
            currant_id=self._context['params']['resId']
            if self.check_bool:
                self.check_bool=False
            vals = {
                'order_id':currant_id,
                'product_id':self.product_id.id,
                'price_unit':self.price_unit,
                'tax_id':self.tax_id,
            }
            self.create(vals)
        
             