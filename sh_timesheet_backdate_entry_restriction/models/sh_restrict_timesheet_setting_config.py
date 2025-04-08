#-*- coding: utf-8 -*-
# Copyright (C) Softhealer Technologies.

from odoo import models, fields

class sh_restrict_timesheet_setting_config(models.TransientModel):
    _inherit = 'res.config.settings'
    
    restricted_days = fields.Integer(string="Restricted Timesheet After" ,
                                     related='company_id.restricted_days',
                                     readonly=False)


class sh_res_company_timesheet(models.Model):
    _inherit = 'res.company'
    
    restricted_days = fields.Integer(string="Restricted Timesheet After")
    