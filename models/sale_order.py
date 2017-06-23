# -*- coding: utf-8 -*-
from openerp import api, fields, models

import logging

_logger = logging.getLogger(__name__)


class sale_order(models.Model):
    _inherit = 'sale.order'

    order_type = fields.Selection([
        ('entretien', 'Entretien'),
        ('type2', 'Type2'),
        ('type3', 'Type3')],
        string='Type', track_visibility='onchange')
    altitude = fields.Float(string='Altitude', digits=(3, 12))

    @api.multi
    def create_fiche_chantier(self):
        return {
            'name': 'Chantier',
            'view_type': 'form',
            'view_mode': 'form',
            'res_model': 'wizard.create.chantiere',
            'view_id': False,
            'target': 'new',
            'type': 'ir.actions.act_window',
        }


class wizard_create_chantier(models.TransientModel):
    _name = 'wizard.create.chantiere'

    name = fields.Char('Nom')
    address = fields.Text(string='Address')
    g_lat = fields.Float(string='G Latitude', store=True,
                         multi='glatlng', digits=(3, 12))
    g_lng = fields.Float(string='G Longitude', store=True,
                         multi='glatlng', digits=(3, 12))

    @api.model
    def default_get(self, fields_list):
        res = models.TransientModel.default_get(self, fields_list)
        context = dict(self._context or {})
        active_ids = context.get('active_ids', []) or []
        related_order = self.env['sale.order'].browse(active_ids)
        address = []
        partner = related_order.partner_shipping_id
        if partner.street:
            address.append(partner.street)
        if partner.street2:
            address.append(partner.street2)
        if partner.city:
            address.append(partner.city)
        if partner.state_id:
            address.append(partner.state_id.name)
        if partner.country_id:
            address.append(partner.country_id.name)
        if partner.zip:
            address.append(partner.zip)

        address = ', '.join(address)
        res['address'] = address
        return res

    @api.multi
    def create_chantier(self):
        """ ...
        """
        context = dict(self._context or {})
        active_ids = context.get('active_ids', []) or []
        related_order = self.env['sale.order'].browse(active_ids)
        vals = {'name': self.name, 'address': self.address, 'g_lat': self.g_lat, 'g_lng': self.g_lng,
                'order_id': related_order.id}
        chantier_id = self.env['chantier'].create(vals)
        return {
            'name': 'Chantier',
            'view_type': 'form',
            'view_mode': 'form',
            'res_model': 'chantier',
            'res_id': chantier_id.id,
            'view_id': False,
            'target': 'current_edit',
            'type': 'ir.actions.act_window',
        }
