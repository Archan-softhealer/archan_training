#-*- coding: utf-8 -*-
# Copyright (C) Softhealer Technologies.

from odoo import fields, models , api

class task(models.Model):
    _name = 'sh.task'
    _description = 'Task'
    
    name = fields.Char('task')
    amount = fields.Float('Amount')
    timesheet = fields.Many2one('sh.timesheet' , string='Timesheet')