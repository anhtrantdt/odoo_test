from odoo import models, fields, api
import re


class ClassInformation(models.Model):
    _name = "class.information"
    _description = "Class Information"

    name = fields.Char(string="Ten lop", required=True)
    grade = fields.Char(string="Khoi", compute="_compute_grade")
    mainTeacher = fields.Char(string="GVCN", required=True)
    schoolID = fields.Many2one("school.information", string="Truong", required=True)
    student_list = fields.One2many("student.information", "class_id", string="Danh sach hoc sinh")
    # address = fields.Text(string="Dia chi", related="schoolID.address")

    @api.depends("name")
    def _compute_grade(self):
        for record in self:
            if record.name:
                record.grade = re.split('[a-zA-Z]', record.name, 1)[0]
