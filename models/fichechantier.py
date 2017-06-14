# -*- coding: utf-8 -*-
from openerp import fields, models, api, _
# from openerp.exceptions import ValidationError
# from dateutil.relativedelta import relativedelta
# from openerp.tools import DEFAULT_SERVER_DATE_FORMAT, DEFAULT_SERVER_DATETIME_FORMAT
import geocoder
import logging
_logger = logging.getLogger(__name__)


class wizard_create_fiche_chantier(models.TransientModel):
    _name = 'wizard.create.fiche.chantiere'

    inter_date = fields.Datetime(string="Date d'intervention",required=True, help="Date d'intervention")
    equipe_id = fields.Many2one('equipe', string='Equipe', index=True, track_visibility='onchange')
    chantier_id = fields.Many2one('chantier', string='Chantier', index=True, track_visibility='onchange')
    subtasks = fields.One2many('subtask', 'fiche_chantier_id', string="Tâches")

    @api.model
    def default_get(self, fields_list):
        res = models.TransientModel.default_get(self, fields_list)
        context = dict(self._context or {})
        active_ids = context.get('active_ids', []) or []
        related_chantier = self.env['chantier'].browse(active_ids)
        tasks_list = [line.product_id.task_ids for line in related_chantier.order_id.order_line]
        task_ids = []
        for x in tasks_list:
            for y in x:
                task_ids.append((4, y.id))
        res['subtasks'] = task_ids
        return res

    @api.multi
    def create_fiche_chantier(self):
        """ ...
        """
        context = dict(self._context or {})
        active_ids = context.get('active_ids', []) or []
        related_chantier = self.env['chantier'].browse(active_ids)
        vals = {
            'equipe_id': self.equipe_id.id,
            'chantier_id': self.chantier_id.id,
            'product_id': 1,
            'inter_date': self.inter_date,
            'subtasks': [(4, task.id) for task in self.subtasks],
            }
        fiche_chantier_id = self.env['fiche.chantier'].create(vals)
        return {
                'name': 'Fiche Chantier',
                'view_type': 'form',
                'view_mode': 'form',
                'res_model': 'fiche.chantier',
                'res_id': fiche_chantier_id.id,
                'view_id': False,
                'target': 'current_edit',
                'type': 'ir.actions.act_window',
                }


class product(models.Model):
    _inherit = 'product.product'

    task_ids = fields.One2many('subtask', 'product_id', string="Tâches")


class subtask(models.Model):
    _name = 'subtask'

    name = fields.Char('Tâche')
    description = fields.Text('Description')
    fiche_chantier_id = fields.Many2one('fiche.chantier', string='Chantier', index=True, track_visibility='onchange')
    product_id = fields.Many2one('product.product', string='Produit', index=True, track_visibility='onchange')


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
    order_id = fields.Many2one('sale.order', string="Order")
    fiche_ids = fields.One2many('fiche.chantier', 'chantier_id', string="Fiches de Chantier")

    @api.one
    def action_dispatch(self):
        self.state = 'progress'

    @api.one
    def action_done(self):
        self.state = 'done'

    @api.model
    def get_google_maps_data(self, domain=[]):
        # get all partners need to display google maps
        chantiers = self.search([('is_display_gm', '=', True), ('state', '!=', 'done')])
        locations = []
        for chantier in chantiers:
            location = [
                chantier.address, chantier.g_lat, chantier.g_lng, chantier.id, chantier.name, chantier.order_id.partner_id.name]
            locations.append(location)

        IC = self.env['ir.config_parameter']
        gm_c_lat = float(IC.get_param('Google_Maps_Center_Latitude'))
        gm_c_lng = float(IC.get_param('Google_Maps_Center_Longitude'))
        gm_zoom = int(IC.get_param('Google_Maps_Zoom'))

        return locations, (gm_c_lat, gm_c_lng, gm_zoom)

    @api.multi
    def create_fiche_chantier(self):
        return {
                'name': 'Fiche Chantier',
                'view_type': 'form',
                'view_mode': 'form',
                'res_model': 'wizard.create.fiche.chantiere',
                'view_id': False,
                'target': 'new',
                'type': 'ir.actions.act_window',
            }


class fiche_chantier(models.Model):
    _inherit = "mrp.production"
    _name = "fiche.chantier"
    _description = 'Fiche de Chantier'

    @api.model
    def _get_default_uom_id(self):
        # _logger.info('self.env.ref("product.product_uom_kgm", raise_if_not_found=False)' + self.env.ref("product.product_uom_kgm", raise_if_not_found=False))
        return self.env.ref("product.product_uom_kgm", raise_if_not_found=False)

    @api.model
    def _get_default_product_id(self):
        return self.env.ref("darb_puthod.product_default_product", raise_if_not_found=False)

    product_id = fields.Many2one(
        'product.product', 'Product',
        domain=[('type', 'in', ['product', 'consu'])],
        readonly=True, required=False,
        states={'confirmed': [('readonly', False)]},default=_get_default_product_id)

    product_uom = fields.Many2one(
        'product.uom', 'Product Unit of Measure',
        readonly=True, required=False,
        states={'confirmed': [('readonly', False)]},default=_get_default_uom_id)


    @api.onchange('equipe_id')
    def _onchange_equipe_id(self):
        if self.equipe_id:
            self.user_id = self.equipe_id.manager.user_id

    state = fields.Selection([
        ('draft', 'A remplir'),
        ('cancel', 'Annulé'),
        ('confirmed', 'Rempli. A valider'),
        ('ready', 'Validé. A comptabiliser'),
        ('done', 'Comptabilisé')], default='draft', copy=False,
        string='Status FC', readonly=True, track_visibility='onchange')

    termine = fields.Boolean(string=u"Chantier Terminé", default=False)
    inter_date = fields.Datetime(string="Date d'intervention",required=True, help="Date d'intervention")
    equipe_id = fields.Many2one('equipe', string='Equipe', index=True, track_visibility='onchange')
    chantier_id = fields.Many2one('chantier', string='Chantier', index=True, track_visibility='onchange')
    partner_id = fields.Many2one('res.partner', string='Client', related='chantier_id.order_id.partner_id')
    veicule_ids = fields.One2many('fiche.chantier.vehicle', 'fiche_chantier_id', string=u'Véhicules')
    materiel_ids = fields.One2many('fiche.chantier.materiel', 'fiche_chantier_id', string=u'Matériels')
    machine_ids = fields.One2many('fiche.chantier.machine', 'fiche_chantier_id', string=u'Machines')
    fourniture_ids = fields.One2many('fiche.chantier.fourniture', 'fiche_chantier_id', string=u'Fournitures')
    kit_ids = fields.One2many('fiche.chantier.kit', 'fiche_chantier_id', string=u'Kits RBKS')
    tuteurage_ids = fields.One2many('fiche.chantier.tuteurage', 'fiche_chantier_id', string=u'Tuteurage')
    vigitaux_ids = fields.One2many('fiche.chantier.vigitaux', 'fiche_chantier_id', string=u'Vigitaux')
    engrais_ids = fields.One2many('fiche.chantier.engrais', 'fiche_chantier_id', string=u'Engrais')
    gazons_ids = fields.One2many('fiche.chantier.gazons', 'fiche_chantier_id', string=u'Gazons')
    gmateriel_ids = fields.One2many('fiche.chantier.gmateriel', 'fiche_chantier_id', string=u'Matériel')
    escalier_ids = fields.One2many('fiche.chantier.escalier', 'fiche_chantier_id', string=u'Escalier')
    outils_ids = fields.One2many('fiche.chantier.outils', 'fiche_chantier_id', string=u'Outils')
    cloture_ids = fields.One2many('fiche.chantier.cloture', 'fiche_chantier_id', string=u'Cloture')
    divers_ids = fields.One2many('fiche.chantier.divers', 'fiche_chantier_id', string=u'Divers')
    terrasse_ids = fields.One2many('fiche.chantier.terrasse', 'fiche_chantier_id', string=u'Terrasse')
    scloture_ids = fields.One2many('fiche.chantier.scloture', 'fiche_chantier_id', string=u'Suite Cloture')
    subtasks = fields.One2many('subtask', 'fiche_chantier_id', string="Tâches")


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


class fiche_chantier_vigitaux(models.Model):
    _name = "fiche.chantier.vigitaux"
    _description = 'Vigitaux de Fiche de Chantier'

    fiche_chantier_id = fields.Many2one('fiche.chantier', string='Fiche de Chantier', index=True, track_visibility='onchange')
    vigitaux_id = fields.Many2one('product.product', string=u'Liste des vigitaux (rajout, retour)')
    date = fields.Date(u'Date')
    commentaire = fields.Text('Commentaires')


class fiche_chantier_engrais(models.Model):
    _name = "fiche.chantier.engrais"
    _description = 'Engrais de Fiche de Chantier'

    fiche_chantier_id = fields.Many2one('fiche.chantier', string='Fiche de Chantier', index=True, track_visibility='onchange')
    engrais_id = fields.Many2one('product.product', string=u'Engrais')
    quantity = fields.Float(u'Qté/tps')


class fiche_chantier_gazons(models.Model):
    _name = "fiche.chantier.gazons"
    _description = 'Gazons de Fiche de Chantier'

    fiche_chantier_id = fields.Many2one('fiche.chantier', string='Fiche de Chantier', index=True, track_visibility='onchange')
    gazons_id = fields.Many2one('product.product', string=u'Gazons')
    quantity = fields.Float(u'Qté/tps')


class fiche_chantier_gmateriel(models.Model):
    _name = "fiche.chantier.gmateriel"
    _description = 'Matériels d\'engazonnement de Fiche de Chantier'

    fiche_chantier_id = fields.Many2one('fiche.chantier', string='Fiche de Chantier', index=True, track_visibility='onchange')
    gmateriel_id = fields.Many2one('product.product', string=u'Matériel')
    quantity = fields.Float(u'Qté/tps')


class fiche_chantier_escalier(models.Model):
    _name = "fiche.chantier.escalier"
    _description = 'Escalier de Fiche de Chantier'

    fiche_chantier_id = fields.Many2one('fiche.chantier', string='Fiche de Chantier', index=True, track_visibility='onchange')
    escalier_id = fields.Many2one('product.product', string=u'Escalier/Muret bois')
    quantity = fields.Float(u'Qté')


class fiche_chantier_outils(models.Model):
    _name = "fiche.chantier.outils"
    _description = 'Outils de Fiche de Chantier'

    fiche_chantier_id = fields.Many2one('fiche.chantier', string='Fiche de Chantier', index=True, track_visibility='onchange')
    outils_id = fields.Many2one('product.product', string=u'Outils')
    quantity = fields.Float(u'Tps')


class fiche_chantier_cloture(models.Model):
    _name = "fiche.chantier.cloture"
    _description = 'Cloture de Fiche de Chantier'

    fiche_chantier_id = fields.Many2one('fiche.chantier', string='Fiche de Chantier', index=True, track_visibility='onchange')
    cloture_id = fields.Many2one('product.product', string=u'Cloture')
    quantity = fields.Float(u'Qté/tps')


class fiche_chantier_divers(models.Model):
    _name = "fiche.chantier.divers"
    _description = 'Divers de Fiche de Chantier'

    fiche_chantier_id = fields.Many2one('fiche.chantier', string='Fiche de Chantier', index=True, track_visibility='onchange')
    divers_id = fields.Many2one('product.product', string=u'Divers')
    quantity = fields.Float(u'Qté/tps')


class fiche_chantier_terrasse(models.Model):
    _name = "fiche.chantier.terrasse"
    _description = 'Terrasse de Fiche de Chantier'

    fiche_chantier_id = fields.Many2one('fiche.chantier', string='Fiche de Chantier', index=True, track_visibility='onchange')
    terrasse_id = fields.Many2one('product.product', string=u'Terrasse')
    quantity = fields.Float(u'Qté')


class fiche_chantier_scloture(models.Model):
    _name = "fiche.chantier.scloture"
    _description = 'Suite Cloture de Fiche de Chantier'

    fiche_chantier_id = fields.Many2one('fiche.chantier', string='Fiche de Chantier', index=True, track_visibility='onchange')
    scloture_id = fields.Many2one('product.product', string=u'Suite Cloture')
    quantity = fields.Float(u'Qté')
