from odoo import api, fields, models

class HospitalPatient(models.Model):
    _name = "hospital.patient"
    _description = "This is just for testing purposes"
    patient_id=fields.Char(string="Patient ID",readonly=True)
    name = fields.Char(string="Name", required=True)
    age=fields.Integer(string="Age",required=True)
    date_of_birth = fields.Date(string="Date of Birth")
    gender = fields.Selection(
        [('male', "Male"), ('female', "Female")],
        string="Gender",
        required=True
    )
    contact_number = fields.Char(string='Contact Number')
    address=fields.Text(string="Address")
    medical_history=fields.Text(string="Medical History")
    
    @api.model
    def create(self, vals):
        vals['patient_id'] = self.env['ir.sequence'].next_by_code('hospital.patient') 
        return super(HospitalPatient, self).create(vals) 
