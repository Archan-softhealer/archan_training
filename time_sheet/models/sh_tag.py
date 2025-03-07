 #-*- coding: utf-8 -*-
# Copyright (C) Softhealer Technologies.

from odoo import fields, models , api

class Tag(models.Model):
    _name='sh.tag'
    _description='Tag'
    
    name = fields.Char('Tag')
    timesheet = fields.Many2many('sh.timesheet' , string='TimeSheet')