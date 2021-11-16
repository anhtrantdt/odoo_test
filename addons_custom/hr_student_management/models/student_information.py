from odoo import models, fields


class StudentInformation(models.Model):
    _name = "student.information"
    _description = "Student Information"

    name = fields.Char(string="Ho va ten", required=True)
    dateOfBirth = fields.Date(string="Ngay sinh", required=True)
    class_id = fields.Many2one("class.information", string="Lop", required=True)
    subject_list = fields.Many2many("subject.information", "relation_student_subject", "student_id", "subject_id", string="Mon hoc dang ky")
    # mainTeacher = fields.Char(string="GVCN", related="class_id.mainTeacher")
