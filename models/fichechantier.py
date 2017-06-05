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
    veicule_ids = fields.One2many('fiche.chantier.vehicle', 'fiche_chantier_id', string=u'Véhicules')
    materiel_ids = fields.One2many('fiche.chantier.materiel', 'fiche_chantier_id', string=u'Matériels')
    machine_ids = fields.One2many('fiche.chantier.machine', 'fiche_chantier_id', string=u'Machines')
    fourniture_ids = fields.One2many('fiche.chantier.fourniture', 'fiche_chantier_id', string=u'Fournitures')
    kit_ids = fields.One2many('fiche.chantier.kit', 'fiche_chantier_id', string=u'Kits RBKS')
    tuteurage_ids = fields.One2many('fiche.chantier.tuteurage', 'fiche_chantier_id', string=u'Tuteurage')


class fiche_chantier_vehicle(models.Model):
    _name = "fiche.chantier.vehicle"
    _description = 'Véhicules de Fiche de Chantier'

    fiche_chantier_id = fields.Many2one('fiche.chantier', string='Fiche de Chantier', index=True, track_visibility='onchange')
    vehicle_id = fields.Many2one('product.product', string=u'Véhicule')
    kms = fields.Float('KMS')


class fiche_chantier_materiel(models.Model):
    _name = "fiche.chantier.materiel"
    _description = 'Matériels de Fiche de Chantier'

    fiche_chantier_id = fields.Many2one('fiche.chantier', string='Fiche de Chantier', index=True, track_visibility='onchange')
    materiel_id = fields.Many2one('product.product', string=u'Matériel')
    temps = fields.Float('Temps')


class fiche_chantier_machine(models.Model):
    _name = "fiche.chantier.machine"
    _description = 'Machines de Fiche de Chantier'

    fiche_chantier_id = fields.Many2one('fiche.chantier', string='Fiche de Chantier', index=True, track_visibility='onchange')
    machine_id = fields.Many2one('product.product', string=u'Machine')
    temps = fields.Float('Temps')


class fiche_chantier_fourniture(models.Model):
    _name = "fiche.chantier.fourniture"
    _description = 'Fournitures de Fiche de Chantier'

    fiche_chantier_id = fields.Many2one('fiche.chantier', string='Fiche de Chantier', index=True, track_visibility='onchange')
    fourniture_id = fields.Many2one('product.product', string=u'Fournitures Plantation')
    quantity = fields.Float(u'Qté')


class fiche_chantier_kit(models.Model):
    _name = "fiche.chantier.kit"
    _description = 'Kits de Fiche de Chantier'

    fiche_chantier_id = fields.Many2one('fiche.chantier', string='Fiche de Chantier', index=True, track_visibility='onchange')
    kit_id = fields.Many2one('product.product', string=u'Kit RBKS')
    quantity = fields.Float(u'Qté')


class fiche_chantier_tuteurage(models.Model):
    _name = "fiche.chantier.tuteurage"
    _description = 'Tuteurages de Fiche de Chantier'

    fiche_chantier_id = fields.Many2one('fiche.chantier', string='Fiche de Chantier', index=True, track_visibility='onchange')
    tuteurage_id = fields.Many2one('product.product', string=u'Tuteurage')
    quantity = fields.Float(u'Qté')
