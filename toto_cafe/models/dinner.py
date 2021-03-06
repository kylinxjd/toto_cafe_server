# _*_ coding: utf-8 _*_
from odoo import models, fields, api


class TotoCafeDinner(models.Model):
    _name = "toto_cafe.dinner"

    type = fields.Selection([
        ("a", "A"),
        ("b", "B"),
    ], required=True, string="Type")
    date = fields.Date(default=fields.Date.today)
    quantity = fields.Integer(default=400)
    image = fields.Image()
    record_ids = fields.One2many("toto_cafe.dinner.record", "dinner_id", string="记录", readonly=True)
    remain = fields.Integer(compute="_compute_remain", store=True, string="剩余餐数")

    @api.depends("record_ids")
    def _compute_remain(self):
        for dinner in self:
            dinner.remain = dinner.quantity - len(dinner.record_ids)

class TotoCafeDinnerRecord(models.Model):
    _name = "toto_cafe.dinner.record"

    dinner_id = fields.Many2one("toto_cafe.dinner", ondelete="cascade")
    department = fields.Char("部")
    section = fields.Char(string="课")
    name = fields.Char(string="姓名")
    no = fields.Char(string="工号")
