# -*- coding: utf-8 -*-
from openerp import http,  SUPERUSER_ID
from openerp.addons.website_project_issue.controllers.main import website_account
from openerp.http import request
from openerp.addons.web.http import request as reqst
from openerp import fields, models, api, _
from datetime import datetime
import logging
_logger = logging.getLogger(__name__)


class WebsiteFicheDeletes(http.Controller):

    @http.route(['/deletevehicles'], type='json', auth="user", website=True)
    def deletevehicles(self, fiche, fiche_veicule):
        user = request.env.user
        cr, uid, context = request.cr, request.uid, request.context
        fiche_id = request.env['fiche.chantier'].sudo().search([('id', '=', fiche)])
        fiche_id.veicule_ids = [(2, int(fiche_veicule))]
        return {
            }

    @http.route(['/deletemateriel'], type='json', auth="user", website=True)
    def deletemateriel(self, fiche, fiche_materiel):
        user = request.env.user
        cr, uid, context = request.cr, request.uid, request.context
        fiche_id = request.env['fiche.chantier'].sudo().search([('id', '=', fiche)])
        fiche_id.materiel_ids = [(2, int(fiche_materiel))]
        return {
            }

    @http.route(['/deletemachine'], type='json', auth="user", website=True)
    def deletemachine(self, fiche, fiche_machine):
        user = request.env.user
        cr, uid, context = request.cr, request.uid, request.context
        fiche_id = request.env['fiche.chantier'].sudo().search([('id', '=', fiche)])
        fiche_id.machine_ids = [(2, int(fiche_machine))]
        return {
            }

    @http.route(['/deletefourniture'], type='json', auth="user", website=True)
    def deletefourniture(self, fiche, fiche_fourniture):
        user = request.env.user
        cr, uid, context = request.cr, request.uid, request.context
        fiche_id = request.env['fiche.chantier'].sudo().search([('id', '=', fiche)])
        fiche_id.fourniture_ids = [(2, int(fiche_fourniture))]
        return {
            }

    @http.route(['/deletekit'], type='json', auth="user", website=True)
    def deletekit(self, fiche, fiche_kit):
        user = request.env.user
        cr, uid, context = request.cr, request.uid, request.context
        fiche_id = request.env['fiche.chantier'].sudo().search([('id', '=', fiche)])
        fiche_id.kit_ids = [(2, int(fiche_kit))]
        return {
            }

    @http.route(['/deletetuteurage'], type='json', auth="user", website=True)
    def deletetuteurage(self, fiche, fiche_tuteurage):
        user = request.env.user
        cr, uid, context = request.cr, request.uid, request.context
        fiche_id = request.env['fiche.chantier'].sudo().search([('id', '=', fiche)])
        fiche_id.tuteurage_ids = [(2, int(fiche_tuteurage))]
        return {
            }

    @http.route(['/deletevigitaux'], type='json', auth="user", website=True)
    def deletevigitaux(self, fiche, fiche_vigitaux):
        user = request.env.user
        cr, uid, context = request.cr, request.uid, request.context
        fiche_id = request.env['fiche.chantier'].sudo().search([('id', '=', fiche)])
        fiche_id.vigitaux_ids = [(2, int(fiche_vigitaux))]
        return {
            }

    @http.route(['/deleteengrai'], type='json', auth="user", website=True)
    def deleteengrai(self, fiche, fiche_engrai):
        user = request.env.user
        cr, uid, context = request.cr, request.uid, request.context
        fiche_id = request.env['fiche.chantier'].sudo().search([('id', '=', fiche)])
        fiche_id.engrais_ids = [(2, int(fiche_engrai))]
        return {
            }

    @http.route(['/deletegazon'], type='json', auth="user", website=True)
    def deletegazon(self, fiche, fiche_gazon):
        user = request.env.user
        cr, uid, context = request.cr, request.uid, request.context
        fiche_id = request.env['fiche.chantier'].sudo().search([('id', '=', fiche)])
        fiche_id.gazons_ids = [(2, int(fiche_gazon))]
        return {
            }

    @http.route(['/deletegmateriel'], type='json', auth="user", website=True)
    def deletegmateriel(self, fiche, fiche_gmaterie):
        user = request.env.user
        cr, uid, context = request.cr, request.uid, request.context
        fiche_id = request.env['fiche.chantier'].sudo().search([('id', '=', fiche)])
        fiche_id.gmateriel_ids = [(2, int(fiche_gmaterie))]
        return {
            }

    @http.route(['/deleteescalier'], type='json', auth="user", website=True)
    def deleteescalier(self, fiche, fiche_escalier):
        user = request.env.user
        cr, uid, context = request.cr, request.uid, request.context
        fiche_id = request.env['fiche.chantier'].sudo().search([('id', '=', fiche)])
        fiche_id.escalier_ids = [(2, int(fiche_escalier))]
        return {
            }

    @http.route(['/deleteoutilss'], type='json', auth="user", website=True)
    def deleteoutilss(self, fiche, fiche_outilss):
        user = request.env.user
        cr, uid, context = request.cr, request.uid, request.context
        fiche_id = request.env['fiche.chantier'].sudo().search([('id', '=', fiche)])
        fiche_id.outils_ids = [(2, int(fiche_outilss))]
        return {
            }

    @http.route(['/deletecloture'], type='json', auth="user", website=True)
    def deletecloture(self, fiche, fiche_cloture):
        user = request.env.user
        cr, uid, context = request.cr, request.uid, request.context
        fiche_id = request.env['fiche.chantier'].sudo().search([('id', '=', fiche)])
        fiche_id.cloture_ids = [(2, int(fiche_cloture))]
        return {
            }

    @http.route(['/deletediverss'], type='json', auth="user", website=True)
    def deletediverss(self, fiche, fiche_diverss):
        user = request.env.user
        cr, uid, context = request.cr, request.uid, request.context
        fiche_id = request.env['fiche.chantier'].sudo().search([('id', '=', fiche)])
        fiche_id.divers_ids = [(2, int(fiche_diverss))]
        return {
            }

    @http.route(['/deleteterrasse'], type='json', auth="user", website=True)
    def deleteterrasse(self, fiche, fiche_terrasse):
        user = request.env.user
        cr, uid, context = request.cr, request.uid, request.context
        fiche_id = request.env['fiche.chantier'].sudo().search([('id', '=', fiche)])
        fiche_id.terrasse_ids = [(2, int(fiche_terrasse))]
        return {
            }

    @http.route(['/deletescloture'], type='json', auth="user", website=True)
    def deletescloture(self, fiche, fiche_scloture):
        user = request.env.user
        cr, uid, context = request.cr, request.uid, request.context
        fiche_id = request.env['fiche.chantier'].sudo().search([('id', '=', fiche)])
        fiche_id.scloture_ids = [(2, int(fiche_scloture))]
        return {
            }

    @http.route(['/deletework'], type='json', auth="user", website=True)
    def deletework(self, fiche, fiche_subtask):
        user = request.env.user
        cr, uid, context = request.cr, request.uid, request.context
        fiche_id = request.env['fiche.chantier'].sudo().search([('id', '=', fiche)])
        request.env['employees.subtasks'].sudo().search([('id', '=', int(fiche_subtask))]).unlink()
        return {
            }
