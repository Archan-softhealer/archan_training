#-*- coding: utf-8 -*-
# Copyright (C) Softhealer Technologies.

from odoo import models, fields

class Sh_manufacturing_checklist_template(models.Model):
    _name = 'sh.mrp.checklist.template'
    _description = 'Manufacturing Checklist Template'
    
    sequence = fields.Integer()
    name = fields.Char(name="Name")
    check_list = fields.Many2many('sh.mrp.checklist' , string="Check List")
    company = fields.Many2one('res.company' ,string="Company" , default = lambda self:self.env.company)
    
    