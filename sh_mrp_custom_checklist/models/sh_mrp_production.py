#-*- coding: utf-8 -*-
# Copyright (C) Softhealer Technologies.

from odoo import models, fields, api , Command

class Sh_mrp_product(models.Model):
    _inherit = "mrp.production"
    
    checklist_completed = fields.Integer(string="Checklist Completed" , compute = '_calculate_complete_percantage')
    checklist_template = fields.Many2many('sh.mrp.checklist.template' , string="Checklist Template")
    sh_checklist_line = fields.One2many('sh.mrp.custom.checklist.line' , inverse_name='sh_mrp_production' ,readonly=False) 
     
    @api.onchange('checklist_template')
    def change_temp(self):
        self.sh_checklist_line = [(5,0,0)]
        if self.checklist_template.check_list:
            for rec in self.checklist_template.check_list:
                if rec.id not in self.sh_checklist_line.ids:
                    dict1 = {'name':rec.id,'description':rec.description,'date':self.date_start,'state':'new'}
                    self.sh_checklist_line = [(0,0,dict1)] 
                    
    @api.depends('checklist_completed')                
    def _calculate_complete_percantage(self):
       for rec in self:
            completed = 0
            total = len(rec.sh_checklist_line)
            if total:
                completed = sum(1 for line in rec.sh_checklist_line if line.state == 'completed')
                rec.checklist_completed = (completed / total) * 100
            else:
                rec.checklist_completed = 0          
 