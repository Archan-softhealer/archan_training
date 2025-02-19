# -*- coding: utf-8 -*-
# Copyright (C) Softhealer Technologies.

from odoo import fields , models

class Diagnosis(models.Model):
    _name='sh.diagnosis'
    _description = 'Diagnosis'
    
    name = fields.Char(string="name")
    patient = fields.Many2many('sh.patient',string="Patient")