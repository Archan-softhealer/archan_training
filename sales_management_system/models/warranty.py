from odoo import fields , models , api
from dateutil.relativedelta import relativedelta

class Warranty(models.Model):
    _name = 'sale.warranty'
    _description = 'Warranty'
    
    name = fields.Char('Name')
    sale_order_id = fields.Many2one('sale.order', name='Sale Order')
    warranty_period = fields.Integer(name='Warranty period in Month' ,default=12)
    warranty_expiry_date = fields.Date(name='Warranty Expiry Date',compute = '_compute_expirydate')
    
    @api.depends('warranty_period','sale_order_id.date_order')
    def _compute_expirydate(self):
            for rec in self:
               if rec.sale_order_id and rec.sale_order_id.date_order: 
                 rec.warranty_expiry_date = fields.Date.from_string(rec.sale_order_id.date_order) + relativedelta(months=rec.warranty_period)
               else:
                 rec.warranty_expiry_date = False


    