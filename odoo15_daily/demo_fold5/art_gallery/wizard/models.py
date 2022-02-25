# -*- coding: utf-8 -*-

from odoo import models, fields, api


class art5(models.Model):
    _name = 'art5.art5'
    # _description = 'art5'

    name = fields.Char()
    age = fields.Integer()
    gender = fields.Selection([('1','male'),('2','female'),('3','other')])
    description = fields.Text()

    @api.depends('value')
    def _value_pc(self):
        for record in self:
            record.value2 = float(record.value) / 100

    def art5(self):
        print("your wizard run sucesfully")