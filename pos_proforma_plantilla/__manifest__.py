# -*- coding: utf-8 -*-
{
    'name': "pos_proforma_plantilla",
    'summary': """
        Modifica la proforma, para que no sea identica a la factura.""",
    'description': """
        Modifica la proforma, para que no sea identica a la factura. Lo que eliminaria confusiones al confundir una proforma con una factura.
    """,
    'author': "Fermin Arellano",
    'website': "http://www.github.com/ferminarellano",
    'category': 'Point of Sale',
    'version': '10.0.0.1',
    'depends': ['pos_restaurant','point_of_sale'],
    'data': ['data.xml'],
    'demo': [],
	'qweb':['static/src/xml/custom.xml'],
}