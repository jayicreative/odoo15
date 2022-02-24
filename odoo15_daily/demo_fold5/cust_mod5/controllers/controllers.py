# -*- coding: utf-8 -*-
# from odoo import http


# class CustMod5(http.Controller):
#     @http.route('/cust_mod5/cust_mod5', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/cust_mod5/cust_mod5/objects', auth='public')
#     def list(self, **kw):
#         return http.request.render('cust_mod5.listing', {
#             'root': '/cust_mod5/cust_mod5',
#             'objects': http.request.env['cust_mod5.cust_mod5'].search([]),
#         })

#     @http.route('/cust_mod5/cust_mod5/objects/<model("cust_mod5.cust_mod5"):obj>', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('cust_mod5.object', {
#             'object': obj
#         })
