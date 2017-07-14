# -*- coding: utf-8 -*-
from openerp import api, fields, models
import collections


class BilanReport(models.AbstractModel):
    _name = 'report.darb_puthod.report_bilan_chantier'

    @api.multi
    def bilan_main_oeuvre(self,doc):
        tasks = []

        fiches = self.env['fiche.chantier'].search([('chantier_id','=',doc.id)])
        for f in fiches:
            tasks.append(f.subtasks)
            for s in tasks:
                print ""

        return tasks



    @api.multi
    def render_html(self, data=None):
        report = self.env['report']._get_report_from_name('darb_puthod.report_bilan_chantier')

        docargs = {
            'doc_ids': self._ids,
            'doc_model': report.model,
            'docs': self.env['chantier'].browse(self._ids),
            'bilan_main_oeuvre': self.bilan_main_oeuvre,
            }

        return self.env['report'].render('darb_puthod.report_bilan_chantier', docargs)