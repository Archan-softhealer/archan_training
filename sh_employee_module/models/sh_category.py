# -*- coding: utf-8 -*-
# Copyright (C) Softhealer Technologies.

from odoo import fields, models

class Category(models.Model):
    _name = 'sh.category'
    _description = 'Category'

    name = fields.Char(string="Name",required=True)
    active = fields.Boolean(string="Active")
    employee_ids = fields.Many2many('sh.employee',string="Employees")
    ref = fields.Char("reference")