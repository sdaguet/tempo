# -*- coding: utf-8 -*-
from openerp import fields, models, api, _

import logging
_logger = logging.getLogger(__name__)   

class Equipe(models.Model):
    _inherit = "hr.employee"
	
    team_name = fields.Char('Team Name',required=True)
    manager = fields.Char('Manager',required=True) 
   #ressource_list= fields.One2Many('class_lié', ondelete='cascade', string="Ressource List", required=True)