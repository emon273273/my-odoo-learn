from odoo import api, fields, models


class HospitalDoctor(models.Model):
    _name = 'account.move'
    _description = 'hospital.invoice'
    _inherit = 'account.move'

    appointment_id = fields.Many2one("hospital.appointment", string="Appointment")