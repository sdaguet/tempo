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
    state = fields.Selection([
        ('draft', 'A remplir'),
        ('cancel', 'Annulé'),
        ('confirmed', 'Rempli. A valider'),
        ('ready', 'Validé. A comptabiliser'),
        ('in_production', 'Validé. A comptabiliser'),
        ('done', 'Comptabilisé')], default='brouillon', copy=False,
        string='Status FC', readonly=True, track_visibility='onchange')

    inter_date = fields.Datetime(string="Date d'intervention",required=True, help="Date d'intervention")
    equipe_id = fields.Many2one('equipe', string='Equipe', index=True, track_visibility='onchange')
