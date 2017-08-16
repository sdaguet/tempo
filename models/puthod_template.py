#!/usr/bin/python
# coding: utf8
from openerp import fields, models, api, _
import logging
import time
_logger = logging.getLogger(__name__)



class PuthodTemplate(models.Model):
    _inherit = 'product.template'
    N_Article = fields.Char(string='N° Article')
    importe = fields.Boolean(string="importe",default = False)
    famille = fields.Selection(string="Famille", selection=[('0', 'FERTIL-POTS'), ('1', 'PLTS FORESTIRS'),('2', 'HAIES'), ('3', 'PLTAPISSANTES'),('4', 'CONIFERES'), ('5', 'ARB.FRUITIERS'),('6', 'SAPINS DE NOEL'), ('7', 'ARBUSTES'),('8', 'ARB.FEUILLUS'), ('9', 'SAPINS DE NOEL'),('ARB', 'ARBUSTES'), ('eng', 'engrais'),('F', 'FOURNITURES-AIDE PLANTATION'), ('JAR', 'J.PLARBUSTES'),('OP-SPE', 'OPERATIONS SPECIALES'), ('TOP', 'topiaire'),('TRA', 'Transport'), ('VIV', 'vivaces'),('Z', 'PRESTATIONS'), ], required=False, )
    marque_savoie = fields.Boolean(string="Marque Savoie",  )
    libelle_commercial = fields.Char("Libellé commercial")
    name_puthod = fields.Char(string="Nom complet", required=False)



    # def create_variant_ids(self, cr, uid, ids, context=None):
    #     _logger.info("------------> Article create_variant_ids iciiiiiiiiiiiiiiiiiiiiiiii : " + str(ids))
    #     return super(PuthodTemplate, self).create_variant_ids(self, cr, uid, ids, context=context)
