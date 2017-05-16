# -*- coding: utf-8 -*-
from openerp import fields, models, api, _
# from openerp.exceptions import ValidationError
# from dateutil.relativedelta import relativedelta
# from openerp.tools import DEFAULT_SERVER_DATE_FORMAT, DEFAULT_SERVER_DATETIME_FORMAT
import geocoder
import logging
_logger = logging.getLogger(__name__)

class fiche_chantier(models.Model):
    _inherit = "mrp.production"
    _name = "fiche.chantier"
    _description = 'Fiche de Chantier'
    status_interv = fields.Selection([
        ('brouillon', u'A remplir'),
        ('rempli', u'Rempli. A valider'),
        ('valide', u'Validé. A comptabiliser'),
        ('comptabilise', u'Comptabilisé')], default='brouillon',
        string='Status FC', readonly=True, track_visibility='onchange')

    inter_date = fields.Datetime(string="Date d'intervention",required=True, help="Date d'intervention")
    equipe_id = fields.Many2one('equipe', string='Equipe', index=True, track_visibility='onchange')

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
