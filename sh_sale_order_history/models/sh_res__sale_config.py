#-*- coding: utf-8 -*-
# Copyright (C) Softhealer Technologies.

from odoo import models, fields, api

class sh_config_setting_sale_history(models.TransientModel):
    _inherit = 'res.config.settings'
    
    sh_last_no_of_orders = fields.Integer("Last NO. of Orders" , related='company_id.sh_last_no_of_days_orders' , readonly=False)
    sh_last_no_of_days_orders = fields.Integer("Last NO. of Day's Orders" , related='company_id.sh_last_no_of_days_orders' ,readonly=False)
    stages = fields.Many2many('ir.model.fields.selection' , string='Stages',domain=[('field_id.model','=','sale.order'),('field_id.name','=','state')] , related='company_id.stages' , readonly=False)
    group_enable_reorder = fields.Boolean(string='Enable Recorder' , related='company_id.group_enable_reorder' , implied_group="sh_sale_order_history.enable_recorder" , readonly=False)
    
class Sh_Res_Company(models.Model):
    _inherit = 'res.company'
    
    sh_last_no_of_orders = fields.Integer("Last NO. of Orders")
    sh_last_no_of_days_orders = fields.Integer("Last NO. of Day's Orders")
    stages = fields.Many2many('ir.model.fields.selection' , string='Stages',domain=[('field_id.model','=','sale.order'),('field_id.name','=','state')] , store=True)
    group_enable_reorder = fields.Boolean(string='Enable Recorder')

    
    
    
    
