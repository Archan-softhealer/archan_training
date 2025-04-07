#-*- coding: utf-8 -*-
# Copyright (C) Softhealer Technologies.

from odoo import models, fields, api , Command

class Sh_meeting(models.Model):
    _inherit = 'calendar.event'
    
    sh_timesheet_ids = fields.One2many('account.analytic.line' , 'sh_meeting_ids')
    project_ids = fields.Many2one('project.project' , string='Project')
    task_ids = fields.Many2one('project.task' , string="Task")
    
    @api.model_create_multi
    def create(self, vals_list):    
        record = super().create(vals_list) 
        print("--------->>>>>",record.partner_ids)
        for partner in record.partner_ids:       
           timesheet = self.env['account.analytic.line'].create({'name': record.name,        
                    'date': record.start,
                    'project_id':record.project_ids.id,
                    'task_id':record.task_ids.id,
                    'partner_id': partner.id,
                    'sh_meeting_ids': record.id,
                    'unit_amount': record.duration
                })
           record.sh_timesheet_ids = [(4,timesheet.id)]
               
        return record
    
    def write(self, vals):
        rec = super(Sh_meeting, self).write(vals)
        if 'project_ids' or 'task_ids' or 'duration' or 'name' or 'start' or 'partner_ids' in vals.keys():
            if 'name' in vals.keys():
                self.sh_timesheet_ids.write({'name': self.name})
            if 'project_ids' in vals.keys():
                self.sh_timesheet_ids.write({'project_id': self.project_ids.id})
            if 'task_ids' in vals.keys():
                self.sh_timesheet_ids.write({'task_id': self.task_ids.id})
            if 'start' in vals.keys():
                self.sh_timesheet_ids.write({'date': self.start})
                self.show_reason = True
            if 'duration' in vals.keys():
                self.sh_timesheet_ids.write({'unit_amount': self.duration})
                
            if 'partner_ids' in vals.keys():
                for val in vals['partner_ids']:
                    if val[0] == 4:
                        timesheet = self.env['account.analytic.line'].create({
                            'name': self.name,
                            'project_id': self.project_ids.id,
                            'partner_id': val[1],
                            'task_id': self.task_ids.id,
                            'unit_amount': self.duration,
                            'date': self.start,
                        })
                        self.sh_timesheet_ids = [(4, timesheet.id)]
                    elif val[0] == 3:
                            delete_timesheet = self.sh_timesheet_ids.filtered(lambda p: p.partner_id.id == val[1])
                            if len(delete_timesheet) == 1 :
                                 delete_timesheet.unlink()  
        return rec

