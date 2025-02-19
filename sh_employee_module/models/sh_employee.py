# -*- coding: utf-8 -*-
# Copyright (C) Softhealer Technologies.

from odoo import fields, models , api
from datetime import date
import pytz , random

_tzs = [(tz, tz) for tz in sorted(pytz.all_timezones, key=lambda tz: tz if not tz.startswith('Etc/') else '_')]
def _tz_get(self):
    return _tzs

class Employee(models.Model):
    _name = 'sh.employee'
    _description = 'Employee'
    
    name = fields.Char(string="Name",required=True)
    emp_salary=fields.Float(string="Salary")
    company_name=fields.Char(string="Company Name")
    company_website=fields.Char(string="Company  Website")
    emp_role=fields.Char(string="Role")
    work_mobile_number=fields.Char(string="Work Mobile Number")
    personal_mobile_number=fields.Char(string="Personal Contact Number")
    Work_email = fields.Text(string="Work Email")
    personal_emp_email = fields.Text(string="Personal Email")
    address = fields.Text(string="Address")
    birthdate=fields.Date(string="DOB(Date Of Birth)")
    gender=fields.Selection([("male","Male"),("female","Female")],string="Gender")
    height = fields.Float(string="Height")
    weight = fields.Float(string="Weight")
    place_of_birth=fields.Text(string="Place Of Birth")
    age=fields.Integer(string="Age" , compute='_compute_age',readonly=False)
    blood_group=fields.Text(string="Blood Group")
    marital_status=fields.Selection([("married","Married"),("unmarried","Unmarried")],string="Marital Status")
    emp_photo=fields.Image()
    
    country_id = fields.Many2one('res.country', string="Country")
    birth_country_id = fields.Many2one('res.country', string="Country of Birth")
    job_id = fields.Many2one('sh.jobs',"Jobs")
    department=fields.Many2one('sh.department',string="Department")
    
    category = fields.Many2many('sh.category',string="category")
    user_id = fields.Many2one('res.users', string="userID")
    
    tz = fields.Selection(_tzs, string='Timezone', default=lambda self: self._context.get('tz'),)
    uid = fields.Char("Id",readonly=True)
    
    Category_id = fields.Many2one("sh.category",string="category_emp")
    ref = fields.Char(string="ref")
    
    agecategory = fields.Many2one("sh.agecategory", string="Age category")
    
    @api.depends('birthdate')
    def _compute_age(self):
        today = date.today()
        for employee in self:
           if employee.birthdate and employee.birthdate < today: 
            employee.age= today.year - employee.birthdate.year - ((today.month,today.day) < (employee.birthdate.month,employee.birthdate.day))
           else:
               employee.age=0
               
     
     
    @api.onchange('user_id')
    def _onchange_userID(self): 
        if self.user_id:
            self.name=self.user_id.name
            self.tz = self.user_id.tz
            
    @api.model_create_multi
    def create(self, vals_list):
         print("===========>>>>>>",vals_list)
         for vals in vals_list:
            print("===================>>>",vals)
            vals["name"] =  vals["name"].upper()
            vals["uid"] = "Emp"+ str(random.randint(1000, 9999))   
             
            if vals["personal_mobile_number"]:
                vals["personal_mobile_number"] = vals["personal_mobile_number"].strip()
                if not vals["personal_mobile_number"].startswith('+91'): 
                        vals["personal_mobile_number"] = '+91' + vals["personal_mobile_number"] 
                        
            if vals['age']:
              age_category = self.env['sh.agecategory'].search([('min_age','<=',vals["age"]),('max_age','>',vals["age"])]) 
              if age_category:
               vals['agecategory'] = age_category.id              
        
         result = super(Employee, self).create(vals_list)
         if result.Category_id:
          result.ref = result.Category_id.ref
         print("result::::",result.ref)
         
         return result
     
     
    def write(self,vals):
        if vals.get("name"): 
            vals["name"] = vals["name"].upper()
        else:
           if[self.name] :
            vals["name"] = self.name.upper()
            
        if vals.get("personal_mobile_number"):   
            vals["personal_mobile_number"] = vals["personal_mobile_number"].strip()
            if not vals["personal_mobile_number"].startswith('+91'): 
                vals["personal_mobile_number"] = '+91' + vals["personal_mobile_number"]
        else:
            if self.personal_mobile_number:
                vals["personal_mobile_number"] = self.personal_mobile_number.strip()
                if not vals["personal_mobile_number"].startswith('+91'): 
                    vals["personal_mobile_number"] = '+91' + self.personal_mobile_number
                    
        if vals.get("age"):
           age_category = self.env['sh.agecategory'].search([('min_age','<=',vals["age"]),('max_age','>',vals["age"])]) 
           if age_category:
             vals['agecategory'] = age_category.id  
        else:
             age_category = self.env['sh.agecategory'].search([('min_age','<=',vals["age"]),('max_age','>',vals["age"])])   
             vals['agecategory'] = age_category.id               
                                         
        return super().write(vals)
