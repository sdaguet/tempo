# -*- coding: utf-8 -*-
from openerp import fields, models, api, _
import logging
_logger = logging.getLogger(__name__)

class Equipe(models.Model):
    _name ='equipe'
    name = fields.Char('Team Name',required=True)
    manager = fields.Many2one('hr.employee', string='Manager', index=True, track_visibility='onchange',required=True)
    fichechantier_ids = fields.One2many('fiche.chantier', 'equipe_id', string='Fiche Chantier')
   #ressource_list= fields.One2Many('class_li�', ondelete='cascade', string="Ressource List", required=True)


class employee(models.Model):
    _inherit = 'hr.employee'

    def pointer_entree(self, datetime):
        vals = {
                'name': datetime,
                'employee_id': self.id,
                'action': 'sign_in',
                }
        self.env['hr.attendance'].create(vals)
        return True
