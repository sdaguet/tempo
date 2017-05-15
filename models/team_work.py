# -*- coding: utf-8 -*-
from openerp import fields, models, api, _
    
class Equipe(models.Model):
    _name ='equipe'
  
    name = fields.Char('Name',required=True)
    manager = fields.Char('Manager',required=True) 
   #ressource_list= fields.One2Many('class_lié', ondelete='cascade', string="Ressource List", required=True)