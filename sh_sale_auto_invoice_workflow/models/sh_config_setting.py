#-*- coding: utf-8 -*-
# Copyright (C) Softhealer Technologies.

from odoo import models, fields , api

class sh_config_setting(models.TransientModel):
    _inherit='res.config.settings'
    
    sh_default_workflow = fields.Many2one('sh.auto.sale.workflow',config_parameter="sh_auto_sale_workflow.sh_default_workflow",string='Default Workflow')
    enable_auto_workflow=fields.Boolean(string="Activate Automation",config_parameter="sh_sale_auto_invoice_workflow.enable_auto_workflow",default=False)
    
    
    @api.model
    def set_values(self):
        super(sh_config_setting, self).set_values()
        self.env['ir.config_parameter'].sudo().set_param("sh_sale_auto_invoice_workflow.enable_auto_workflow", self.enable_auto_workflow)
 
        group = self.env.ref('sh_sale_auto_invoice_workflow.sh_res_config_sale_automation_group', raise_if_not_found=False)
        if group:
            if self.enable_auto_workflow:
                group.users = [(6,0, self.env['res.users'].search([]).ids)]
            else:
                group.users = [(5,0,0)]