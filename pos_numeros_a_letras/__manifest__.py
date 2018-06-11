# -*- coding: utf-8 -*-
{
    'name': "pos_numeros_a_letras",
    'summary': """
        Imprime el monto del recibo del POS en letras""",
    'description': """
        Imprime el monto del recibo del POS en letras, en conformidad con los requerimientos de la Servicio de Administración de Rentas de Honduras.
    """,
    'author': "Fermin Arellano",
    'website': "http://www.github.com/ferminarellano",
    'category': 'Point of Sale',
    'version': '10.0.1',
    'depends': ['point_of_sale'],
    'data': [
		'data.xml'
    ],
	'qweb':['static/src/xml/custom.xml'],
	'demo': []
}