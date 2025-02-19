# -*- coding: utf-8 -*-
# Copyright (C) Softhealer Technologies.

from odoo import fields, models

class Age_Category(models.Model):
    _name = 'sh.agecategory'
    _description = 'Age-Category'
    
    name = fields.Char(string="name")
    min_age = fields.Integer(string="min Age")
    max_age = fields.Integer(string="max Age")