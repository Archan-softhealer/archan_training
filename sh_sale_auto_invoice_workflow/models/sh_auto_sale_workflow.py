#-*- coding: utf-8 -*-
# Copyright (C) Softhealer Technologies.

from odoo import fields, models , api


class Sh_auto_sale_workflow(models.Model):
    _name = 'sh.auto.sale.workflow'
    _description = 'Auto Sale Workflow'
    
    name = fields.Char(string="Name")
    validate_order = fields.Boolean(string="Delivery Order")
    create_invoice = fields.Boolean("Create Invoice")
    validate_invoice = fields.Boolean(string="Validate Invoice")
    register_payment = fields.Boolean(string="Register Payment")
    send_invoice_by_email = fields.Boolean(string="Send Invoice By Email")
    sale_journal = fields.Many2one('account.journal' , required=True , domain=[('type','=','sale')])
    payment_journal = fields.Many2one('account.journal' , domain=[('type','in',('bank','cash'))] , required=True)
    payment_method = fields.Many2one('account.payment.method' , string="Payment Method" , domain=[('payment_type' , '=' , 'inbound')] , required=True)
    company = fields.Many2one('res.partner' , string="Comapny" , required=True) 
    
    @api.onchange('create_invoice' , 'validate_invoice' , 'register_payment' )
    def handle_checkbox(self):
       if self.create_invoice==False:
           self.validate_invoice = False
           
       if self.validate_invoice==False:
           self.register_payment = False
           self.send_invoice_by_email=False