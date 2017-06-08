# -*- coding: utf-8 -*-
from openerp import fields, models, api, _
import logging
_logger = logging.getLogger(__name__)

class Equipe(models.Model):
    _name ='equipe'
    name = fields.Char('Team Name',required=True)
    manager = fields.Many2one('hr.employee', string='Manager', index=True, track_visibility='onchange',required=True)
    fichechantier_ids = fields.One2many('fiche.chantier', 'equipe_id', string='Fiche Chantier')
    ressource_list = fields.One2many('hr.employee', 'equipe_id', string="Ressource List")


class coefficientK(models.Model):
    _name = 'coefficientK'

    date = fields.Date()

    journees_tot_ann = fields.Float(string='Journées totales annuelles')
    repos_hebdo = fields.Float(string='Repos hebdomadaires')
    jrs_feries_semaine = fields.Float(string='Jours fériés en semaine')
    conges_contractuels = fields.Float(string='Congés contractuels')
    jrs_ouvr_contracts = fields.Float(string="Jours ouvrés contractuels")
    hrs_ouvr_jrn = fields.Float(string="Heures ouvrables journ.")
    hrs_ouvr_ann = fields.Float(string="Heures ouvrables anuelles")
    absn_prevu = fields.Float(string="Asbsenéisme")
    absn_maladies_acc = fields.Float(string="Absences maladie et accid.")
    ###########################################################################
    hrs_pres_ann = fields.Float(string="HEURES DE PRES. ANN")
    ###########################################################################
    hrs_feries_semaine = fields.Float(string='Heures fériées en semaine')
    hrs_conges_contractuels = fields.Float(string='Congés contractuels en Heures')
    

    ###########################################################################
    absn_maladies_acc = fields.Float(string="Absences maladie et accid.")
    ###########################################################################



    ###########################################################################
    absn_maladies_acc = fields.Float(string="Absences maladie et accid.")
    ###########################################################################
    coeffct_k = fields.Float()

class employee(models.Model):
    _inherit = 'hr.employee'

    equipe_id = fields.Many2one('equipe', string='Equipe')
    profile_type = fields.Selection([
        ('OUVRIERS', u'OUVRIERS'),
        ('EMPLOYES', u'EMPLOYES'),
        ('APPRENTIS', u'APPRENTIS'),
        ('OCCASIONNELS', u'OCCASIONNELS')],
        string='Profile')


    @api.multi
    def pointer_entree(self, datetime=None):
        datetime = fields.Datetime.now()
        vals = {
                'name': datetime,
                'employee_id': self.id,
                'action': 'sign_in',
                }
        self.env['hr.attendance'].create(vals)
        return True

    @api.multi
    def pointer_sortie(self, datetime=None):
        datetime = fields.Datetime.now()
        vals = {
                'name': datetime,
                'employee_id': self.id,
                'action': 'sign_out',
                }
        self.env['hr.attendance'].create(vals)
        return True
