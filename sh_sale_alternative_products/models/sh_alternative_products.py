#-*- coding: utf-8 -*-
# Copyright (C) Softhealer Technologies.

from odoo import fields, models , Command , api


class Alternaive_Product(models.Model):
    _inherit = 'product.product'
    
    alternative_product = fields.Many2many('product.product',
                                           relation='product_alternative_rel' ,
                                           column1='src_id' , column2='dest_id' , 
                                           string="Alternaive Product"  , 
                                           )

    def write(self, vals):
       rtn = super().write(vals)
       if 'alternative_product' in vals:
            for val in vals['alternative_product']:
                if val[0]==4: 
               
                    recs=self.env['product.product'].browse(self.alternative_product.ids)
                    all_product=self.alternative_product.ids + [self.id] 
                    for id in all_product:
                        for rec in recs:   
                           if id!=rec.id:  
                            rtn = super(Alternaive_Product,rec).write({'alternative_product':[Command.link(id)]}) 
                if val[0]==3:
                    rec = self.browse(val[1])
                    rec.write({'alternative_product':[(5,0,0)]}) 
                    self.env.execute_query(api.SQL(f"delete FROM product_alternative_rel WHERE dest_id={rec.id} ;"))                   
                    
       return rtn



