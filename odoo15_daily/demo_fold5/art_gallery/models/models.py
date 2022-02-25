# -*- coding: utf-8 -*-

from odoo import models, fields, api


class art_gallery(models.Model):
    _name = 'art_gallery.art_gallery'
    _description = 'art_gallery.art_gallery'

    name = fields.Char()
    value = fields.Integer()
    value2 = fields.Float(compute="_value_pc", store=True)
    description = fields.Text()

    @api.depends('value')
    def _value_pc(self):
        for record in self:
            record.value2 = float(record.value) / 100
