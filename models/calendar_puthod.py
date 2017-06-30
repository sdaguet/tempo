# -*- coding: utf-8 -*-
from openerp import api, fields, models
import logging
_logger = logging.getLogger(__name__)

class CalendarPuthod(models.Model):
    _inherit = 'calendar.event'

    partner_p_ids = fields.Many2many(comodel_name="res.partner", string="Responsables", compute="_compute_users")
    #
    # psartner_ids = fields.many2many('res.partner', 'calendar_event_res_partner_rel', string='Attendees',
    #                                 states={'done': [('readonly', True)]})

    @api.one
    @api.depends('partner_p_ids')
    def _compute_users(self):
        users = []
        fiches = self.env['fiche.chantier'].search([('user_id','!=', False)])
        for f in fiches:
            users.append(f.user_id.partner_id.id)
        self.partner_p_ids = users
        print "iciiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiii"
        print self.partner_p_ids.ids
        print self.partner_ids.ids
        pass