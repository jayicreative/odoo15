# -*- coding: utf-8 -*-

from odoo import models, fields, api


class customers(models.Model):
    _name = 'customers.customers'
    _description = 'customers.customers'

    name = fields.Char()
    value = fields.Integer()
    value2 = fields.Float(compute="_value_pc", store=True)
    description = fields.Text()

    @api.depends('value')
    def _value_pc(self):
        for record in self:
            record.value2 = float(record.value) / 100
    def show_customers(self):
        print("your smart button has been set succesfully")