from datetime import datetime

from odoo import api, fields, models


class HospitalAppointment(models.Model):
    _name = 'hospital.appointment'
    _description = 'Appointment'
    appoinment_id = fields.Char(string='Appointment ID',readonly=True) 
    patient_id = fields.Many2one('hospital.patient', string='Patient', required=True)
    # doctor_id = fields.Many2one('res.users', string='Doctor', required=True)
    appointment_date = fields.Datetime(string='Appointment Date', required=True, default=fields.Datetime.now)
    reason = fields.Text(string='Reason for Appointment')
    state = fields.Selection([
        ('draft', 'Draft'),
        ('confirmed', 'Confirmed'),
        ('done', 'Done'),
        ('cancelled', 'Cancelled'),
    ], string='Status', default='draft')

    @api.model
    def create(self, vals):
        vals['appoinment_id'] = self.env['ir.sequence'].next_by_code('hospital.appointment') 
        return super(HospitalAppointment, self).create(vals) 

