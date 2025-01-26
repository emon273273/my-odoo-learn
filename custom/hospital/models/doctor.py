from odoo import models, fields, api

class HospitalDoctor(models.Model):
    _name = 'hospital.doctor'
    _description = 'Doctor'

    name = fields.Char(string='Doctor Name', required=True)
    doctor_id = fields.Char(string="Doctor Id", readonly=True)
    specialization = fields.Selection([
        ('cardiology', 'Cardiology'),
        ('neurology', 'Neurology'),
        ('orthopedics', 'Orthopedics'),
        ('pediatrics', 'Pediatrics'),
        ('general', 'General Medicine'),
        
    ], string='Specialization', required=True)
    phone = fields.Char(string='Phone')
    email = fields.Char(string='Email')
    gender = fields.Selection([('male', 'Male'), ('female', 'Female')], string='Gender')
    state = fields.Selection([('active', 'Active'), ('inactive', 'Inactive')], string='Status', default='active')

    @api.model
    def create(self, vals):
        
        if not vals.get('doctor_id'):
            vals['doctor_id'] = self.env['ir.sequence'].next_by_code('hospital.doctor')
        return super(HospitalDoctor, self).create(vals)
