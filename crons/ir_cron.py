# -*- coding: utf-8 -*-
from openerp import fields, models, api, _
from dateutil.relativedelta import relativedelta
from openerp.tools import DEFAULT_SERVER_DATE_FORMAT
import logging
_logger = logging.getLogger(__name__)


class fiche_chantier(models.Model):
    _inherit = "fiche.chantier"

    @api.model
    def scheduler_reminder_mrp_production(self):
        #Cette méthode est appelée par une tâche cron
        """ envoi des notification en cas de non remplissage de la fiche de chantier de la veille"""
        mail_mail_obj = self.env['mail.mail']
        values = {}
        today = fields.Date.today()
        fiche_chantier = self.search([('state', '=', 'draft')])
        res = {}
        for record in fiche_chantier:
            limit_date = (fields.Datetime.from_string(today) - relativedelta(days=+1)).strftime(DEFAULT_SERVER_DATE_FORMAT)
            if record.inter_date <= limit_date:
                if record.equipe_id.manager in res:
                    res[record.equipe_id.manager].append(record.name)
                else:
                    res[record.equipe_id.manager] = [record.name]
        for item, value in res.items():
            char = ', '.join(value)
            body = "Bonjour %s,<br><br>il y a des fiches chantier a remplir : %s.<br><br>Cordialement." %(item.name, char)
            values['subject'] = 'Alerte fiche de chantier'
            values['email_to'] = item.work_email
            values['body_html'] = '<pre><span class="inner-pre" style="font-size: 15px">%s<br></span></pre>' %body
            msg_id = mail_mail_obj.create(values)
            if msg_id:
                msg_id.send()
        return True


class Equipe(models.Model):
    _inherit = 'equipe'

    @api.model
    def scheduler_chek_teams(self):
        """Cette méthode est appelée par une tâche cron 
        ... """
        today = fields.Date.today()
        teams = self.search([('active', '=', True)])
        for record in teams:
            today_date = (fields.Datetime.from_string(today)).strftime(DEFAULT_SERVER_DATE_FORMAT)
            if record.create_date < today_date:
                record.active = False
        return True
