# -*- coding: utf-8 -*-

from odoo import models, fields, api


class smart_button(models.Model):
    _name = 'smart_button.smart_button'
    _description = 'smart_button.smart_button'

    name = fields.Char()
    value = fields.Integer()
    value2 = fields.Float(compute="_value_pc", store=True)
    description = fields.Text()

    @api.depends('value')
    def _value_pc(self):
        for record in self:
            record.value2 = float(record.value) / 100
    def push_smart(self):
        print("jay")
