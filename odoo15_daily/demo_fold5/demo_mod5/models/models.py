# -*- coding: utf-8 -*-

from odoo import models, fields, api


class demo_mod5(models.Model):
    _name = 'demo_mod5.demo_mod5'
    _description = 'demo_mod5.demo_mod5'

    name = fields.Char()
    value = fields.Integer()
    value2 = fields.Float(compute="_value_pc", store=True)
    description = fields.Text()
    image = fields.Binary()

    phone_no = fields.Char()
    select = fields.Selection([("one","like"),("two","comment"),("three","share")])

class demo_mod6(models.Model):
    _inherit = 'demo_mod5.demo_mod5'

    gender = fields.Char()
    @api.depends('value')
    def _value_pc(self):
        for record in self:
            record.value2 = float(record.value) / 100
