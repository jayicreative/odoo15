# -*- coding: utf-8 -*-
# from odoo import http


# class DemoMod2(http.Controller):
#     @http.route('/demo_mod2/demo_mod2', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/demo_mod2/demo_mod2/objects', auth='public')
#     def list(self, **kw):
#         return http.request.render('demo_mod2.listing', {
#             'root': '/demo_mod2/demo_mod2',
#             'objects': http.request.env['demo_mod2.demo_mod2'].search([]),
#         })

#     @http.route('/demo_mod2/demo_mod2/objects/<model("demo_mod2.demo_mod2"):obj>', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('demo_mod2.object', {
#             'object': obj
#         })
