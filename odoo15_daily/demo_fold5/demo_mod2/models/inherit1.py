#  -*- coding:utf-8 -*-
from odoo import models, fields, api

class inherit(models.Model):
    _inherit = 'sale.order'

    order_details = fields.Char()