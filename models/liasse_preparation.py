# -*- coding: utf-8 -*-
from openerp import api, fields, models

import logging
_logger = logging.getLogger(__name__)


class liasse_preparation(models.Model):
    _name = 'liasse.preparation'

    name = fields.Char('Nom')
    date = fields.Date('Date')
    partner_id = fields.Many2one('res.partner', string='Client')
    lines = fields.One2many('liasse.preparation.line', 'liasse_id', string="Lines")
    chantier_id = fields.Many2one('chantier', string='Chantier', index=True, track_visibility='onchange')
    partner_invoice_id = fields.Many2one('res.partner', string='Adresse de Facturation')
    partner_shipping_id = fields.Many2one('res.partner', string='Adresse de livraison')


    @api.multi
    @api.onchange('partner_id')
    def onchange_partner_id(self):
        """
        Update the following fields when the partner is changed:
        - Invoice address
        - Delivery address
        """
        if not self.partner_id:
            self.update({
                'partner_invoice_id': False,
                'partner_shipping_id': False,
            })
            return

        addr = self.partner_id.address_get(['delivery', 'invoice'])
        values = {
            'partner_invoice_id': addr['invoice'],
            'partner_shipping_id': addr['delivery'],
        }
        self.update(values)

    @api.one
    def getallemplacementgroups(self):
        datas = {}
        res = []
        for obj in self.lines.search([('liasse_id','=', self.id)]):
            key = obj.emplacement_id
            if key in datas:
                datas[key].append(obj)
            else:
                datas[key] = [obj]
        res.append(datas)
        return datas


class liasse_preparation_line(models.Model):
    _name = 'liasse.preparation.line'

    emplacement_id = fields.Many2one('emplacement', string='Emplacement', index=True, track_visibility='onchange')
    product_id = fields.Many2one('product.product', string=u'Désignation')
    qty = fields.Char('Quantité')
    nbr_etiq = fields.Char('Nbre Etiq')
    liasse_id = fields.Many2one('liasse.preparation', string=u'Liasse de préparation')

    @api.onchange('emplacement_id')
    def _onchange_emplacement_id(self):
        return {'domain': {
            'product_id': [('id', 'in', self.emplacement_id.product_ids.ids)],
        }}
