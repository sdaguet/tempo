# -*- coding: utf-8 -*-
from openerp import fields, models, api, _

class Equipe(models.Model):
    
    _name ='equipe'
    name = fields.Char('Name',required=True)
    manager = fields.Many2one('hr.employee', string='Manager', index=True, track_visibility='onchange',required=True)
   #ressource_list= fields.One2Many('class_li�', ondelete='cascade', string="Ressource List", required=True)
