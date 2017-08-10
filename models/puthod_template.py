#!/usr/bin/python
# coding: utf8
from openerp import fields, models, api, _
from openerp.exceptions import ValidationError
from datetime import datetime


class PuthodTemplate(models.Model):
    _inherit = 'product.template'
    N_Article = fields.Char(string='N° Article')
    importe = fields.Boolean(string="importe",default = False)
    famille = fields.Selection(string="Famille", selection=[('0', 'FERTIL-POTS'), ('1', 'PLTS FORESTIRS'),('2', 'HAIES'), ('3', 'PLTAPISSANTES'),('4', 'CONIFERES'), ('5', 'ARB.FRUITIERS'),('6', 'SAPINS DE NOEL'), ('7', 'ARBUSTES'),('8', 'ARB.FEUILLUS'), ('9', 'SAPINS DE NOEL'),('ARB', 'ARBUSTES'), ('eng', 'engrais'),('F', 'FOURNITURES-AIDE PLANTATION'), ('JAR', 'J.PLARBUSTES'),('OP-SPE', 'OPERATIONS SPECIALES'), ('TOP', 'topiaire'),('TRA', 'Transport'), ('VIV', 'vivaces'),('Z', 'PRESTATIONS'), ], required=False, )
    marque_savoie = fields.Boolean(string="Marque Savoie",  )
    libelle_commercial = fields.Char("Libellé commercial")
