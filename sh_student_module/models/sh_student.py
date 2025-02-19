# -*- coding: utf-8 -*-
# Copyright (C) Softhealer Technologies.

from odoo import fields, models

class Employee(models.Model):
    _name = 'sh.student'
    _description = 'Student'
    
    name = fields.Char(string="Name",required=True)
    age  = fields.Integer(string="Age")    
    