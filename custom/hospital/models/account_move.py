from odoo import api, fields, models


class AccountMove(models.Model):
    _inherit='account.move'
    appointment_id=fields.Many2one('hospital.appointment',string="Appoinment")
    patient_id=fields.Many2one('hospital.patient',string="Patient")
