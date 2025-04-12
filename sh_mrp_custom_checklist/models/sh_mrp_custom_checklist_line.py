#-*- coding: utf-8 -*-
# Copyright (C) Softhealer Technologies.

from odoo import models, fields, api 
from datetime import date

class Sh_mrp_custom_checklist_line(models.Model):
    _name = 'sh.mrp.custom.checklist.line'
    _description = 'Sh Mrp Custom Checklist Line'
    
    name = fields.Many2one('sh.mrp.checklist' , String ='name')
    description = fields.Char(name="Description")
    date = fields.Date(name="Date" , default=date.today())
    state = fields.Selection([('new' , 'New') , ('completed','Completed') , ('canclled' , 'Canclled')] , default='new' )   
    sh_mrp_production = fields.Many2one('mrp.production')
    
    @api.onchange('name')
    def _onchange_name(self):
        if self.name:
            self.description = self.name.description
            self.state = 'new'  

    
    def handle_complete(self):
        self.state = 'completed'
        
    def handle_cancle(self):
        self.state = 'canclled'