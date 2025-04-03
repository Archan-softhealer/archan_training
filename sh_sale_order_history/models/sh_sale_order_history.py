#-*- coding: utf-8 -*-
# Copyright (C) Softhealer Technologies.

from odoo import models,fields,api , Command
from dateutil.relativedelta import relativedelta
from datetime import datetime

class Sh_Sale_order_history(models.Model):
    _inherit = ["sale.order"]

    sh_sale_order_history = fields.One2many('sale.order.line' ,readonly=False,  inverse_name='order_id' ,
                                           string='Order History' , compute = '_compute_sale_history')
    sh_reorder = fields.Boolean("Reorder")  
    
    @api.depends('partner_id')  
    def _compute_sale_history(self):
        day=self.company_id.sh_last_no_of_days_orders
        date=datetime.now() - relativedelta(days=day) 
        for rec in self:
             record_set= self.env['sale.order.line'].search([ ('order_partner_id' , '=' , rec.partner_id.id), 
                                                                             ('order_id' , '!=' , rec.id) ,
                                                                             ('sh_date_order' , '>=' , date),
                                                                             ('state' , 'in' , ([state.value for state in self.company_id.stages]))], 
                                                                             limit=rec.company_id.sh_last_no_of_orders,order="sh_date_order desc")
                                                                           
             print("=========>",record_set)                                                              
             rec.sh_sale_order_history = [Command.set(record_set.ids)] 
             
    def view_lines_reorder(self):
        record = self.sh_sale_order_history.search([('check_bool' , '=' , True)])
        if record:
            for rec in self.sh_sale_order_history:
                if rec.check_bool: 
                    rec.move_to_line_order()
        else:
            for rec in self.sh_sale_order_history:
                rec.move_to_line_order()                
