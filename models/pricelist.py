# -*- coding: utf-8 -*-
from openerp import api, fields, models

import logging
_logger = logging.getLogger(__name__)


class product_pricelist(models.Model):
    _inherit = 'product.pricelist'

    applied_on = fields.Selection([('partner', 'Client'), ('type_partner', 'Type Client')], string="Appliquer sur")
    partner_id = fields.Many2one('res.partner', string='Client')
    type_client = fields.Selection(string="Type de client", selection=[('FR', 'clt fruitiers'), ('PF', 'clt plt forestier'), ('PO', 'clt pltes ornementales'), ('PP', 'clt puthod paysage')])

    @api.onchange('applied_on') # if these fields are changed, call method
    def _check_change(self):
        self.partner_id = False
        self.type_client = False

    @api.model
    def create(self, vals):
        res = super(product_pricelist, self).create(vals)
        if res.applied_on == 'partner':
            res.partner_id.property_product_pricelist = res.id
        elif res.applied_on == 'type_partner':
            partners = self.env['res.partner'].search([('type_client', '=', res.type_client)])
            for partner in partners:
                partner.property_product_pricelist = res.id
        return res

    @api.multi
    def write(self, vals):
        res = super(product_pricelist, self).write(vals)
        if 'partner_id' in vals.keys() or 'type_client' in vals.keys():
            if self.applied_on == 'partner':
                self.partner_id.property_product_pricelist = self.id
            elif self.applied_on == 'type_partner':
                partners = self.env['res.partner'].search([('type_client', '=', self.type_client)])
                for partner in partners:
                    partner.property_product_pricelist = self.id
        return res
