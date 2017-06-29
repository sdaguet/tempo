# -*- coding: utf-8 -*-
from openerp import api, fields, models

class CalendarPuthod(models.Model):
    _inherit = 'calendar.event'

    user_ids = fields.Many2many(comodel_name="res.users", string="Responsables", compute="_compute_users")

    @api.one
    @api.depends('user_ids')
    def _compute_users(self):
        users = []
        fiches = self.env['fiche.chantier'].search([('user_id','!=', False)])
        for f in fiches:
            users.append(f.user_id.id)
        self.user_ids = users
        print "iciiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiii"
        print users
        print self.user_ids.ids
        print self.partner_ids
        pass

