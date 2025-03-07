#-*- coding: utf-8 -*-
# Copyright (C) Softhealer Technologies.

from odoo import fields, models , api

class Rejection(models.TransientModel):
    _name='sh.rejection'
    _description='Rejection'
    
    name = fields.Text('Rejection Reason' , required=True)
    
    def submit_reason(self):
        active_id = self.env.context["active_id"]
        
        record = self.env['sh.timesheet'].browse(active_id)
        record.rejection_reason = self.name
        record.state = 'reject'
