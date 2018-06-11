# -*- coding: utf-8 -*-
from odoo import http

# class PosNumerosALetras(http.Controller):
#     @http.route('/pos_numeros_a_letras/pos_numeros_a_letras/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/pos_numeros_a_letras/pos_numeros_a_letras/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('pos_numeros_a_letras.listing', {
#             'root': '/pos_numeros_a_letras/pos_numeros_a_letras',
#             'objects': http.request.env['pos_numeros_a_letras.pos_numeros_a_letras'].search([]),
#         })

#     @http.route('/pos_numeros_a_letras/pos_numeros_a_letras/objects/<model("pos_numeros_a_letras.pos_numeros_a_letras"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('pos_numeros_a_letras.object', {
#             'object': obj
#         })