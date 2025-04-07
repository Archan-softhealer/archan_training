#-*- coding: utf-8 -*-
# Copyright (C) Softhealer Technologies.


from odoo import fields,models,api

class Sh_timesheet(models.Model):
    _inherit = 'account.analytic.line'
    
    sh_meeting_ids = fields.Many2one('calendar.event')