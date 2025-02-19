# -*- coding: utf-8 -*-
# Copyright (C) Softhealer Technologies.

from odoo import models , fields

class Doctor(models.Model):
    _name = 'sh.doctor'
    _description = 'Doctor'
    
    name = fields.Char(string="Name")
    specialization = fields.Char("Specialization")
    patients = fields.One2many('sh.patient',string="Patients",inverse_name="doctor")