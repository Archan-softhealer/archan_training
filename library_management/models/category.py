# -*- coding: utf-8 -*-
# Copyright (C) Softhealer Technologies.

from odoo import fields , models , api

class Category(models.Model):
    _name = 'library.category'
    _description = "Category"
    
    name=fields.Char(required=True)
    description = fields.Text(name="Description")
    book_ids=fields.One2many('library.book','category_id')
    