# -*- coding: utf-8 -*-
# from odoo import http


# class Pictures(http.Controller):
#     @http.route('/pictures/pictures', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/pictures/pictures/objects', auth='public')
#     def list(self, **kw):
#         return http.request.render('pictures.listing', {
#             'root': '/pictures/pictures',
#             'objects': http.request.env['pictures.pictures'].search([]),
#         })

#     @http.route('/pictures/pictures/objects/<model("pictures.pictures"):obj>', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('pictures.object', {
#             'object': obj
#         })
