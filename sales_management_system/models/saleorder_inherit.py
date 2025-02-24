from odoo import fields , models , api


class inherit_sale_order(models.Model):
    _inherit = 'sale.order'
     
    warranty_applicable = fields.Boolean(name='Is Warranty Applicable?')
    
    @api.model_create_multi
    def create(self, vals_list):
        record = super(inherit_sale_order, self).create(vals_list)        
        for rec in record:
            if rec.warranty_applicable:          
                self.env['sale.warranty'].create({'name':rec.name,'sale_order_id':record.id})

        return record       
            