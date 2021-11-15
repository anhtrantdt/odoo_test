from odoo import models, fields


class SubjectInformation(models.Model):
    _name = "subject.information"
    _description = "Subject Information"

    name = fields.Char(string="Ten mon hoc")
    unit = fields.Integer(string="So tiet hoc")
