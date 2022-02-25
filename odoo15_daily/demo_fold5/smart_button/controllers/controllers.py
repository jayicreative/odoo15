# -*- coding: utf-8 -*-
# from odoo import http


# class SmartButton(http.Controller):
#     @http.route('/smart_button/smart_button', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/smart_button/smart_button/objects', auth='public')
#     def list(self, **kw):
#         return http.request.render('smart_button.listing', {
#             'root': '/smart_button/smart_button',
#             'objects': http.request.env['smart_button.smart_button'].search([]),
#         })

#     @http.route('/smart_button/smart_button/objects/<model("smart_button.smart_button"):obj>', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('smart_button.object', {
#             'object': obj
#         })
