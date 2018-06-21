# -*- coding: utf-8 -*-
from odoo import http

# class /odoo/custom/addons/posProformaPlantilla(http.Controller):
#     @http.route('//odoo/custom/addons/pos_proforma_plantilla//odoo/custom/addons/pos_proforma_plantilla/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('//odoo/custom/addons/pos_proforma_plantilla//odoo/custom/addons/pos_proforma_plantilla/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('/odoo/custom/addons/pos_proforma_plantilla.listing', {
#             'root': '//odoo/custom/addons/pos_proforma_plantilla//odoo/custom/addons/pos_proforma_plantilla',
#             'objects': http.request.env['/odoo/custom/addons/pos_proforma_plantilla./odoo/custom/addons/pos_proforma_plantilla'].search([]),
#         })

#     @http.route('//odoo/custom/addons/pos_proforma_plantilla//odoo/custom/addons/pos_proforma_plantilla/objects/<model("/odoo/custom/addons/pos_proforma_plantilla./odoo/custom/addons/pos_proforma_plantilla"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('/odoo/custom/addons/pos_proforma_plantilla.object', {
#             'object': obj
#         })