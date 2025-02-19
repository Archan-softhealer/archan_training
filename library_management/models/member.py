# -*- coding: utf-8 -*-
# Copyright (C) Softhealer Technologies.

from odoo import fields, models , api
import random

class Member(models.Model):
    _name = 'library.member'
    _description = "Member"
    
    name = fields.Char(required=True)
    borrowed_books = fields.Many2many('library.book',name="Borrowed Books")
    membership_id = fields.Char(name="Member ID",readonly=True , store=True)
    email = fields.Char(name="E-mail")
    phone = fields.Integer(name="Phone")
    
    @api.model_create_multi
    def create(self , vals_list):
        for rec in vals_list:
            rec["membership_id"] = "mem" + str(random.randint(1000, 9999)) 
      
        result = super(Member, self).create(vals_list)
        return result
    