from odoo import api, fields, models

class HospitalPatient(models.Model):
    _name = "hospital.doctor"
    _description = "This is just for testing purposes"

    name = fields.Char(string="Name", required=True)
    date_of_birth = fields.Date(string="Date of Birth")
    gender = fields.Selection(
        [('male', "Male"), ('female', "Female")],
        string="Gender",
        required=False
    )
    city = fields.Char(string="City")
    state = fields.Char(string="State")
    country = fields.Char(string="Country")
