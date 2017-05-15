# -*- coding: utf-8 -*-
from openerp import fields, models, api, _
# from openerp.exceptions import ValidationError
# from dateutil.relativedelta import relativedelta
# from openerp.tools import DEFAULT_SERVER_DATE_FORMAT, DEFAULT_SERVER_DATETIME_FORMAT
import geocoder
import logging
_logger = logging.getLogger(__name__)

class mrp_production(models.Model):
    _inherit = "mrp.production"
    _description = 'Fiche de Chantier'
    status_interv = fields.Selection([
        ('brouillon', u'A remplir'),
        ('rempli', u'Rempli. A valider'),
        ('valide', u'Validé. A comptabiliser'),
        ('comptabilise', u'Comptabilisé')], default='brouillon',
        string='Status FC', readonly=True, track_visibility='onchange')

    inter_date = fields.Datetime(string="Date d'intervention",required=True, help="Date d'intervention")
    lieu_intervention_latitude = fields.Float(
        compute='_compute_glatlng', string='G Latitude', store=True,
        multi='glatlng')
    lieu_intervention_longitude = fields.Float(
        compute='_compute_glatlng', string='G Longitude', store=True,
        multi='glatlng')
    lieu_intervention_adresse = fields.Char(string='''Lieu d'intervention''', required=True) # compute='_get_address',

    is_display_gm = fields.Boolean('Display Google Maps?')


    def _get_address(self):
        address = []
        # if self.street:
        #     address.append(self.street)
        # if self.street2:
        #     address.append(self.street2)
        # if self.city:
        #     address.append(self.city)
        # if self.state_id:
        #     address.append(self.state_id.name)
        # if self.country_id:
        #     address.append(self.country_id.name)
        # if self.zip:
        #     address.append(self.zip)
        # return ', '.join(address)
        return self.lieu_intervention_adresse

    @api.model
    def get_google_maps_data(self, domain=[]):
        # get all partners need to display google maps
        domain.append(('is_display_gm', '=', True))
        fiches = self.search(domain)
        locations = []
        for f in fiches:
            location = [
                partner.street, partner.g_lat, partner.g_lng, partner.id]
            locations.append(location)

        # get google maps center configuration
        IC = self.env['ir.config_parameter']
        gm_c_lat = float(IC.get_param('Google_Maps_Center_Latitude'))
        gm_c_lng = float(IC.get_param('Google_Maps_Center_Longitude'))
        gm_zoom = int(IC.get_param('Google_Maps_Zoom'))

        return locations, (gm_c_lat, gm_c_lng, gm_zoom)

    @api.depends('lieu_intervention_latitude', 'lieu_intervention_longitude', 'lieu_intervention_adresse')
    def _compute_glatlng(self):
        for record in self:
            address = record.lieu_intervention_adresse
            if address:
                g = geocoder.google(address).latlng
                if g:
                    record.lieu_intervention_latitude = g[0]
                    record.lieu_intervention_longitude = g[1]
                else:
                    record.lieu_intervention_latitude = False
                    record.lieu_intervention_longitude = False

    @api.one
    def action_depart(self):
        self.status_interv = 'brouillon'

    @api.one
    def action_remplir(self):
        self.status_interv = 'rempli'

    @api.one
    def action_valider(self):
        self.status_interv = 'valide'

    @api.one
    def action_compta(self):
        self.status_interv = 'comptabilise'

    @api.one
    def action_decompta(self):
        self.status_interv = 'valide'
