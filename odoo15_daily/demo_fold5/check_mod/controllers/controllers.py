# -*- coding: utf-8 -*-
# from odoo import http


# class CheckMod(http.Controller):
#     @http.route('/check_mod/check_mod', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/check_mod/check_mod/objects', auth='public')
#     def list(self, **kw):
#         return http.request.render('check_mod.listing', {
#             'root': '/check_mod/check_mod',
#             'objects': http.request.env['check_mod.check_mod'].search([]),
#         })

#     @http.route('/check_mod/check_mod/objects/<model("check_mod.check_mod"):obj>', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('check_mod.object', {
#             'object': obj
#         })
