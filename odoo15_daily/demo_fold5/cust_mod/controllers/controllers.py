# -*- coding: utf-8 -*-
# from odoo import http


# class CustMod(http.Controller):
#     @http.route('/cust_mod/cust_mod', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/cust_mod/cust_mod/objects', auth='public')
#     def list(self, **kw):
#         return http.request.render('cust_mod.listing', {
#             'root': '/cust_mod/cust_mod',
#             'objects': http.request.env['cust_mod.cust_mod'].search([]),
#         })

#     @http.route('/cust_mod/cust_mod/objects/<model("cust_mod.cust_mod"):obj>', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('cust_mod.object', {
#             'object': obj
#         })
