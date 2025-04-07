#-*- coding: utf-8 -*-
# Copyright (C) Softhealer Technologies.

from odoo import models, fields

class sh_config_company_timesheet(models.TransientModel):
    _inherit = 'res.config.settings'
    
    group_enable_timesheet = fields.Boolean(string="Create Timesheet", 
                                            readonly=False,
                                            related='company_id.group_enable_timesheet',  
                                            help="Enable timesheet for employees",
                                            implied_group='sh_calendar_meeting_timesheet.enable_timesheet_group')


class sh_res_company(models.Model):
    _inherit = 'res.company'    
    
    group_enable_timesheet = fields.Boolean("Create Timesheet")