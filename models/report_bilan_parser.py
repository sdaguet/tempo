# -*- coding: utf-8 -*-
from openerp import api, fields, models
import collections


class ParserOrder(models.Model):
    _inherit = 'fiche.chantier'
    _order = 'inter_date desc'
    inter_date = fields.Date(string="Date d'intervention", required=True, help="Date d'intervention")


class BilanReport(models.AbstractModel):
    _name = 'report.darb_puthod.report_bilan_chantier'

    @api.multi
    def get_time(self, heure):
        return {
            '7:00': 7,
            '7:15': 7.15,
            '7:30': 7.30,
            '8:00': 8,
            '8:15': 8.15,
            '8:30': 8.30,
            '9:00': 9,
            '9:15': 9.15,
            '9:30': 9.30,
            '10:00': 10,
            '10:15': 10.15,
            '10:30': 10.30,
            '11:00': 11,
            '11:15': 11.15,
            '11:30': 11.30,
            '12:00': 12,
            '13:00': 13,
            '13:15': 13.15,
            '13:30': 13.30,
            '14:00': 14,
            '14:15': 14.15,
            '14:30': 14.30,
            '15:00': 15,
            '15:15': 15.15,
            '15:30': 15.30,
            '16:00': 16,
            '16:15': 16.15,
            '16:30': 16.30,
            '17:00': 17,
            '17:15': 17.15,
            '17:30': 17.30,
            '18:00': 18,
            '18:15': 18.15,
            '18:30': 18.30,
            '19:00': 19,
        }[heure]

    @api.multi
    def add_plus(self, date_e):
        lenn = len(date_e)
        i = 0
        res = ""
        for d in date_e:
            if i > lenn:
                break

            if i != lenn:
                i = i + 1
                if res == "":
                    res = d
                elif res != "":
                    res = res + " + " + d

        return res

    @api.multi
    def get_tmp(self, etss):
        tmp_p_d = 0
        tmp_t = 0
        tmp_ta = 0
        tmp_pl = 0
        tmp_dh = 0
        tmp_pr = 0
        tmp_g = 0
        tmp_a = 0
        tmp_divers = 0

        tmps = []

        for ets in etss:
            for et in ets:
                if et.type == "p" or et.type == "d":
                    tmp_p_d = tmp_p_d + (self.get_time(et.heure_fin) - self.get_time(et.heure_deb))
                elif et.type == "t":
                    tmp_t = tmp_t + (self.get_time(et.heure_fin) - self.get_time(et.heure_deb))
                elif et.type == "ta":
                    tmp_ta = tmp_ta + (self.get_time(et.heure_fin) - self.get_time(et.heure_deb))
                elif et.type == "pl":
                    tmp_pl = tmp_pl + (self.get_time(et.heure_fin) - self.get_time(et.heure_deb))
                elif et.type == "dh":
                    tmp_dh = tmp_dh + (self.get_time(et.heure_fin) - self.get_time(et.heure_deb))
                elif et.type == "pr":
                    tmp_pr = tmp_pr + (self.get_time(et.heure_fin) - self.get_time(et.heure_deb))
                elif et.type == "g":
                    tmp_g = tmp_g + (self.get_time(et.heure_fin) - self.get_time(et.heure_deb))
                elif et.type == "a":
                    tmp_a = tmp_a + (self.get_time(et.heure_fin) - self.get_time(et.heure_deb))
                else:
                    tmp_divers = tmp_divers + (self.get_time(et.heure_fin) - self.get_time(et.heure_deb))

        tmps.extend([tmp_p_d,
                    tmp_t,
                    tmp_ta,
                    tmp_pl,
                    tmp_dh,
                    tmp_pr,
                    tmp_g,
                    tmp_a,
                    tmp_divers])
        return tmps

    @api.multi
    def bilan_main_oeuvre(self, sub):
        employee_tasks = []
        date_e = []
        comment = ""

        fiche = self.env['fiche.chantier'].search([('id', '=', sub.id)])
        date = fiche.inter_date
        for s in fiche.subtasks:
            employee_tasks.append(s.employee_subtask_ids)
            if s.comment:
                comment = comment + "  " + s.comment
        for ets in employee_tasks:
            for et in ets:
                date_e.append(et.employee.name)
        tmp = self.get_tmp(employee_tasks)

        print "tmp"
        print tmp
        print "date_e"
        print date_e
        date_e = list(set(date_e))
        print "date_e"
        print len(date_e)
        plus = self.add_plus(date_e)
        print "date_e"
        print plus
        return (date, plus, tmp, comment)

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
