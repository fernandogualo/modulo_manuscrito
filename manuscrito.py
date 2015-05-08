# -*- coding: utf-8 -*-
from openerp.osv import fields, orm
import datetime

class manuscrito(orm.Model):
	_name = 'res.manuscrito'
	_description = 'Manuscrito'
	_columns = {
		'autor': fields.many2one('res.partner', 'Autor', track_visibility='onchange',required=True, select=True),domain="[('author','=',True)]"),
		'partner_id': fields.many2one('res.partner', 'Partner', ondelete='set null', track_visibility='onchange',
            select=True, help="Linked partner (optional). Usually created when converting the lead."),

		'titulo': fields.char('Título', size=50, required=True),
		'isbn':fields.char('ISBN', size=30, required=True),
		'formato':fields.char('Formato', size=30),
		'genero':fields.selection([('ciencia-ficcion','Ciencia-Ficcion'),('novela','Novela'),('poesia','Poesía'),('cuento','Cuento'),('historia','Historia'),('miedo','Miedo'),('otro','Otros')],'Género', required=True),
		'email':fields.char('E-MAIL',size=20),
		'comment': fields.text('Descripción'),
		'image': fields.binary("Image", help="Select image here"),
		'date': fields.date('Date', select=1),
		'idioma':fields.selection([('cas','Castellano'),('en','Inglés'),('fr','Francés')],'Idioma'),
		'state': fields.selection([('recibo', 'Acuse recibo'),('eval', 'Evaluación'),('confirmacion','Pendiente confirmación'),('cancelled', 'Cancelado'),('firma', 'Firma Contrato'),('corregir', 'Corrección'),('reenvio', 'Visto bueno autor'),('envio imprenta', 'Enviado a imprenta'), ('done', 'Hecho')]),
	}
	def set_recibo(self, cr, uid, ids, context=None):
		return self.write(cr, uid, ids, {'state': 'eval'}, context=context)
	def set_evaluar(self, cr, uid, ids, context=None):
		return self.write(cr, uid, ids, {'state': 'confirmacion'}, context=context)
	def set_aceptar(self, cr, uid, ids, context=None):
		return self.write(cr, uid, ids, {'state': 'firma'}, context=context)
	def set_firmar(self, cr, uid, ids, context=None):
		return self.write(cr, uid, ids, {'state': 'corregir'}, context=context)
	def set_corregir(self, cr, uid, ids, context=None):
		return self.write(cr, uid, ids, {'state': 'reenvio'}, context=context)
	def set_visto(self, cr, uid, ids, context=None):
		return self.write(cr, uid, ids, {'state': 'done'}, context=context)
	def set_imprenta(self, cr, uid, ids, context=None):
		return self.write(cr, uid, ids, {'state': 'envio imprenta'}, context=context)
	_defaults = {
        'state': 'recibo',
        #'genero': 'novela',
		#'idioma': 'cas',
    }

		
class author(orm.Model):
	_name= 'res.partner'
	_inherit = 'res.partner'
	_columns = {
		'author':fields.boolean('Autor'),
	}

