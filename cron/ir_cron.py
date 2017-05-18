# -*- coding: utf-8 -*-
from openerp import fields, models, api, _
from dateutil.relativedelta import relativedelta
from openerp.tools import DEFAULT_SERVER_DATETIME_FORMAT
import logging
_logger = logging.getLogger(__name__)


class fiche_chantier(models.Model):
    _inherit = "mrp.production"

    @api.model
    def scheduler_reminder_mrp_production(self):
        #Cette méthode est appelée par une tâche cron
        """ envoi des notification en cas de non remplissage de la fiche de chantier de la veille"""
        mail_mail_obj = self.env['mail.mail']
        values = {}
        today = fields.Datetime.now()
        fiche_chantier = self.search([('state', '=', 'draft')])
        res = {}
        for record in fiche_chantier:
            limit_date = (fields.Datetime.from_string(today) + relativedelta(days=+1)).strftime(DEFAULT_SERVER_DATETIME_FORMAT)
            if record.inter_date <= limit_date:
                if record.equipe_id.manager in res:
                    res[record.equipe_id.manager].append(record)
                else:
                    res[record.equipe_id.manager] = [record]
        for item, value in res.items():
            body = _("Bonjour %s,\n" %(item.name))
            footer = _("Cordialement.\n")
            values['subject'] = 'Alerte fiche de chantier'
            values['email_to'] = item
            values['body_html'] = '<pre><span class="inner-pre" style="font-size: 15px">%s<br>%s</span></pre>' %(body, footer),
            values['body'] = body
            msg_id = mail_mail_obj.create(values)
            if msg_id:
                mail_mail_obj.send([msg_id])
        return True
