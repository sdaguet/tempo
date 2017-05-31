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


class employee(models.Model):
    _inherit = 'hr.employee'

    equipe_id = fields.Many2one('equipe', string='Equipe')

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
