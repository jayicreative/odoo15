# -*- coding: utf-8 -*-

from odoo import models, fields, api


class wiz5(models.Model):
    _name = 'wiz5.wiz5'
    # _description = 'wiz'

    name = fields.Char()
    value = fields.Integer()
    value2 = fields.Float(compute="_value_pc", store=True)
    description = fields.Text()

    @api.depends('value')
    def _value_pc(self):
        for record in self:
            record.value2 = float(record.value) / 100

    def check5(self):
        print("jay5")