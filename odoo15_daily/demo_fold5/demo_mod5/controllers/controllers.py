# -*- coding: utf-8 -*-
# from odoo import http


# class DemoMod5(http.Controller):
#     @http.route('/demo_mod5/demo_mod5', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/demo_mod5/demo_mod5/objects', auth='public')
#     def list(self, **kw):
#         return http.request.render('demo_mod5.listing', {
#             'root': '/demo_mod5/demo_mod5',
#             'objects': http.request.env['demo_mod5.demo_mod5'].search([]),
#         })

#     @http.route('/demo_mod5/demo_mod5/objects/<model("demo_mod5.demo_mod5"):obj>', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('demo_mod5.object', {
#             'object': obj
#         })
