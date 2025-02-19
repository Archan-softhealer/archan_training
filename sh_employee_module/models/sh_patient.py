# -*- coding: utf-8 -*-
# Copyright (C) Softhealer Technologies.

from odoo import models , fields

class Patient(models.Model):
    _name='sh.patient' 
    _description='Patient'
    
    name = fields.Char("Patient Name")
    age = fields.Integer(string="Age")
    doctor = fields.Many2one('sh.doctor',string="Doctor")
    diagnosis = fields.Many2many('sh.diagnosis',string="Diagnosis")