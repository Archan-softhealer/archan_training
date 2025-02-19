# -*- coding: utf-8 -*-
# Copyright (C) Softhealer Technologies.

from odoo import fields , models ,api
from odoo.exceptions import ValidationError

class Book(models.Model):
    _name='library.book'
    _description = "Books"
    
    name=fields.Char(required=True,string="Book Name")
    author = fields.Char(name="Author") 
    published_date = fields.Date(name="Published Date")
    available_copies = fields.Integer(name="Available Copies")
    category_id=fields.Many2one('library.category',string="Category")
    members = fields.Many2many('library.member',string="Members")
    
    
    @api.onchange('name')
    def book_category_check(self):
        if self.name:
            category_id=self.env['library.category'].search([])
            for char in str(self.name).split(' '):
                for data in category_id:
                    if data.name.lower() in char.lower():
                        self.category_id=data.id
                    elif data.name.lower() in self.name.lower():
                        self.category_id = data.id
   
    @api.model_create_multi 
    def create(self, vals_list):  
        for rec in vals_list:
            if not rec["category_id"]:
              raise ValidationError("Please fill in the Category field.")
        return super(Book, self).create(vals_list)
    
    def unlink(self):
        
        for rec in self: 
            # recs = self.env['library.member'].browse(rec['members'])
            # print("recs========>",recs)
            
            if rec.members:
                 raise ValidationError("This Book is borrowed you can't remve it. ")
        
        return super().unlink() 