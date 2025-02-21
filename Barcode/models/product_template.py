from odoo import models, fields, api
from datetime import datetime

class ProductTemplate(models.Model):
    _inherit = 'product.template'

    @api.model
    def _generate_barcode(self):
        """Generates a barcode with pattern: COMPANY-YYYYMM-SEQ"""
        company_code = self.env.user.company_id.name[:3].upper()  # First 3 letters of company name
        date_part = datetime.today().strftime('%Y%m')  # YYYYMM format
        sequence = self.env['ir.sequence'].next_by_code('product.barcode.sequence') or '0001'
        return f"{company_code}-{date_part}-{sequence}"

    @api.model
    def create(self, vals):
        """Override create method to generate a barcode automatically if not provided"""
        if not vals.get('barcode'):
            vals['barcode'] = self._generate_barcode()
        return super(ProductTemplate, self).create(vals)

    def action_generate_new_barcode(self):
        """Button action to regenerate barcode"""
        for product in self:
            product.barcode = self._generate_barcode()
