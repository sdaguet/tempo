# -*- coding: utf-8 -*-
from openerp import fields, models, api, _
# from openerp.exceptions import ValidationError
# from dateutil.relativedelta import relativedelta
# from openerp.tools import DEFAULT_SERVER_DATE_FORMAT, DEFAULT_SERVER_DATETIME_FORMAT
import geocoder
import logging
_logger = logging.getLogger(__name__)


class subtask(models.Model):
    _name = 'subtask'

    name = fields.Char('Tâche')
    description = fields.Text('Description')
    chantier_id = fields.Many2one('chantier', string='Chantier', index=True, track_visibility='onchange')


class chantier(models.Model):
    _name = "chantier"
    _description = 'Chantier'

    @api.depends('address')
    def _compute_glatlng(self):
        for record in self:
            address = record.address
            if address:
                g = geocoder.google(address).latlng
                if g:
                    record.g_lat = g[0]
                    record.g_lng = g[1]
                else:
                    record.g_lat = False
                    record.g_lng = False

    name = fields.Char('Nom')
    state = fields.Selection([
        ('draft', 'Brouillon'),
        ('progress', 'En cours'),
        ('done', 'Terminé'),], default='draft', copy=False,
        string='Status', readonly=True, track_visibility='onchange')

    address = fields.Text(string='Address')
    is_display_gm = fields.Boolean('Display Google Maps?')
    g_lat = fields.Float(
        compute='_compute_glatlng', string='G Latitude', store=True,
        multi='glatlng', digits=(3,12))
    g_lng = fields.Float(
        compute='_compute_glatlng', string='G Longitude', store=True,
        multi='glatlng', digits=(3,12))
    subtasks = fields.One2many('subtask', 'chantier_id', string="Tâches")
    order_id = fields.Many2one('sale.order', string="Order")
    fiche_ids = fields.One2many('fiche.chantier', 'chantier_id', string="Fiches de Chantier")


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
        ('done', 'Comptabilisé')], default='draft', copy=False,
        string='Status FC', readonly=True, track_visibility='onchange')

    inter_date = fields.Datetime(string="Date d'intervention",required=True, help="Date d'intervention")
    equipe_id = fields.Many2one('equipe', string='Equipe', index=True, track_visibility='onchange')
    chantier_id = fields.Many2one('chantier', string='Chantier', index=True, track_visibility='onchange')
