# -*- coding: utf-8 -*-
from openerp import fields, models, api, _
from openerp.exceptions import ValidationError

import logging
from datetime import datetime

_logger = logging.getLogger(__name__)


class Equipe(models.Model):
    _name ='equipe'
    name = fields.Char('Team Name', required=True, compute='_get_name')
    manager = fields.Many2one('hr.employee', string='Manager', index=True, track_visibility='onchange',required=True)
    fichechantier_ids = fields.One2many('fiche.chantier', 'equipe_id', string='Fiche Chantier')
    ressource_list = fields.One2many('hr.employee', 'equipe_id', string="Ressource List")
    active = fields.Boolean(u"Active")

    @api.multi
    @api.depends('manager')
    def _get_name(self):
        for record in self:
            if record.manager:
                record.name = 'Equipe ' + record.manager.name

    @api.one
    @api.constrains('active', 'manager')
    def _check_active(self):
        if self.active is True:
            actives = self.sudo().search([('active', '=', True), ('manager', '=', self.manager.id)])
            if actives and actives != self:
                raise ValidationError(u"Une équipe active existe déjà !")


class employee(models.Model):
    _inherit = 'hr.employee'

    equipe_id = fields.Many2one('equipe', string='Equipe')
    profile_type = fields.Selection([
        ('OUVRIERS', u'OUVRIERS'),
        ('EMPLOYES', u'EMPLOYES'),
        ('APPRENTIS', u'APPRENTIS'),
        ('OCCASIONNELS', u'OCCASIONNELS')],
        string='Profile')

    @api.multi
    def print_coeff_k(self):
        return {
            'name': 'Chantier',
            'view_type': 'form',
            'view_mode': 'form',
            'res_model': 'wizard.print.coeffk',
            'view_id': False,
            'target': 'new',
            'type': 'ir.actions.act_window',
        }

    @api.multi
    def pointer_entree(self, datetime=None):
        datetime = fields.Datetime.now()
        vals = {
                'name': datetime,
                'employee_id': self.id,
                'action': 'sign_in',
                }
        self.env['hr.attendance'].create(vals)
        return True

    @api.multi
    def pointer_sortie(self, datetime=None):
        datetime = fields.Datetime.now()
        vals = {
                'name': datetime,
                'employee_id': self.id,
                'action': 'sign_out',
                }
        self.env['hr.attendance'].create(vals)
        return True



class wizard_print_coeffk(models.TransientModel):
    _name = 'wizard.print.coeffk'

    dob = fields.Datetime(string="Date d'intervention",required=True, help="Date d'intervention")
    employee = fields.Char(u'Employé')

    @api.model
    def default_get(self, fields_list):
        res = models.TransientModel.default_get(self, fields_list)
        context = dict(self._context or {})
        active_ids = context.get('active_ids', []) or []
        related_employee = self.env['hr.employee'].browse(active_ids)
        res['employee'] = related_employee.name
        return res

    @api.multi
    def print_coeff_k(self):
        """ ...
        """
        context = dict(self._context or {})
        active_ids = context.get('active_ids', []) or []
        date = datetime.strptime(self.dob, '%Y-%m-%d %H:%M:%S')
        _logger.info("DOB : " + str(self.dob))
        _logger.info("MONTH : " + str(date.month))
        _logger.info("YEAR : " + str(date.year))
        vals = {
            'employee_id': active_ids,
            'month': date.month,
            'year': date.year,
            'dob': self.dob,
            }
        return  self.pool['report'].get_action(
            self.env.cr, self.env.uid, active_ids, 'darb_puthod.report_hr_employee_view', data=vals, context=context)

