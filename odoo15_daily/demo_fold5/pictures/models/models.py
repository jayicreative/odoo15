# -*- coding: utf-8 -*-

from odoo import models, fields, api


class pictures(models.Model):
    _name = 'pictures.pictures'
    _description = 'pictures.pictures'

    description = fields.Text()
    image1 = fields.Binary()
    image2 = fields.Binary()
    image3 = fields.Binary()
    image4 = fields.Binary()


    @api.depends('value')
    def _value_pc(self):
        for record in self:
            record.value2 = float(record.value) / 100
