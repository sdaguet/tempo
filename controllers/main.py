# -*- coding: utf-8 -*-
from openerp import http,  SUPERUSER_ID
from openerp.addons.website_project_issue.controllers.main import website_account
from openerp.http import request
from openerp.addons.web.http import request as reqst
from openerp import fields, models, api, _
import logging
_logger = logging.getLogger(__name__)

class WebsiteContractDarbtech(http.Controller):

    @http.route('/pointages', type='http', auth="user", website=True)
    def pointages(self, **kw):
        user = request.env.user
        cr, uid, context = request.cr, request.uid, request.context
        employes = request.registry.get('hr.employee')
        _logger.info("Current user = " + str(uid))
        current_employee = request.env['hr.employee'].sudo().search([('user_id', '=', uid)])
        _logger.info("Current employee = " + str(current_employee))
        list_teams = request.env['equipe'].sudo().search(
                [
                    ('manager', 'in', current_employee.ids)
                ])

        return http.request.render('darb_puthod.pointages', {
            'teams' : list_teams
                })

    @http.route('/pointer', type='json', auth="user", website=True)
    def pointer(self, **kw):
        user = request.env.user
        cr, uid, context = request.cr, request.uid, request.context
        employes = request.registry.get('hr.employee')
        _logger.info("POINTER user = " + str(uid))

        return {}

    @http.route(['/ficheslist'], type='http', auth="user", website=True)
    def fiches_liste(self, product_id=None):
        user = request.env.user
        cr, uid, context = reqst.cr, reqst.uid, reqst.context
        fiche = request.env['fiche.chantier'].sudo().search(
                [
                    ('user_id', '=', uid)
                ])

        _logger.info("Generated fiche RRRRRRRRRRRRRRRRRRRRRRRRRRRRRR : " + str(fiche))
        return http.request.render('darb_puthod.listfiches', {
                    'fiches': fiche,
                })

    # fiche info

    @http.route(['/ficheslist/<int:fiche>/'], type='http', auth="user", website=True)
    def showfiche(self, fiche):
        user = request.env.user
        cr, uid, context = reqst.cr, reqst.uid, reqst.context

        fiche_id = request.env['fiche.chantier'].sudo().search([('id', '=', fiche)])
        list_teams_id = request.env['fiche.chantier'].sudo().search([('id', '=', fiche)]).equipe_id

        _logger.info("Generated fiche_chantierRRRRRRRRRRRRRRRRRRRRRRRRRRRRRR : " + str(fiche))

        return http.request.render('darb_puthod.ficheviewer', {
            'teams': list_teams_id,
            'fiche': fiche_id,
        })

    @http.route('/ficheviewer', type='json', auth="user", website=True)
    def ficheviewer(self, **kw):
        user = request.env.user
        cr, uid, context = request.cr, request.uid, request.context
        fiche = request.registry.get('fiche.chantier')
        _logger.info("POINTERfffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff user = " + str(fiche))
        return {}

    @http.route(['/chantierslist'], type='http', auth="user", website=True)
    def chantiers_liste(self, product_id=None):
        user = request.env.user
        cr, uid, context = reqst.cr, reqst.uid, reqst.context

        fiche_chantier = request.env['fiche.chantier'].sudo().search([])


        _logger.info("Generated fiche_chantierRRRRRRRRRRRRRRRRRRRRRRRRRRRRRR : " + str(fiche_chantier))
        return http.request.render('darb_puthod.listchantiers', {
                    'chantiers': fiche_chantier,
                })

    @http.route(['/chantiersForm'], type='http', auth="user", website=True)
    def chantiers_form(self, product_id=None):
        user = request.env.user
        cr, uid, context = reqst.cr, reqst.uid, reqst.context

        fiche_chantier = request.env['fiche.chantier'].sudo().search([])

        _logger.info("Generated fiche_chantierRRRRRRRRRRRRRRRRRRRRRRRRRRRRRR : " + str(fiche_chantier))
        form = [1,2,3]
        return http.request.render('darb_puthod.formchantiers', {
                    'chantiers': fiche_chantier,
                })

    @http.route(['/chantiersnew'], type='http', auth="user", website=True)
    def chantiers_nvx(self, product_id=None):
        user = request.env.user
        cr, uid, context = reqst.cr, reqst.uid, reqst.context

        fiche_chantier = request.env['fiche.chantier'].sudo().search([])


        _logger.info("Generated fiche_chantierRRRRRRRRRRRRRRRRRRRRRRRRRRRRRR : " + str(fiche_chantier))
        form = [1,2,3]
        return http.request.render('darb_puthod.newchantiers', {
            'chantiers': fiche_chantier,
            })


    @http.route(['/equiplist/chantier/<int:chantier_id>'], type='http', auth="user", website=True)
    def equiplist(self, chantier_id):
        user = request.env.user
        cr, uid, context = reqst.cr, reqst.uid, reqst.context

        equipe_ids = request.env['equipe'].sudo().search([])


        _logger.info("Generated fiche_chantierRRRRRRRRRRRRRRRRRRRRRRRRRRRRRR : " + str(equipe_ids))
        form = [1,2,3]
        return http.request.render('darb_puthod.listequipes', {
                    'equipes': equipe_ids,
                    'chantier_id': chantier_id,
                })

    @http.route(['/equiplist/chantier/<int:chantier_id>/<int:equipe_id>'], type='http', auth="user", website=True)
    def createfiche(self, chantier_id, equipe_id):
        user = request.env.user
        cr, uid, context = reqst.cr, reqst.uid, reqst.context

        equipe_id = request.env['equipe'].sudo().search([('id','=',equipe_id)])
        chantier_id = request.env['equipe'].sudo().search([('id','=',chantier_id)])
        vals = {
            'equipe_id': equipe_id.id,
            'chantier_id': chantier_id.id,
            'inter_date': fields.Datetime.now(),
            }
        fiche_chantier = request.env['fiche.chantier'].create(vals)
        _logger.info("Generated fiche_chantierRRRRRRRRRRRRRRRRRRRRRRRRRRRRRR : " + str(equipe_id))
        form = [1,2,3]

        return http.request.render('darb_puthod.formchantiers', {
                    'chantiers': fiche_chantier,
                })

    @http.route(['/equipes'], type='http', auth="user", website=True)
    def equipes_nvx(self, product_id=None):
        user = request.env.user
        cr, uid, context = reqst.cr, reqst.uid, reqst.context

        employees = request.env['hr.employee'].sudo().search(['|', ('equipe_id','=',False), ('equipe_id.active','=',False)])


        _logger.info("Generated fiche_chantierRRRRRRRRRRRRRRRRRRRRRRRRRRRRRR : " + str(employees))
        return http.request.render('darb_puthod.newequipes', {
            'employees': employees,
            'equipe': 0,
            })

    @http.route(['/equipes/<int:equipe_id>/<int:employee_id>'], type='http', auth="user", website=True)
    def createequip(self, equipe_id, employee_id):
        user = request.env.user
        cr, uid, context = reqst.cr, reqst.uid, reqst.context
        _logger.info("just idddddddddddddddddddddddd : " + str(equipe_id))

        equipe_id = request.env['equipe'].sudo().search([('id','=',equipe_id)])
        _logger.info("objjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjj : " + str(equipe_id))
        employee = request.env['hr.employee'].sudo().search([('id','=',employee_id)])
        current_employee = request.env['hr.employee'].sudo().search([('user_id', '=', uid)])
        _logger.info("employeeemployeeemployee : " + str(employee))
        if equipe_id:
            _logger.info("111111111111111111 : " + str(employee))
            employee.equipe_id = equipe_id.id
        else:
            manager_equipe_id = request.env['equipe'].sudo().search([('manager','in',current_employee.ids), ('active','=',True)])
            manager_equipe_id.active = False
            _logger.info("222222222222222222 : " + str(employee))
            vals = {
                'name': 'Equipe',
                'manager': current_employee[0].id if current_employee else 1,
                'ressource_list': [(4, employee_id)],
                'active': True
                }
            equipe_id = request.env['equipe'].create(vals)
        _logger.info("Generated fiche_chantierRRRRRRRRRRRRRRRRRRRRRRRRRRRRRR : " + str(equipe_id))
        form = [1,2,3]

        employees = request.env['hr.employee'].sudo().search(['|', ('equipe_id','=',False), ('equipe_id.active','=',False)])
        _logger.info("Generated fiche_chantierlasttttttttttttttttttttttttttt: " + str(employees))

        return http.request.render('darb_puthod.newequipes', {
            'employees': employees,
            'equipe': equipe_id.id,
                })
