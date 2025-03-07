#-*- coding: utf-8 -*-
# Copyright (C) Softhealer Technologies.

from odoo import fields, models , api
from datetime import date

class Timesheet(models.Model):
    _name = 'sh.timesheet'
    _description = 'Timesheet'
    _inherit = ['mail.thread.cc',
                'mail.activity.mixin',
                'utm.mixin',
                'mail.tracking.duration.mixin',
               ]
    
    user_id = fields.Many2one('res.users' , name = "user")
    name = fields.Char(name='timesheet' , required=True)
    description = fields.Html(string="Description")
    date = fields.Date(string="Date" , default = date.today())
    total_hours = fields.Float(string='Total Hours' , compute='total_task')
    tag_ids = fields.Many2many('sh.tag',string='Tags')
    state = fields.Selection([('draft','Draft') , ('submitted','Submitted') , ('approved','Approved'),('reject','Reject')] ,default='draft')
    rejection_reason  = fields.Text('Rejection Reason' , readonly=True)
    task_ids = fields.One2many('sh.task','timesheet' , string='Tasks')
    count = fields.Integer(compute='total_task')
    
    def submit_manager_button(self):
        self.state = 'submitted'
    
    def approve_button(self):
       self.state = 'approved'
       
    @api.depends('task_ids')   
    def total_task(self):
        for rec in self:
            rec.count = len(rec.task_ids)
            rec.total_hours = sum(task.amount for task in rec.task_ids)
        
    # @api.depends('task_ids')
    # def _total_hours(self):
    #     for rec in self:
    #        rec.total_hours = sum(task.amount for task in rec.task_ids)
        