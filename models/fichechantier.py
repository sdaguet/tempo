#!/usr/bin/python
# coding: utf8

import sys
reload(sys)
sys.setdefaultencoding('utf-8')

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
    def default_get(self, fields_list):     # Cette fonction retourne le tableau res qui est égal à models.TransientModel.default_get(self, fields_list)
        res = models.TransientModel.default_get(self, fields_list)
        context = dict(self._context or {})
        active_ids = context.get('active_ids', []) or []
        related_chantier = self.env['chantier'].browse(active_ids)
        tasks_list = [line.product_id.task_ids for line in related_chantier.order_id.order_line if line.tasks]
        task_ids = []
        for x in tasks_list:
            for y in x:
                task_ids.append((0, 0, {'name': y.name, 'description': y.description, 'rapide': y.rapide, 'fiche_chantier_task': True, 'subtask_id': y.id,}))
        res['subtasks'] = task_ids
        return res

    @api.multi
    def create_fiche_chantier(self):   # Cette fonction permet de créer une fiche chantier à partir du wizard elle retourne un enregistrement
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

    tasks = fields.Boolean(string=u"Peut avoir des tâches")
    task_ids = fields.One2many('subtask', 'product_id', string=u"Tâches")
    altitude_max = fields.Float(string='Altitude MAX', digits=(3, 0),default = 0)
    altitude_min = fields.Float(string='Altitude MIN', digits=(3, 0),default = 0)
    qrcode = fields.Char(string='QR Code')

    #fields puthod
    n_article = fields.Char(string='N° Article')
    famille_p = fields.Selection(string="Famille", selection=[('0', 'FERTIL-POTS'), ('1', 'PLTS FORESTIRS'),('2', 'HAIES'), ('3', 'PLTAPISSANTES'),('4', 'CONIFERES'), ('5', 'ARB.FRUITIERS'),('6', 'SAPINS DE NOEL'), ('7', 'ARBUSTES'),('8', 'ARB.FEUILLUS'), ('9', 'SAPINS DE NOEL'),('ARB', 'ARBUSTES'), ('eng', 'engrais'),('F', 'FOURNITURES-AIDE PLANTATION'), ('JAR', 'J.PLARBUSTES'),('OP-SPE', 'OPERATIONS SPECIALES'), ('TOP', 'topiaire'),('TRA', 'Transport'), ('VIV', 'vivaces'),('Z', 'PRESTATIONS'), ], required=False)
    #importe = fields.Boolean(string="importe",default = False)
    marque_savoie = fields.Boolean(string="Marque Savoie",  )
    name_puthod = fields.Char(string="Nom complet", required=False)
    compute_famille_p = fields.Char(string="_compute_famille_p", compute='_compute_famille_p')
    active = fields.Boolean('Active', default = True,readonly = 0,help="If unchecked, it will allow you to hide the product without removing it.", compute ='_compute_actif')

    @api.multi
    @api.depends('barcode','active','importe')
    def _compute_actif(self):
        bc = self.barcode
        print "barcode"
        print bc
        imp = self.importe
        print "imp"
        print imp
        if imp:
            if bc == False or bc == '' or bc == ' ' :
                self.active = False
            else:
                self.active = True

    @api.multi
    @api.depends('name_puthod','name')
    def name_get(self):		# La fonction name_get(self) retourne la liste result qui se compose de l'id et le nom de l'enregistrement 
        result = []
        for p in self:
            if not p.name_puthod:
                result.append((p.id, p.name))
            else:
                print p.name_puthod
                result.append((p.id,p.name_puthod))
        return result


    _sql_constraints = [
        ('qrcode_uniq', 'unique(qrcode)', _("A qrcode can only be assigned to one product !")),
    ]

    @api.one
    def get_product_taille(self):
        attribute_ids = self.attribute_value_ids
        res = [attribute.name for attribute in attribute_ids if attribute.attribute_id == self.env.ref('darb_puthod.product_attribute_taille')]
        taille = res[0] if res else None
        return taille

    @api.one
    @api.constrains('altitude_max', 'altitude_min')
    def _check_altitude(self):        # La fonction _check_altitude permet de voir si l'altitude max est supérieur à l'altitude min sinon elle lève une exception
        if self.altitude_max < self.altitude_min:
            raise ValidationError(u"Altitude MAX est inférieur à Altitude MIN !")

    @api.multi
    @api.depends('famille_p')
    def _compute_famille_p(self):

        famille = self.famille_p

        if famille == 'eng':
            xml_record_eng = self.env.ref("darb_puthod.product_category_engrais")
            print "xml_record_eng"
            print xml_record_eng

            self.categ_id = xml_record_eng
            print "xml_record_eng"
            self.type = 'consu'

        elif famille == 'F':
                    xml_record_F = self.env.ref("darb_puthod.product_category_fourniture")
                    self.categ_id = xml_record_F
                    self.type = 'consu'


        elif famille == 'OP-SPE':
                    xml_record_OP_SPE = self.env.ref("darb_puthod.product_category_divers")
                    self.categ_id = xml_record_OP_SPE
                    #type a definir

        elif famille == 'TRA':
                    xml_record_TRA = self.env.ref("darb_puthod.product_category_vehicle")
                    self.categ_id = xml_record_TRA
                    self.type = 'service'

        elif famille == 'Z':
                    xml_record_Z = self.env.ref("darb_puthod.product_category_prestations")
                    self.categ_id = xml_record_Z
                    self.type = 'service'

        elif famille == False:
            pass

        else:
            xml_record_vigitaux = self.env.ref("darb_puthod.product_category_vigitaux")
            print "xml_record_vigitaux"
            print xml_record_vigitaux
            self.categ_id = xml_record_vigitaux
            self.type = 'product'

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
    def _get_name(self):   # Cette fonction permet de calculer automatiquement la valeur du champ name en appelant l'attribut compute
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
    def _get_name(self):  # Cette fonction permet de calculer automatiquement la valeur du champ name en appelant l'attribut compute
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
    def _compute_glatlng(self):  # Cette fonction permet de remplir automatiquement les champs g_lat et g_lng de latitude et longitude respectivement à partir d'une adresse
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
    is_display_gm = fields.Boolean('Display Google Maps?', default=True)
    g_lat = fields.Float(
        compute='_compute_glatlng', string='G Latitude', store=True,
        multi='glatlng', digits=(3, 12))
    g_lng = fields.Float(
        compute='_compute_glatlng', string='G Longitude', store=True,
        multi='glatlng', digits=(3, 12))
    order_id = fields.Many2one('sale.order', string="Order")
    order_type = fields.Selection(string="Type de chantier", related='order_id.order_type', required=False, )
    fiche_ids = fields.One2many('fiche.chantier', 'chantier_id', string="Fiches de Chantier")


    @api.one
    @api.depends('fiche_ids', 'fiche_ids.termine', 'order_id')
    def _compute_state(self):  # Cette fonction permet de remplir automatiquement les champs state soit en progress, done, draft
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
    def action_dispatch(self):  # Cette fonction modifie les deux champs de l'enregistrement valid_click et state
        self.write({'valid_click':True, 'state':'progress'})
        #self.state = 'progress'

    done_click  = fields.Boolean(string="done", default = False )
    @api.one
    def action_done(self): # Cette fonction modifie les deux champs de l'enregistrement valid_click et state
        self.write({'done_click':True, 'state':'done'})
        #self.state = 'done'

    @api.model
    def get_google_maps_data(self, domain=[]):   # Cette fonction retourne la location des chantiers : latitude,longitude et zoom
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
    def create_fiche_chantier(self):  # Cette fonction retourne un enregistrement et permet de créer une fiche de chantier
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
    def action_confirm(self):  # Cette fonction modifie le champ de l'enregistrement state à l'etat confirmed
        res = self.write({'state': 'confirmed'})
        return res

    @api.multi
    def moves_ready(self):  # Cette fonction modifie le champ de l'enregistrement state à l'etat ready
        res = self.write({'state': 'ready'})
        return res

    @api.multi
    def button_produce(self):  # Cette fonction modifie le champ de l'enregistrement state à l'etat in_production
        res = self.write({'state': 'in_production'})
        order_id = self.chantier_id.order_id
        picking_id = self.env['stock.picking'].search([('group_id', '=', order_id.procurement_group_id.id),('state', 'in', ('assigned', 'confirmed', 'partially_available'))]) if order_id.procurement_group_id else []
        picking_id.force_assign()
        for pack in picking_id.pack_operation_product_ids:
            prod_vegetaux = [vigitaux.vigitaux_id for vigitaux in self.vigitaux_ids]
            tot_vegetaux = sum([1 for vigitaux in self.vigitaux_ids if pack.product_id == vigitaux.vigitaux_id])

            prod_fournitures = [fourniture.fourniture_id for fourniture in self.fourniture_ids]
            tot_fournitures = sum([fourniture.quantity for fourniture in self.fourniture_ids if pack.product_id == fourniture.fourniture_id])

            prod_kits = [kit.kit_id for kit in self.kit_ids]
            tot_kits = sum([kit.quantity for kit in self.kit_ids if pack.product_id == kit.kit_id])

            prod_tuteurages = [tuteurage.tuteurage_id for tuteurage in self.tuteurage_ids]
            tot_tuteurages = sum([tuteurage.quantity for tuteurage in self.tuteurage_ids if pack.product_id == tuteurage.tuteurage_id])

            prod_engrais = [engrais.engrais_id for engrais in self.engrais_ids]
            tot_engrais = sum([engrais.quantity for engrais in self.engrais_ids if pack.product_id == engrais.engrais_id])

            prod_gazons = [gazons.gazons_id for gazons in self.gazons_ids]
            tot_gazons = sum([gazons.quantity for gazons in self.gazons_ids if pack.product_id == gazons.gazons_id])

            prod_escaliers = [escalier.escalier_id for escalier in self.escalier_ids]
            tot_escaliers = sum([escalier.quantity for escalier in self.escalier_ids if pack.product_id == escalier.escalier_id])

            prod_divers = [divers.divers_id for divers in self.divers_ids]
            tot_divers = sum([divers.quantity for divers in self.divers_ids if pack.product_id == divers.divers_id])

            prod_terrasses = [terrasse.terrasse_id for terrasse in self.terrasse_ids]
            tot_terrasses = sum([terrasse.quantity for terrasse in self.terrasse_ids if pack.product_id == terrasse.terrasse_id])

            prod_sclotures = [scloture.scloture_id for scloture in self.scloture_ids]
            sclotures = sum([scloture.quantity for scloture in self.scloture_ids if pack.product_id == scloture.scloture_id])

            prod_clotures = [cloture.cloture_id for cloture in self.cloture_ids]
            clotures = sum([cloture.quantity for cloture in self.cloture_ids if pack.product_id == cloture.cloture_id])
            list_clotures = prod_sclotures + prod_clotures
            tot_clotures = sclotures + clotures

            if pack.product_id in prod_vegetaux:
                pack.qty_done = tot_vegetaux
            if pack.product_id in prod_fournitures:
                pack.qty_done = tot_fournitures
            if pack.product_id in list_clotures:
                pack.qty_done = tot_clotures
            if pack.product_id in prod_kits:
                pack.qty_done = tot_kits
            if pack.product_id in prod_tuteurages:
                pack.qty_done = tot_tuteurages
            if pack.product_id in prod_engrais:
                pack.qty_done = tot_engrais
            if pack.product_id in prod_gazons:
                pack.qty_done = tot_gazons
            if pack.product_id in prod_escaliers:
                pack.qty_done = tot_escaliers
            if pack.product_id in prod_divers:
                pack.qty_done = tot_divers
            if pack.product_id in prod_terrasses:
                pack.qty_done = tot_terrasses
        wiz_act = picking_id.do_new_transfer()
        if wiz_act:
            wiz = self.env[wiz_act['res_model']].browse(wiz_act['res_id'])
            wiz.process()
        return res

    @api.multi
    def button_done(self):  # Cette fonction modifie le champ de l'enregistrement state à l'etat done
        res = self.write({'state': 'done'})
        return res

    @api.multi
    def button_cancel(self): # Cette fonction modifie le champ de l'enregistrement state à l'etat cancel
        res = self.write({'state': 'cancel'})
        return res

    @api.multi
    def button_back(self):  # Cette fonction modifie le champ de l'enregistrement state à l'etat draft
        res = self.write({'state': 'draft'})
        return res

    @api.model
    def _get_default_uom_id(self): # Cette fonction retourne self.env.ref("product.product_uom_kgm", raise_if_not_found=False)
        # _logger.info('self.env.ref("product.product_uom_kgm", raise_if_not_found=False)' + self.env.ref("product.product_uom_kgm", raise_if_not_found=False))
        return self.env.ref("product.product_uom_kgm", raise_if_not_found=False)

    @api.model
    def _get_default_product_id(self):  # Cette fonction retourne self.env.ref("darb_puthod.product_default_product", raise_if_not_found=False)
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
    def _compute_user(self):  # Cette fonction permet de calculer automatiquement la valeur du champ user_id en appelant l'attribut compute
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
    def _compute_type_inter(self):  # Cette fonction permet de calculer automatiquement la valeur du champ type_inter en appelant l'attribut compute
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
