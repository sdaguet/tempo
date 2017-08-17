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
    compute_famille = fields.Char(string="_compute_famille", compute='_compute_famille')
    marque_savoie = fields.Boolean(string="Marque Savoie",  )
    libelle_commercial = fields.Char("Libellé commercial")
    name_puthod = fields.Char(string="Nom complet", required=False)

    @api.multi
    @api.depends('famille')
    def _compute_famille(self):

        famille = self.famille

        if famille == 'eng':
            xml_record_eng = self.env.ref("darb_puthod.product_category_engrais")
            self.write({'categ_id':xml_record_eng.id,'type':'consu'})

        elif famille == 'F':
            xml_record_F = self.env.ref("darb_puthod.product_category_fourniture")
            self.write({'categ_id':xml_record_F.id,'type':'consu'})

        elif famille == 'OP-SPE':
            xml_record_OP_SPE = self.env.ref("darb_puthod.product_category_divers")
            self.write({'categ_id':xml_record_OP_SPE.id,'type':'service'})
            #type a definir

        elif famille == 'TRA':
            xml_record_TRA = self.env.ref("darb_puthod.product_category_vehicle")
            self.write({'categ_id':xml_record_TRA.id,'type':'service'})

        elif famille == 'Z':
            xml_record_Z = self.env.ref("darb_puthod.product_category_prestations")
            self.write({'categ_id':xml_record_Z.id,'type':'service'})

        else:
            xml_record_vigitaux = self.env.ref("darb_puthod.product_category_vigitaux")
            self.write({'categ_id':xml_record_vigitaux.id,'type':'product'})




    # def create_variant_ids(self, cr, uid, ids, context=None):
    #     _logger.info("------------> Article create_variant_ids iciiiiiiiiiiiiiiiiiiiiiiii : " + str(ids))
    #     return super(PuthodTemplate, self).create_variant_ids(self, cr, uid, ids, context=context)
