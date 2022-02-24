# -*- coding: utf-8 -*-

from odoo import models, fields, api


class demo_mod2(models.Model):
    _name = 'demo_mod2.demo_mod2'
    _description = 'demo_mod2.demo_mod2'

    name = fields.Char()
    value = fields.Integer()
    value2 = fields.Float(compute="_value_pc", store=True)
    description = fields.Text()

class inherit_mod(models.Model):
    _inherit = 'demo_mod2.demo_mod2'

    gender = fields.Char()
    @api.depends('value')
    def _value_pc(self):
        for record in self:
            record.value2 = float(record.value) / 100
