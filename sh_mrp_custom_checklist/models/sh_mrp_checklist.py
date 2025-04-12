#-*- coding: utf-8 -*-
# Copyright (C) Softhealer Technologies.

from odoo import models, fields

class Sh_manufacturing_checklist(models.Model):
    _name = 'sh.mrp.checklist'
    _description = 'Manufacturing Checklist'
    
    sequence = fields.Integer()
    name = fields.Char(name="Name")
    description = fields.Char(name="descripion")
    company = fields.Many2one('res.company' , name="Company" , default = lambda self:self.env.company)    