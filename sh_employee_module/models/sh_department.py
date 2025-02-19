# -*- coding: utf-8 -*-
# Copyright (C) Softhealer Technologies.

from odoo import fields, models

class Department(models.Model):
    _name = 'sh.department'
    _description = 'department'

    name = fields.Char(string="Department Name",required=True)
    active = fields.Boolean(string="Active")
    parent_department = fields.Many2one('sh.department',string="Parent Department")
    manager_id = fields.Many2one('sh.employee',string="Manager")
    
    child_ids = fields.One2many('sh.department', inverse_name='parent_department', string="child Ids")
    member_ids = fields.One2many('sh.employee' , inverse_name='department', string="Members")
    jobs_ids = fields.One2many('sh.jobs',inverse_name='department_ids',string="Jobs")