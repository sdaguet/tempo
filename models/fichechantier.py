#!/usr/bin/python
# coding: utf8
from openerp import fields, models, api, _
from openerp.exceptions import ValidationError
from datetime import datetime
# from dateutil.relativedelta import relativedelta
# from openerp.tools import DEFAULT_SERVER_DATE_FORMAT, DEFAULT_SERVER_DATETIME_FORMAT
import geocoder
import logging

_logger = logging.getLogger(__name__)

types = [
    ('p', 'Préparation'),
    ('d', 'Déplacement'),
    ('pl', 'Plantation'),
    ('t', 'Tonte'),
    ('ta', 'Taille'),
    ('dh', 'Désherbage'),
    ('g', 'Gazon'),
    ('g', 'Gazon plaqué'),
    ('a', 'Arrosage'),
    ('f', 'Fertilisation'),
    ('tb', 'Terrasse'),
    ('cl', 'Clôture'),
    ('pr', 'Protection'),
    ('em', 'Escalier-murêt'),
    ('ma', 'Maçonnerie'),
    ('di', 'Divers')]

plage_horaire = [
        ('7:00', '7:00'),
        ('7:15', '7:15'),
        ('7:30', '7:30'),
        ('8:00', '8:00'),
        ('8:15', '8:15'),
        ('8:30', '8:30'),
        ('9:00', '9:00'),
        ('9:15', '9:15'),
        ('9:30', '9:30'),
        ('10:00', '10:00'),
        ('10:15', '10:15'),
        ('10:30', '10:30'),
        ('11:00', '11:00'),
        ('11:15', '11:15'),
        ('11:30', '11:30'),
        ('12:00', '12:00'),
        ('13:00', '13:00'),
        ('13:15', '13:15'),
        ('13:30', '13:30'),
        ('14:00', '14:00'),
        ('14:15', '14:15'),
        ('14:30', '14:30'),
        ('15:00', '15:00'),
        ('15:15', '15:15'),
        ('15:30', '15:30'),
        ('16:00', '16:00'),
        ('16:15', '16:15'),
        ('16:30', '16:30'),
        ('17:00', '17:00'),
        ('17:15', '17:15'),
        ('17:30', '17:30'),
        ('18:00', '18:00'),
        ('18:15', '18:15'),
        ('18:30', '18:30'),
        ('19:00', '19:00')]


class subtask_wizard(models.TransientModel):
    _name = 'subtask.wizard'

    name = fields.Char('Tâche')
    description = fields.Text('Description')
    product_id = fields.Many2one('product.product', string='Produit', index=True, track_visibility='onchange')
    fiche_chantier_task = fields.Boolean(string="Ajouter")
    wizard_id = fields.Many2one('wizard.create.fiche.chantiere')
    rapide = fields.Boolean(string="Rapide")
    subtask_id = fields.Many2one('subtask', string='ref product Tâche')


class wizard_create_fiche_chantier(models.TransientModel):
    _name = 'wizard.create.fiche.chantiere'

    inter_date = fields.Date(string="Date d'intervention", required=True, help="Date d'intervention")
    equipe_id = fields.Many2one('equipe', string='Equipe', index=True, track_visibility='onchange')
    chantier_id = fields.Many2one('chantier', string='Chantier', index=True, track_visibility='onchange')
    subtasks = fields.One2many('subtask.wizard', 'wizard_id', string="Tâches")

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
                task_ids.append((0, 0, {'name': y.name, 'description': y.description, 'rapide': y.rapide, 'fiche_chantier_task': True, 'subtask_id': y.id,}))
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
            'chantier_id': related_chantier.id,
            'inter_date': self.inter_date,
            'subtasks': [((0, 0, {'subtask_id': task.subtask_id.id})) for task in self.subtasks if task.fiche_chantier_task == True],
            'address': related_chantier.address,
            'is_display_gm': related_chantier.is_display_gm,
            'g_lat': related_chantier.g_lat,
            'g_lng': related_chantier.g_lng,
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
    altitude_max = fields.Float(string='Altitude MAX', digits=(3, 0),default = 0)
    altitude_min = fields.Float(string='Altitude MIN', digits=(3, 0),default = 0)
    qrcode = fields.Char(string='QR Code')
    # N_Article = fields.Char(string='N° Article')
    # importe = fields.Boolean(string="importe",default = False)
    # famille = fields.Selection(string="Famille", selection=[('0', 'FERTIL-POTS'), ('1', 'PLTS FORESTIRS'),('2', 'HAIES'), ('3', 'PLTAPISSANTES'),('4', 'CONIFERES'), ('5', 'ARB.FRUITIERS'),('6', 'SAPINS DE NOEL'), ('7', 'ARBUSTES'),('8', 'ARB.FEUILLUS'), ('9', 'SAPINS DE NOEL'),('ARB', 'ARBUSTES'), ('eng', 'engrais'),('F', 'FOURNITURES-AIDE PLANTATION'), ('JAR', 'J.PLARBUSTES'),('OP-SPE', 'OPERATIONS SPECIALES'), ('TOP', 'topiaire'),('TRA', 'Transport'), ('VIV', 'vivaces'),('Z', 'PRESTATIONS'), ], required=False, )
    # marque_savoie = fields.Boolean(string="Marque Savoie",  )
    _sql_constraints = [
        ('qrcode_uniq', 'unique(qrcode)', _("A qrcode can only be assigned to one product !")),
    ]

    @api.one
    @api.constrains('altitude_max', 'altitude_min')
    def _check_altitude(self):
        if self.altitude_max < self.altitude_min:
            raise ValidationError(u"Altitude MAX est inférieur à Altitude MIN !")

    # @api.multi
    # @api.depends('N_Article_id','N_Article_id.Poids_Brut','N_Article_id.Code_Barre','N_Article_id.Libelle_commercial','N_Article_id.Taille_bis','N_Article_id.Nom_francais', 'N_Article_id.Prix_Etiquette')
    # def _compute_Article(self):
    #
    #     if self.N_Article_id:
    #
    #         #pour les categ
    #         # xml_record = self.env.ref("darb_puthod.product_category_vehicle")
    #         #
    #         # print "xml_record"
    #         # print xml_record
    #
    #         Nom_francais = self.N_Article_id.Nom_francais
    #         if Nom_francais:
    #             Nom_francais = Nom_francais
    #         else:
    #             Nom_francais = ""
    #
    #         Libelle_commercial = self.N_Article_id.Libelle_commercial
    #         if Libelle_commercial:
    #             Libelle_commercial = Libelle_commercial
    #         else:
    #             Libelle_commercial = ""
    #
    #         Taille_bis = self.N_Article_id.Taille_bis
    #         if Taille_bis:
    #             Taille_bis = Taille_bis
    #         else:
    #             Taille_bis = ""
    #
    #         name = Libelle_commercial + " " + Taille_bis + " - " +Nom_francais
    #         lst_price = float(self.N_Article_id.Prix_Etiquette)
    #         weight = float(self.N_Article_id.Poids_Brut)
    #         Code_Barre = self.N_Article_id.Code_Barre
    #         record = self.write({'lst_price': lst_price, 'weight': weight, 'name': name, 'barcode':Code_Barre})
    #         return record


class subtask(models.Model):
    _name = 'subtask'

    name = fields.Char('Tâche')
    description = fields.Text('Description')
    product_id = fields.Many2one('product.product', string='Produit', index=True, track_visibility='onchange')
    rapide = fields.Boolean(string="Rapide")



class fiche_chantier_subtasks(models.Model):
    _name = 'fiche.chantier.subtasks'

    @api.multi
    @api.depends('subtask_id')
    def _get_name(self):
        for record in self:
            if record.subtask_id:
                record.name = record.subtask_id.name

    name = fields.Char('Nom', compute='_get_name')
    subtask_id = fields.Many2one('subtask', string='Tâche', index=True, track_visibility='onchange')
    fiche_chantier_id = fields.Many2one('fiche.chantier', string="Fiches de Chantier", index=True, track_visibility='onchange')

    comment = fields.Text('Commentaire')
    state = fields.Selection([
        ('draft', 'Non'),
        ('done', 'Oui'),], default='draft', copy=False,
        string='Terminé?', track_visibility='onchange')
    employee_subtask_ids = fields.One2many('employees.subtasks', 'fiche_chantier_subtask_id', string="Horaires")


class employees_subtasks(models.Model):
    _name = 'employees.subtasks'

    @api.multi
    @api.depends('employee', 'heure_deb', 'heure_fin')
    def _get_name(self):
        for record in self:
            if record.employee and record.heure_deb and record.heure_fin:
                record.name = str(record.employee.name) + ' : ' + str(record.type) + ' (' + str(record.heure_deb) + ' - ' + str(record.heure_fin) + ')'

    name = fields.Char('Nom', compute='_get_name')
    employee = fields.Many2one('hr.employee', string='Employee', index=True, track_visibility='onchange', required=True)
    heure_deb = fields.Selection(plage_horaire, copy=False ,string='Heure début', track_visibility='onchange')
    heure_fin = fields.Selection(plage_horaire, copy=False ,string='Heure fin', track_visibility='onchange')
    fiche_chantier_subtask_id = fields.Many2one('fiche.chantier.subtasks', string='fcst', index=True, track_visibility='onchange')
    type = fields.Selection(types, copy=False,
                            string='Type', track_visibility='onchange')
    time_cost = fields.Float(string="time cost",  required=False, related='employee.timesheet_cost',store = True )

	#Check time : Start < End
	#Check intersections between time
    """@api.one
    @api.constrains('heure_deb', 'heure_fin')
    def _check_active(self):
        if self.heure_deb and self.heure_fin:
            dd = datetime.strptime(self.heure_deb,'%H:%M')
            df = datetime.strptime(self.heure_fin,'%H:%M')
            if dd > df:
                raise ValidationError(u"Heure début > Heure fin !")

    @api.multi
    @api.constrains('heure_deb', 'heure_fin', 'employee', 'fiche_chantier_subtask_id')
    def _check_active2(self):
        if self.heure_deb and self.heure_fin:
            dd = datetime.strptime(self.heure_deb,'%H:%M')
            df = datetime.strptime(self.heure_fin,'%H:%M')
        item_ids = self.search([('employee', '=', self.employee.id), ('id', '<>', self.id), ('fiche_chantier_subtask_id', '=', self.fiche_chantier_subtask_id.id)])
        for item in item_ids:
            idd = datetime.strptime(item.heure_deb,'%H:%M')
            idf = datetime.strptime(item.heure_fin,'%H:%M')
            if (df > idd and df < idf) or (dd > idd and dd < idf) or (dd > idd and df < idf) or (dd < idd and df > idf):
                raise ValidationError(u"Intersection entre plages horaires !")
        else:
            return True"""


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
        ('done', 'Terminé'), ], default='draft', copy=False,
        string='Status', readonly=True, track_visibility='onchange', compute="_compute_state")

    address = fields.Text(string='Adresse')
    is_display_gm = fields.Boolean('Display Google Maps?')
    g_lat = fields.Float(
        compute='_compute_glatlng', string='G Latitude', store=True,
        multi='glatlng', digits=(3, 12))
    g_lng = fields.Float(
        compute='_compute_glatlng', string='G Longitude', store=True,
        multi='glatlng', digits=(3, 12))
    order_id = fields.Many2one('sale.order', string="Order")
    fiche_ids = fields.One2many('fiche.chantier', 'chantier_id', string="Fiches de Chantier")


    @api.one
    @api.depends('fiche_ids', 'fiche_ids.termine', 'order_id')
    def _compute_state(self):
        done = 1;
        if self.fiche_ids.ids != []:
            for fiche in self.fiche_ids:
                if fiche.termine == True:
                    done = 1
                else:
                    done = 0
                    break
            if done == 1: self.state = 'done'
            elif done == 0 and self.done_click != True: self.state = 'progress'
            else : self.state = 'done'

        elif self.valid_click != True and self.fiche_ids.ids == []:
            self.state = 'draft'
        else:
            self.state = 'progress'
        pass

    valid_click  = fields.Boolean(string="valid", default = False )

    @api.one
    def action_dispatch(self):
        self.write({'valid_click':True, 'state':'progress'})
        #self.state = 'progress'

    done_click  = fields.Boolean(string="done", default = False )
    @api.one
    def action_done(self):
        self.write({'done_click':True, 'state':'done'})
        #self.state = 'done'

    @api.model
    def get_google_maps_data(self, domain=[]):
        # get all partners need to display google maps
        chantiers = self.search([('is_display_gm', '=', True), ('state', '!=', 'done')])
        locations = []
        for chantier in chantiers:
            location = [
                chantier.address, chantier.g_lat, chantier.g_lng, chantier.id, chantier.name,
                chantier.order_id.partner_id.name]
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

    @api.multi
    def action_confirm(self):
        res = self.write({'state': 'confirmed'})
        return res

    @api.multi
    def moves_ready(self):
        res = self.write({'state': 'ready'})
        return res

    @api.multi
    def button_produce(self):
        res = self.write({'state': 'in_production'})
        return res

    @api.multi
    def button_done(self):
        res = self.write({'state': 'done'})
        return res

    @api.multi
    def button_cancel(self):
        res = self.write({'state': 'cancel'})
        return res

    @api.multi
    def button_back(self):
        res = self.write({'state': 'draft'})
        return res

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
        states={'confirmed': [('readonly', False)]}, default=_get_default_product_id)

    product_uom = fields.Many2one(
        'product.uom', 'Product Unit of Measure',
        readonly=True, required=False,
        states={'confirmed': [('readonly', False)]}, default=_get_default_uom_id)


    user_id = fields.Many2one('res.users', 'Responsible', compute="_compute_user")

    @api.multi
    @api.depends('equipe_id.manager.user_id')
    def _compute_user(self):
        for record in self:
            if record.equipe_id:
                record.user_id = record.equipe_id.manager.user_id

    state = fields.Selection([
        ('draft', 'A remplir'),
        ('confirmed', 'Envoyé. A valider'),
        ('ready', 'Validé. A comptabiliser'),
        ('in_production', 'Comptabilisé'),
        ('done', 'Terminé'),('cancel', 'Annulé')], default='draft', copy=False,
        string='Status FC', readonly=True, track_visibility='onchange')
	#change inter_date from datetime to date
    termine = fields.Boolean(string=u"Chantier Terminé", default=False)
    inter_date = fields.Date(string="Date d'intervention", required=True, help="Date d'intervention")
    equipe_id = fields.Many2one('equipe', string='Equipe', index=True, track_visibility='onchange')
    chantier_id = fields.Many2one('chantier', string='Chantier', index=True, track_visibility='onchange')
    partner_id = fields.Many2one('res.partner', string='Client', related='chantier_id.order_id.partner_id')
    veicule_ids = fields.One2many('fiche.chantier.vehicle', 'fiche_chantier_id', string=u'Véhicules')
    materiel_ids = fields.One2many('fiche.chantier.materiel', 'fiche_chantier_id', string=u'Matériels')
    machine_ids = fields.One2many('fiche.chantier.machine', 'fiche_chantier_id', string=u'Machines')
    fourniture_ids = fields.One2many('fiche.chantier.fourniture', 'fiche_chantier_id', string=u'Fournitures')
    kit_ids = fields.One2many('fiche.chantier.kit', 'fiche_chantier_id', string=u'Kits RBKS')
    tuteurage_ids = fields.One2many('fiche.chantier.tuteurage', 'fiche_chantier_id', string=u'Tuteurage')
    vigitaux_ids = fields.One2many('fiche.chantier.vigitaux', 'fiche_chantier_id', string=u'Végétaux')
    engrais_ids = fields.One2many('fiche.chantier.engrais', 'fiche_chantier_id', string=u'Engrais')
    gazons_ids = fields.One2many('fiche.chantier.gazons', 'fiche_chantier_id', string=u'Gazons')
    gmateriel_ids = fields.One2many('fiche.chantier.gmateriel', 'fiche_chantier_id', string=u'Matériel')
    escalier_ids = fields.One2many('fiche.chantier.escalier', 'fiche_chantier_id', string=u'Escalier')
    outils_ids = fields.One2many('fiche.chantier.outils', 'fiche_chantier_id', string=u'Outils')
    cloture_ids = fields.One2many('fiche.chantier.cloture', 'fiche_chantier_id', string=u'Cloture')
    divers_ids = fields.One2many('fiche.chantier.divers', 'fiche_chantier_id', string=u'Divers')
    terrasse_ids = fields.One2many('fiche.chantier.terrasse', 'fiche_chantier_id', string=u'Terrasse')
    scloture_ids = fields.One2many('fiche.chantier.scloture', 'fiche_chantier_id', string=u'Suite Cloture')
    subtasks = fields.One2many('fiche.chantier.subtasks', 'fiche_chantier_id', string=u"Tâches")
    type_inter = fields.Selection(string="Type d'intervention",compute="_compute_type_inter", selection=[('cloturante', 'Clôturante'), ('rapide', 'Rapide'),('maintenance', 'Maintenance'), ('normale', 'Normale')], required=False, )
    remarqs = fields.Text('Commentaire')

    @api.one
    @api.depends('subtasks','termine','chantier_id.order_id.order_type')
    def _compute_type_inter(self):
        rapide = False
        for s in self.subtasks:
            if s.subtask_id.rapide != True:
                rapide = False
                break
            else:
                rapide = True

        if self.termine:
            self.type_inter = 'cloturante'
        elif self.chantier_id.order_id.order_type == 'entretien' :
            self.type_inter = 'maintenance'
        elif rapide :
            self.type_inter = 'rapide'
        else:
            self.type_inter = 'normale'
        pass


class fiche_chantier_vehicle(models.Model):
    _name = "fiche.chantier.vehicle"
    _description = 'Véhicules de Fiche de Chantier'

    fiche_chantier_id = fields.Many2one('fiche.chantier', string='Fiche de Chantier', index=True,
                                        track_visibility='onchange')
    vehicle_id = fields.Many2one('product.product', string=u'Véhicule')
    kms = fields.Float('KMS')


class fiche_chantier_materiel(models.Model):
    _name = "fiche.chantier.materiel"
    _description = 'Matériels de Fiche de Chantier'

    fiche_chantier_id = fields.Many2one('fiche.chantier', string='Fiche de Chantier', index=True,
                                        track_visibility='onchange')
    materiel_id = fields.Many2one('product.product', string=u'Matériel')
    temps = fields.Float('Temps')


class fiche_chantier_machine(models.Model):
    _name = "fiche.chantier.machine"
    _description = 'Machines de Fiche de Chantier'

    fiche_chantier_id = fields.Many2one('fiche.chantier', string='Fiche de Chantier', index=True,
                                        track_visibility='onchange')
    machine_id = fields.Many2one('product.product', string=u'Machine')
    temps = fields.Float('Temps')


class fiche_chantier_fourniture(models.Model):
    _name = "fiche.chantier.fourniture"
    _description = 'Fournitures de Fiche de Chantier'

    fiche_chantier_id = fields.Many2one('fiche.chantier', string='Fiche de Chantier', index=True,
                                        track_visibility='onchange')
    fourniture_id = fields.Many2one('product.product', string=u'Fournitures Plantation')
    quantity = fields.Float(u'Qté')


class fiche_chantier_kit(models.Model):
    _name = "fiche.chantier.kit"
    _description = 'Kits de Fiche de Chantier'

    fiche_chantier_id = fields.Many2one('fiche.chantier', string='Fiche de Chantier', index=True,
                                        track_visibility='onchange')
    kit_id = fields.Many2one('product.product', string=u'Kit RBKS')
    quantity = fields.Float(u'Qté')


class fiche_chantier_tuteurage(models.Model):
    _name = "fiche.chantier.tuteurage"
    _description = 'Tuteurages de Fiche de Chantier'

    fiche_chantier_id = fields.Many2one('fiche.chantier', string='Fiche de Chantier', index=True,
                                        track_visibility='onchange')
    tuteurage_id = fields.Many2one('product.product', string=u'Tuteurage')
    quantity = fields.Float(u'Qté')


class fiche_chantier_vigitaux(models.Model):
    _name = "fiche.chantier.vigitaux"
    _description = 'Végétaux de Fiche de Chantier'

    fiche_chantier_id = fields.Many2one('fiche.chantier', string='Fiche de Chantier', index=True,
                                        track_visibility='onchange')
    vigitaux_id = fields.Many2one('product.product', string=u'Liste des Végétaux (rajout, retour)')
    date = fields.Date(u'Date')
    commentaire = fields.Text('Commentaires')


class fiche_chantier_engrais(models.Model):
    _name = "fiche.chantier.engrais"
    _description = 'Engrais de Fiche de Chantier'

    fiche_chantier_id = fields.Many2one('fiche.chantier', string='Fiche de Chantier', index=True,
                                        track_visibility='onchange')
    engrais_id = fields.Many2one('product.product', string=u'Engrais')
    quantity = fields.Float(u'Qté/tps')


class fiche_chantier_gazons(models.Model):
    _name = "fiche.chantier.gazons"
    _description = 'Gazons de Fiche de Chantier'

    fiche_chantier_id = fields.Many2one('fiche.chantier', string='Fiche de Chantier', index=True,
                                        track_visibility='onchange')
    gazons_id = fields.Many2one('product.product', string=u'Gazons')
    quantity = fields.Float(u'Qté/tps')


class fiche_chantier_gmateriel(models.Model):
    _name = "fiche.chantier.gmateriel"
    _description = 'Matériels d\'engazonnement de Fiche de Chantier'

    fiche_chantier_id = fields.Many2one('fiche.chantier', string='Fiche de Chantier', index=True,
                                        track_visibility='onchange')
    gmateriel_id = fields.Many2one('product.product', string=u'Matériel')
    quantity = fields.Float(u'Qté/tps')


class fiche_chantier_escalier(models.Model):
    _name = "fiche.chantier.escalier"
    _description = 'Escalier de Fiche de Chantier'

    fiche_chantier_id = fields.Many2one('fiche.chantier', string='Fiche de Chantier', index=True,
                                        track_visibility='onchange')
    escalier_id = fields.Many2one('product.product', string=u'Escalier/Muret bois')
    quantity = fields.Float(u'Qté')


class fiche_chantier_outils(models.Model):
    _name = "fiche.chantier.outils"
    _description = 'Outils de Fiche de Chantier'

    fiche_chantier_id = fields.Many2one('fiche.chantier', string='Fiche de Chantier', index=True,
                                        track_visibility='onchange')
    outils_id = fields.Many2one('product.product', string=u'Outils')
    quantity = fields.Float(u'Tps')


class fiche_chantier_cloture(models.Model):
    _name = "fiche.chantier.cloture"
    _description = 'Cloture de Fiche de Chantier'

    fiche_chantier_id = fields.Many2one('fiche.chantier', string='Fiche de Chantier', index=True,
                                        track_visibility='onchange')
    cloture_id = fields.Many2one('product.product', string=u'Cloture')
    quantity = fields.Float(u'Qté/tps')


class fiche_chantier_divers(models.Model):
    _name = "fiche.chantier.divers"
    _description = 'Divers de Fiche de Chantier'

    fiche_chantier_id = fields.Many2one('fiche.chantier', string='Fiche de Chantier', index=True,
                                        track_visibility='onchange')
    divers_id = fields.Many2one('product.product', string=u'Divers')
    quantity = fields.Float(u'Qté/tps')


class fiche_chantier_terrasse(models.Model):
    _name = "fiche.chantier.terrasse"
    _description = 'Terrasse de Fiche de Chantier'

    fiche_chantier_id = fields.Many2one('fiche.chantier', string='Fiche de Chantier', index=True,
                                        track_visibility='onchange')
    terrasse_id = fields.Many2one('product.product', string=u'Terrasse')
    quantity = fields.Float(u'Qté')


class fiche_chantier_scloture(models.Model):
    _name = "fiche.chantier.scloture"
    _description = 'Suite Cloture de Fiche de Chantier'

    fiche_chantier_id = fields.Many2one('fiche.chantier', string='Fiche de Chantier', index=True,
                                        track_visibility='onchange')
    scloture_id = fields.Many2one('product.product', string=u'Suite Cloture')
    quantity = fields.Float(u'Qté')
