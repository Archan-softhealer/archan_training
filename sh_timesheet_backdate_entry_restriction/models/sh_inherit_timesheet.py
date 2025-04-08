#-*- coding: utf-8 -*-
# Copyright (C) Softhealer Technologies.

from odoo import  fields,models,api
from odoo.exceptions import ValidationError
from dateutil.relativedelta import relativedelta
from datetime import datetime


class Sh_inherit_timesheet(models.Model):
    _inherit = 'account.analytic.line'
    
    @api.model_create_multi
    def create(self, vals_list):
        if not self.env.user.has_group('sh_timesheet_backdate_entry_restriction.sh_restrict_timesheet'):  
            day = self.env.company.restricted_days
            last_date = datetime.now() - relativedelta(days=day)        
            for vals in vals_list:
             if "date" in vals :
                record_date = datetime.strptime(vals['date'], "%Y-%m-%d")
                if record_date < last_date:
                    raise ValidationError(f"You are not allowed to fill timesheet before {day} day(s).")
 
        return super().create(vals_list)   