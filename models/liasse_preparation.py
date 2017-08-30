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
    fiche_chantier_id = fields.Many2one('fiche.chantier', string='Fiche Chantier', index=True, track_visibility='onchange')
    partner_invoice_id = fields.Many2one('res.partner', string='Adresse de Facturation')
    partner_shipping_id = fields.Many2one('res.partner', string='Adresse de livraison')
    state = fields.Selection([
        ('draft', 'Brouillon'),
        ('done', 'Validé'), ('cancel', 'Annulé')], default='draft', copy=False,
        string='Status', readonly=True, track_visibility='onchange')

    @api.multi
    def action_confirm(self):
        # Cette fonction modifie le champ state à l'etat done
        for line in self.lines:
            if line.product_id.categ_id.id == self.env.ref('darb_puthod.product_category_vehicle').id:
                self.fiche_chantier_id.veicule_ids = [(0, 0, {
                        'veicule_id': line.product_id.id,
                        'kms': line.qty,
                        })]
            elif line.product_id.categ_id.id == self.env.ref('darb_puthod.product_category_materiel').id:
                self.fiche_chantier_id.materiel_ids = [(0, 0, {
                        'materiel_id': line.product_id.id,
                        'temps': line.qty,
                        })]
            elif line.product_id.categ_id.id == self.env.ref('darb_puthod.product_category_machine').id:
                self.fiche_chantier_id.machine_ids = [(0, 0, {
                        'machine_id': line.product_id.id,
                        'temps': line.qty,
                        })]
            elif line.product_id.categ_id.id == self.env.ref('darb_puthod.product_category_fourniture').id:
                self.fiche_chantier_id.fourniture_ids = [(0, 0, {
                        'fourniture_id': line.product_id.id,
                        'quantity': line.qty,
                        })]
            elif line.product_id.categ_id.id == self.env.ref('darb_puthod.product_category_kit').id:
                self.fiche_chantier_id.kit_ids = [(0, 0, {
                        'kit_id': line.product_id.id,
                        'quantity': line.qty,
                        })]
            elif line.product_id.categ_id.id == self.env.ref('darb_puthod.product_category_tuteurage').id:
                self.fiche_chantier_id.tuteurage_ids = [(0, 0, {
                        'tuteurage_id': line.product_id.id,
                        'quantity': line.qty,
                        })]
            elif line.product_id.categ_id.id == self.env.ref('darb_puthod.product_category_gazons').id:
                self.fiche_chantier_id.gazons_ids = [(0, 0, {
                        'gazons_id': line.product_id.id,
                        'quantity': line.qty,
                        })]
            elif line.product_id.categ_id.id == self.env.ref('darb_puthod.product_category_engrais').id:
                self.fiche_chantier_id.engrais_ids = [(0, 0, {
                        'engrais_id': line.product_id.id,
                        'quantity': line.qty,
                        })]
            elif line.product_id.categ_id.id == self.env.ref('darb_puthod.product_category_gmateriel').id:
                self.fiche_chantier_id.gmateriel_ids = [(0, 0, {
                        'gmateriel_id': line.product_id.id,
                        'quantity': line.qty,
                        })]
            elif line.product_id.categ_id.id == self.env.ref('darb_puthod.product_category_escalier').id:
                self.fiche_chantier_id.escalier_ids = [(0, 0, {
                        'escalier_id': line.product_id.id,
                        'quantity': line.qty,
                        })]
            elif line.product_id.categ_id.id == self.env.ref('darb_puthod.product_category_outils').id:
                self.fiche_chantier_id.outils_ids = [(0, 0, {
                        'outils_id': line.product_id.id,
                        'quantity': line.qty,
                        })]
            elif line.product_id.categ_id.id == self.env.ref('darb_puthod.product_category_cloture').id:
                self.fiche_chantier_id.cloture_ids = [(0, 0, {
                        'cloture_id': line.product_id.id,
                        'quantity': line.qty,
                        })]
            elif line.product_id.categ_id.id == self.env.ref('darb_puthod.product_category_divers').id:
                self.fiche_chantier_id.divers_ids = [(0, 0, {
                        'divers_id': line.product_id.id,
                        'quantity': line.qty,
                        })]
            elif line.product_id.categ_id.id == self.env.ref('darb_puthod.product_category_terrasse').id:
                self.fiche_chantier_id.terrasse_ids = [(0, 0, {
                        'terrasse_id': line.product_id.id,
                        'quantity': line.qty,
                        })]
            elif line.product_id.categ_id.id == self.env.ref('darb_puthod.product_category_vigitaux').id:
                for i in range(line.qty):
                    self.fiche_chantier_id.vigitaux_ids = [(0, 0, {
                            'vigitaux_id': line.product_id.id,
                            })]
        res = self.write({'state': 'done'})
        return res

    @api.multi
    def button_cancel(self):
        # Cette fonction modifie le champ state à l'etat cancel
        res = self.write({'state': 'cancel'})
        return res

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
    qty = fields.Integer('Quantité')
    nbr_etiq = fields.Integer('Nbre Etiq')
    liasse_id = fields.Many2one('liasse.preparation', string=u'Liasse de préparation')

    @api.onchange('emplacement_id')
    def _onchange_emplacement_id(self):
        return {'domain': {
            'product_id': [('id', 'in', self.emplacement_id.product_ids.ids)],
        }}
