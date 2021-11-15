from odoo import models, fields


class ClassInformation(models.Model):
    _name = "class.information"
    _description = "Class Information"

    name = fields.Char(string="Ten lop", required=True)
    grade = fields.Char(string="Khoi", required=True)
    mainTeacher = fields.Char(string="GVCN", required=True)
    schoolID = fields.Many2one("school.information", string="Truong", required=True)
    student_list = fields.One2many("student.information", "class_id", string="Danh sach hoc sinh")
