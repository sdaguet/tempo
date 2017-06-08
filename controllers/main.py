# -*- coding: utf-8 -*-
from openerp import http,  SUPERUSER_ID
from openerp.addons.website_project_issue.controllers.main import website_account
from openerp.http import request
from openerp.addons.web.http import request as reqst
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
                    ('manager', '=', current_employee.id)
                ])
        
        return http.request.render('darb_puthod.pointages', {
            'teams' : list_teams
                })
                
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