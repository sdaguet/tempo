# -*- coding: utf-8 -*-
from openerp import api, fields, models
import collections
import logging
_logger = logging.getLogger(__name__)

class ParserOrder(models.Model):
    _inherit = 'fiche.chantier'
    _order = 'inter_date desc'
    inter_date = fields.Date(string="Date d'intervention", required=True, help="Date d'intervention")


class BilanReport(models.AbstractModel):
    _name = 'report.darb_puthod.report_bilan_chantier'

    @api.multi
    def get_sum_product(self, doc):
        sum_v = 0
        sum_p_d = 0
        sum_t = 0
        sum_ta = 0
        sum_pl = 0
        sum_dh = 0
        sum_pr = 0
        sum_g = 0
        sum_a = 0
        sum_divers = 0
        sum_f = 0
        sum_s = 0

        sum_c_v = 0
        sum_c_p_d = 0
        sum_c_t = 0
        sum_c_ta = 0
        sum_c_pl = 0
        sum_c_dh = 0
        sum_c_pr = 0
        sum_c_g = 0
        sum_c_a = 0
        sum_c_divers = 0
        sum_c_f = 0
        sum_c_s = 0

        sum = 0
        sum_c = 0

        chantier_order = self.env['chantier'].browse(doc.id).order_id
        order_lines = chantier_order.order_line

        for ol in order_lines:

            if ol.product_id.categ_id.name == "Végétaux":
                sum_v = sum_v + ol.price_unit
                sum_c_v = sum_c_v + ol.purchase_price

            elif ol.product_id.categ_id.name == "Préparation/Déplacement":
                sum_p_d = sum_p_d + ol.price_unit
                sum_c_p_d = sum_c_p_d + ol.purchase_price

            elif ol.product_id.categ_id.name == "Tonte":
                sum_t = sum_t + ol.price_unit
                sum_c_t = sum_c_t + ol.purchase_price

            elif ol.product_id.categ_id.name == "Taille":
                sum_ta = sum_ta + ol.price_unit
                sum_c_ta = sum_c_ta + ol.purchase_price

            elif ol.product_id.categ_id.name == "Plantation":
                sum_pl = sum_pl + ol.price_unit
                sum_c_pl = sum_c_pl + ol.purchase_price

            elif ol.product_id.categ_id.name == "Desherbage":
                sum_dh = sum_dh + ol.price_unit
                sum_c_dh = sum_c_dh + ol.purchase_price

            elif ol.product_id.categ_id.name == "Protection":
                sum_pr = sum_pr + ol.price_unit
                sum_c_pr = sum_c_pr + ol.purchase_price

            elif ol.product_id.categ_id.name == "Gazons":
                sum_g = sum_g + ol.price_unit
                sum_c_g = sum_c_g + ol.purchase_price

            elif ol.product_id.categ_id.name == "Arrosage":
                sum_a = sum_a + ol.price_unit
                sum_c_a = sum_c_a + ol.purchase_price

            elif ol.product_id.categ_id.name == "Fournitures plantation":
                sum_f = sum_f + ol.price_unit
                sum_c_f = sum_c_f + ol.purchase_price

            elif ol.product_id.categ_id.name == "Sous-Traitance":
                sum_s = sum_s + ol.price_unit
                sum_c_s = sum_c_s + ol.purchase_price

            else:
                sum_divers = sum_divers + ol.price_unit
                sum_c_divers = sum_c_divers + ol.purchase_price

        sum = sum_v + sum_p_d + sum_t + sum_ta + sum_pl + sum_dh + sum_pr + sum_g + sum_a + sum_divers + sum_f + sum_s
        sum_c = sum_c_v + sum_c_p_d + sum_c_t + sum_c_ta + sum_c_pl + sum_c_dh + sum_c_pr + sum_c_g + sum_c_a + sum_c_divers + sum_c_f + sum_c_s


        return (sum_v,
                sum_p_d,
                sum_t,
                sum_ta,
                sum_pl,
                sum_dh,
                sum_pr,
                sum_g,
                sum_a,
                sum_divers,
                sum_f,
                sum_s,

                sum_c_v,
                sum_c_p_d,
                sum_c_t,
                sum_c_ta,
                sum_c_pl,
                sum_c_dh,
                sum_c_pr,
                sum_c_g,
                sum_c_a,
                sum_c_divers,
                sum_c_f,
                sum_c_s,
                sum,
                sum_c)

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
    def get_tmp_cost(self, etss):

        tmp_cost_p_d = 0
        tmp_cost_t = 0
        tmp_cost_ta = 0
        tmp_cost_pl = 0
        tmp_cost_dh = 0
        tmp_cost_pr = 0
        tmp_cost_g = 0
        tmp_cost_a = 0
        tmp_cost_divers = 0

        tmp_costs = []

        for ets in etss:
            for et in ets:
                if et.type == "p" or et.type == "d":
                    tmp_cost_p_d = tmp_cost_p_d + (self.get_time(et.heure_fin) - self.get_time(
                        et.heure_deb)) * et.time_cost
                elif et.type == "t":
                    tmp_cost_t = tmp_cost_t + (self.get_time(et.heure_fin) - self.get_time(et.heure_deb)) * et.time_cost
                elif et.type == "ta":
                    tmp_cost_ta = tmp_cost_ta + (self.get_time(et.heure_fin) - self.get_time(
                        et.heure_deb)) * et.time_cost
                elif et.type == "pl":
                    tmp_cost_pl = tmp_cost_pl + (self.get_time(et.heure_fin) - self.get_time(
                        et.heure_deb)) * et.time_cost
                elif et.type == "dh":
                    tmp_cost_dh = tmp_cost_dh + (self.get_time(et.heure_fin) - self.get_time(
                        et.heure_deb)) * et.time_cost
                elif et.type == "pr":
                    tmp_cost_pr = tmp_cost_pr + (self.get_time(et.heure_fin) - self.get_time(
                        et.heure_deb)) * et.time_cost
                elif et.type == "g":
                    tmp_cost_g = tmp_cost_g + (self.get_time(et.heure_fin) - self.get_time(et.heure_deb)) * et.time_cost
                elif et.type == "a":
                    tmp_cost_a = tmp_cost_a + (self.get_time(et.heure_fin) - self.get_time(et.heure_deb)) * et.time_cost
                else:
                    tmp_cost_divers = tmp_cost_divers + (self.get_time(et.heure_fin) - self.get_time(
                        et.heure_deb)) * et.time_cost

            tmp_costs.extend([tmp_cost_p_d,
                              tmp_cost_t,
                              tmp_cost_ta,
                              tmp_cost_pl,
                              tmp_cost_dh,
                              tmp_cost_pr,
                              tmp_cost_g,
                              tmp_cost_a,
                              tmp_cost_divers])
            return tmp_costs

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
        tmp_cost = self.get_tmp_cost(employee_tasks)
        
		#logger ajouté
        #print "tmp"
        #print tmp
        _logger.info("bilan_main_oeuvre(self, sub): %r" % tmp)
		
		#logger ajouté
		#print "date_e"
        #print date_e
        _logger.info("bilan_main_oeuvre(self, sub): %r" % date_e)
        
        date_e = list(set(date_e))
        #logger ajouté
		#print "date_e"
        #print len(date_e)
        _logger.info("bilan_main_oeuvre(self, sub): %r" % len(date_e))
		
        plus = self.add_plus(date_e)
        #logger ajouté
		#print "date_e"
        #print plus
        _logger.info("bilan_main_oeuvre(self, sub): %r" % plus)
        return (date, plus, tmp, tmp_cost, comment)

    @api.multi
    def render_html(self, data=None):
        report = self.env['report']._get_report_from_name('darb_puthod.report_bilan_chantier')

        docargs = {
            'doc_ids': self._ids,
            'doc_model': report.model,
            'docs': self.env['chantier'].browse(self._ids),
            'bilan_main_oeuvre': self.bilan_main_oeuvre,
            'get_sum_product' : self.get_sum_product
        }

        return self.env['report'].render('darb_puthod.report_bilan_chantier', docargs)
