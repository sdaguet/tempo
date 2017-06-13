# -*- coding: utf-8 -*-
from openerp import fields, models, api, _


class NewModule(models.Model):
    _inherit = 'hr.employee'

    janvier = fields.Float("Janvier", compute="_compute_months")
    fevrier = fields.Float("Fevrier", compute="_compute_months")
    mars = fields.Float("Mars", compute="_compute_months")
    avril = fields.Float("Avril", compute="_compute_months")
    mai = fields.Float("Mai", compute="_compute_months")
    juin = fields.Float("Juin", compute="_compute_months")
    juillet = fields.Float("Juillet", compute="_compute_months")
    aout = fields.Float("Août", compute="_compute_months")
    septembre = fields.Float("Septembre", compute="_compute_months")
    octobre = fields.Float("Octobre", compute="_compute_months")
    novembre = fields.Float("Novembre", compute="_compute_months")
    decembre = fields.Float("Décembre", compute="_compute_months")
    attendance_id = fields.Many2one(comodel_name="hr.attendance")

    @api.one
    @api.depends('attendance_id.name')
    def _compute_months(self):
        count_1 = self.env['hr.attendance'].search_count([('employee_id', '=', self.id), ('name', 'like', '%-01-%')])
        count_2 = self.env['hr.attendance'].search_count([('employee_id', '=', self.id), ('name', 'like', '%-02-%')])
        count_3 = self.env['hr.attendance'].search_count([('employee_id', '=', self.id), ('name', 'like', '%-03-%')])
        count_4 = self.env['hr.attendance'].search_count([('employee_id', '=', self.id), ('name', 'like', '%-04-%')])
        count_5 = self.env['hr.attendance'].search_count([('employee_id', '=', self.id), ('name', 'like', '%-05-%')])
        count_6 = self.env['hr.attendance'].search_count([('employee_id', '=', self.id), ('name', 'like', '%-06-%')])
        count_7 = self.env['hr.attendance'].search_count([('employee_id', '=', self.id), ('name', 'like', '%-07-%')])
        count_8 = self.env['hr.attendance'].search_count([('employee_id', '=', self.id), ('name', 'like', '%-08-%')])
        count_9 = self.env['hr.attendance'].search_count([('employee_id', '=', self.id), ('name', 'like', '%-09-%')])
        count_10 = self.env['hr.attendance'].search_count([('employee_id', '=', self.id), ('name', 'like', '%-10-%')])
        count_11 = self.env['hr.attendance'].search_count([('employee_id', '=', self.id), ('name', 'like', '%-11-%')])
        count_12 = self.env['hr.attendance'].search_count([('employee_id', '=', self.id), ('name', 'like', '%-12-%')])

        self.janvier = count_1 * 8
        self.fevrier = count_2 * 8
        self.mars = count_3 * 8
        self.avril = count_4 * 8
        self.mai = count_5 * 8
        self.juin = count_6 * 8
        self.juillet = count_7 * 8
        self.aout = count_8 * 8
        self.septembre = count_9 * 8
        self.octobre = count_10 * 8
        self.novembre = count_11 * 8
        self.decembre = count_12 * 8

        pass
