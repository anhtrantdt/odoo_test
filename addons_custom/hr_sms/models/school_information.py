from odoo import models, fields


class SchoolInformation(models.Model):
    _name = "school.information"
    _description = "School Information"

    name = fields.Char(string='Ten truong')
    type = fields.Selection([('Public', 'Cong lap'), ('Private', 'Dan lap')], default='Public', string="Loai truong")
    email = fields.Text(string="Email")
    address = fields.Text(string="Dia chi")

    phoneNo = fields.Char(string="So dien thoai")
    hasOnlineClass = fields.Boolean(string="Co lop hoc online")
    rank = fields.Integer(string="Xep hang")
    establishDay = fields.Date(string="Ngay thanh lap")
    document = fields.Binary(string="Tai lieu ve truong")
    document_name = fields.Char(string="Ten tai lieu")

    class_list = fields.One2many("class.information", "schoolID", string="Danh sach lop hoc")
