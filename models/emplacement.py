# -*- coding: utf-8 -*-
from openerp import api, fields, models

import logging
_logger = logging.getLogger(__name__)


class emplacement(models.Model):
    _name = 'emplacement'

    name = fields.Char('Nom')
    chantier_id = fields.Many2one('chantier', string='Chantier', index=True, track_visibility='onchange')
    longueur = fields.Char('Longueur')
    densite = fields.Char('Densité')
    product_ids = fields.Many2many('product.product', string="Produits")


class product_emplacement(models.Model):
    _name = 'product.emplacement'

    product_id = fields.Many2one('product.product', string='Produit', index=True, track_visibility='onchange')
    emplacement_id = fields.Many2one('emplacement', string='Emplacement', index=True, track_visibility='onchange')
    name = fields.Char('Nom', related='product_id.name')
