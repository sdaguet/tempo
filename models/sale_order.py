# -*- coding: utf-8 -*-
from openerp import api, fields, models, _
from datetime import datetime, timedelta
from openerp import SUPERUSER_ID
import openerp.addons.decimal_precision as dp
from openerp.exceptions import UserError
from openerp.tools import float_is_zero, float_compare, DEFAULT_SERVER_DATETIME_FORMAT

import logging

_logger = logging.getLogger(__name__)


class sale_order(models.Model):
    _inherit = 'sale.order'

    order_type = fields.Selection([
        ('entretien', 'Entretien'),
        ('amenagement', 'Aménagement'),
        ('plantation', 'Plantation'),
        ('sous_traitance', u'Sous-traitance')],
        string='Type', track_visibility='onchange')
    altitude = fields.Float(string='Altitude', digits=(3, 0))
    item_url = fields.Char('View Item')
    n_client = fields.Char(string="N° Client", required=False, related = 'partner_id.N_Client' )
    iframe = fields.Html('Embedded Webpage', compute='_compute_iframe', sanitize=False, strip_style=False)

    @api.multi
    def _compute_iframe(self):  # Cette fonction permet de calculer automatiquement la valeur du champ iframe
            url = self.item_url
            #log ajouté a cette place
			#print "uuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuu"
            _logger.info("_compute_iframe : %r" % url)
            #print url
            template = self.env.ref('darb_puthod.iframe')
            #print "tttttttttttttttttttttttttttttttttttttt"
            _logger.info("_compute_iframe : %r" % template)
            #print template
            self.iframe = template.render({'url': url})
            #print "iffffffffffffffffffffffffff"
            _logger.info("_compute_iframe : %r" % self.iframe)
            #print self.iframe

    @api.multi
    def create_fiche_chantier(self):  # Cette fonction permet de retourner un nouveau enregistrement d'une fiche de chantier  
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
    address = fields.Text(string='Adresse')
    g_lat = fields.Float(string='G Latitude', store=True,
                         multi='glatlng', digits=(3, 12))
    g_lng = fields.Float(string='G Longitude', store=True,
                         multi='glatlng', digits=(3, 12))

    @api.model
    def default_get(self, fields_list):   # Cette fonction permet de retourner la variable models.TransientModel.default_get(self, fields_list)
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
    def create_chantier(self):   # Cette fonction permet de créer un nouveau enregistrement d'un chantier
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

class PuthodIntervention(models.Model):
    _name = 'puthod.intervention'

    order_line_id = fields.Many2one(comodel_name="sale.order.line", string="Source", required=False)
    date_inter = fields.Datetime(string="Date d'intervention", default=fields.Datetime.now, required=False)
    user_inter_id = fields.Many2one(comodel_name="res.users", string="User", default=lambda self: self.env.user, required=False)
    nb_inter = fields.Integer(string="Nombre d'intervention", required=False)
    inter_effectue = fields.Integer(string="Effectuées")
    inter_restant = fields.Integer(string="Restantes")


class PuthodOrderLine(models.Model):
    _inherit = 'sale.order.line'

    inter_effectue = fields.Integer(string="Effectuées")
    inter_restant = fields.Integer(string="Restantes")
    type = fields.Selection(related='product_id.type')
    inter_ids  = fields.One2many(comodel_name="puthod.intervention", inverse_name="order_line_id", string="Interventions", required=False )
    tasks = fields.Boolean(string=u"Peut avoir des tâches")

    @api.multi
    @api.onchange('product_id')
    def product_id_change(self):  # Cette fonction permet de retourner la variable res qui est super(PuthodOrderLine, self).product_id_change() 
        res = super(PuthodOrderLine, self).product_id_change()
        for line in self:
            if line.product_id.tasks:
                line.tasks = True
        return res



