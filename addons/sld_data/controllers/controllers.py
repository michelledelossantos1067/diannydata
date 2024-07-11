# -*- coding: utf-8 -*-
# from odoo import http


# class SldData(http.Controller):
#     @http.route('/sld_data/sld_data', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/sld_data/sld_data/objects', auth='public')
#     def list(self, **kw):
#         return http.request.render('sld_data.listing', {
#             'root': '/sld_data/sld_data',
#             'objects': http.request.env['sld_data.sld_data'].search([]),
#         })

#     @http.route('/sld_data/sld_data/objects/<model("sld_data.sld_data"):obj>', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('sld_data.object', {
#             'object': obj
#         })
