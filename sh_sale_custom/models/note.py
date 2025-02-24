# -*- coding: utf-8 -*-

from odoo import models,fields


class sh_Note(models.Model):
    _name='sh.note'
    
    name = fields.Char('Name')


class sale_order_inherit(models.Model):
    _inherit='sale.order'
    
    custom_note = fields.Many2many('sh.note',string="Note")
    
class sale_orderline_inherit(models.Model):
    _inherit='sale.order.line'
    
    custom_note = fields.Many2one('sh.note',string="Note")

class crm_inherit(models.Model):
    _inherit = 'crm.lead'
    
    custom_field1 = fields.Char('custom filed1')
    custom_field2 = fields.Char('custom filed2')    