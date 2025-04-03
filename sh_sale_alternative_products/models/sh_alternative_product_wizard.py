#-*- coding: utf-8 -*-
# Copyright (C) Softhealer Technologies.


from odoo import fields, models , api

class alternative_product_wizard(models.TransientModel):            
    _name = 'alternative.product.wizard'
    _description = 'Alternative Product Wizard'

    
    name=fields.Many2one('sale.order.line',readonly=True)
    product_id=fields.Many2one("product.product",readonly=True)
    alt_product=fields.Many2many("product.product",compute='_compute_product_alternative')
    alternative_product_id=fields.Many2one("product.product")
    
    @api.depends('product_id')
    def _compute_product_alternative(self):
        for record in self:
            record.alt_product=record.product_id.alternative_product.ids    
           
    
    def get_record_set(self):
        model=self.env.context['active_model']
        id=self.env.context['active_id']        
        rec=self.env[model].browse(id)

        return rec
    
    @api.model
    def default_get(self, fields_list):
        rec=self.get_record_set()
        rtn= super().default_get(fields_list)
        rtn.update({'name' :rec.id,'product_id':rec.product_id.id})
        return rtn
    
    def replace_method(self):
        if self.alternative_product_id:
            rec=self.get_record_set()
            rec.product_id=self.alternative_product_id
