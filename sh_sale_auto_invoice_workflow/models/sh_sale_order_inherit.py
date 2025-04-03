#-*- coding: utf-8 -*-
# Copyright (C) Softhealer Technologies.

from odoo import fields, models , api

class sh_sale_oder_inherit(models.Model):
   _inherit = 'sale.order'

   sale_workflow = fields.Many2one('sh.auto.sale.workflow')
   
  
   @api.model
   def default_get(self, fields):
     rec=self.env['sh.auto.sale.workflow'].search([('id','=',(self.env['ir.config_parameter'].get_param('sh_auto_sale_workflow.sh_default_workflow')))])
     rtn = super().default_get(fields)
     rtn.update({'sale_workflow' : rec.id})      
     return rtn 

   def action_confirm(self):
    rtn =  super().action_confirm()
    if self.sale_workflow.validate_order:
        print("-------=============>>>>>>>")
        self.env['stock.picking'].search([('id','in',self.picking_ids.ids)]).button_validate()
    if self.sale_workflow.create_invoice:
        invoice = self._create_invoices()    
               
        if self.sale_workflow.validate_invoice:
            invoice.action_post()
            
        if self.sale_workflow.register_payment: 
                            self.env["account.payment.register"].with_context(
                                active_model="account.move",
                                active_ids=invoice.ids,
                                payment_method_line_id = self.sale_workflow.payment_method.id,
                                journal_id = self.sale_workflow.payment_journal.id
                            ).create({"group_payment": False}).action_create_payments()
    
    if self.sale_workflow.send_invoice_by_email:
        self.env['account.move.send.wizard'].create({'move_id':invoice.id}).action_send_and_print()
       
       
    return rtn