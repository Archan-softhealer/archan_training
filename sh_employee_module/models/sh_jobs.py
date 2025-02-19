# -*- coding: utf-8 -*-
# Copyright (C) Softhealer Technologies.

from odoo import fields, models 

class Jobs(models.Model):
    _name = 'sh.jobs'
    _description = 'Jobs'

    name = fields.Char(string="Name",required=True)
    active = fields.Boolean(string="Active")
    address_id = fields.Many2one('res.partner',string="Address")
    manager_ids = fields.Many2one('sh.employee',string="Manager")
    employee_ids = fields.One2many('sh.employee',inverse_name='job_id',string="Employee") 
    department_ids = fields.Many2one('sh.department',string="Department")  
     
    favorite_user_ids = fields.Many2many('res.users',string="Favorite user")
    # interviewer_ids  = fields.Many2many('res.users', string="Interviewer")
    # extended_interviewer_ids = fields.Many2many('res.users',string="Extended Interviewer")
    
    