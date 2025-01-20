from odoo import api, fields, models


class PharmacyInventory(models.Model):
    _name = 'pharmacy.inventory'
    _description = 'Pharmacy Inventory'

    name = fields.Char(string='Medicine Name', required=True)
    product_id = fields.Many2one('product.product', string='Product')
    quantity = fields.Float(string='Quantity', required=True)
    price = fields.Float(string='Price')
    expiry_date = fields.Date(string='Expiry Date')

class PharmacyPrescription(models.Model):
    _name = 'pharmacy.prescription'
    _description = 'Pharmacy Prescription'

    prescription_id = fields.Char(string='Prescription ID', readonly=True)
    patient_id = fields.Many2one('hospital.patient', string='Patient', required=True)
    doctor_id = fields.Many2one('hospital.doctor', string='Doctor', required=True)
    medicine_ids = fields.Many2many('pharmacy.inventory', string='Medicines')
    prescription_date = fields.Datetime(string='Prescription Date', default=fields.Datetime.now)

    @api.model
    def create(self, vals):
        vals['prescription_id'] = self.env['ir.sequence'].next_by_code('pharmacy.inventory') 
        return super(PharmacyPrescription, self).create(vals)

class PharmacyDrugInfo(models.Model):
    _name = 'pharmacy.drug.info'
    _description = 'Pharmacy Drug Information'

    name = fields.Char(string='Drug Name', required=True)
    manufacturer = fields.Char(string='Manufacturer')
    side_effects = fields.Text(string='Side Effects')
    dosage = fields.Text(string='Dosage')
    contraindications = fields.Text(string='Contraindications')
