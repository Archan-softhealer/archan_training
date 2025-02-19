# -*- coding: utf-8 -*-
# Copyright (C) Softhealer Technologies.

from odoo import fields , models , api
from odoo.exceptions import UserError

class Borrowing(models.Model):
    _name = 'library.borrowing'
    _description = 'Borrowing'
    
    member_id = fields.Many2one("library.member" , name = "Member ID")
    book_id = fields.Many2one('library.book' , name="Book Id")
    borrow_date = fields.Date(name="Borrow Date")
    return_date = fields.Date(name="Return Date")
    state  = fields.Selection([('borrowed','Borrowed'),('returned','Returned')],name='State' , required=True )
    
    
    @api.model_create_multi
    def create(self, vals_list):
        for rec in vals_list:
          book = self.env['library.book'].browse(rec['book_id'])
          count = book.available_copies  
          
          mem_id = self.env['library.member'].browse(rec['member_id'])
                    
          if rec['state'] == 'borrowed':
                if count<1:
                    raise UserError("This book is not available")
                else:
                    book.available_copies = count - 1
                    # book.members = mem_id
                    mem_id.write({'borrowed_books':[[4,rec['book_id']]]})                   
          else:        
            book.available_copies = count + 1
            mem_id.write({'borrowed_books':[[3,rec['book_id']]]})
            
        result = super(Borrowing, self).create(vals_list)
        return result       
    
    def write(self, vals):
       
       if vals.get('book_id'):
          book = self.env['library.book'].browse(vals['book_id']) #recordset of a book
       else:
          book = self.book_id 
             
       count = book.available_copies  
          
       if vals.get('member_id'):
          mem_id = self.env['library.member'].browse(vals['member_id']) #record set of a member 
       else:
          mem_id = self.member_id
            
       if vals.get('state'):                    
          if vals['state'] == 'borrowed':
                if count<1:
                    raise UserError("This book is not available")
                else:
                    book.available_copies = count - 1
                    # book.members = mem_id
                    mem_id.write({'borrowed_books':[[4,vals['book_id']]]})                   
          else:        
            book.available_copies = count + 1
            mem_id.write({'borrowed_books':[[3,vals['book_id']]]})   
       else:
          if self.state == 'borrowed':
                if count<1:
                    raise UserError("This book is not available")
                else:
                    book.available_copies = count - 1
                    # book.members = mem_id
                    mem_id.write({'borrowed_books':[[4,self.book_id]]})                   
          else:        
            book.available_copies = count + 1
            mem_id.write({'borrowed_books':[[3,self.book_id]]}) 
         
       return super().write(vals)        