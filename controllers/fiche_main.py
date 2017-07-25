# -*- coding: utf-8 -*-
from openerp import http,  SUPERUSER_ID
from openerp.addons.website_project_issue.controllers.main import website_account
from openerp.http import request
from openerp.addons.web.http import request as reqst
from openerp import fields, models, api, _
from datetime import datetime
import logging
_logger = logging.getLogger(__name__)


class WebsiteContractDarbtech(http.Controller):

    @http.route(['/addvehicles'], type='json', auth="user", website=True)
    def addvehicles(self, fiche, vehicle, km):
        user = request.env.user
        cr, uid, context = request.cr, request.uid, request.context
        _logger.info("POINTER user = " + str(uid))
        fiche_id = request.env['fiche.chantier'].sudo().search([('id', '=', fiche)])
        error_message = ""
        vehicle_name = ""
        if vehicle:
            vehicle_name = request.env['product.product'].sudo().search([('id','=', int(vehicle))]).name
            fiche_id.veicule_ids = [(0, 0, {
                                    'vehicle_id': int(vehicle),
                                    'kms': km,
                                    })]
        else:
            error_message = _(u'Certains champs obligatoires sont vides.')
        return {
            'vehicle': vehicle_name,
            'km': km,
            'error_message': error_message
            }

    @http.route(['/addmateriel'], type='json', auth="user", website=True)
    def addmateriel(self, fiche, materiel, temps):
        user = request.env.user
        cr, uid, context = request.cr, request.uid, request.context
        _logger.info("POINTER user = " + str(uid))
        fiche_id = request.env['fiche.chantier'].sudo().search([('id', '=', fiche)])
        error_message = ""
        materiel_name = ""
        if materiel:
            materiel_name = request.env['product.product'].sudo().search([('id','=', int(materiel))]).name
            fiche_id.materiel_ids = [(0, 0, {
                                    'materiel_id': int(materiel),
                                    'temps': temps,
                                    })]
        else:
            error_message = _(u'Certains champs obligatoires sont vides.')
        return {
            'materiel': materiel_name,
            'temps': temps,
            'error_message': error_message
            }

    @http.route(['/addmachine'], type='json', auth="user", website=True)
    def addmachine(self, fiche, machine, temps):
        user = request.env.user
        cr, uid, context = request.cr, request.uid, request.context
        _logger.info("POINTER user = " + str(uid))
        fiche_id = request.env['fiche.chantier'].sudo().search([('id', '=', fiche)])
        error_message = ""
        machine_name = ""
        if machine:
            machine_name = request.env['product.product'].sudo().search([('id','=', int(machine))]).name
            fiche_id.materiel_ids = [(0, 0, {
                                    'materiel_id': int(machine),
                                    'temps': temps,
                                    })]
        else:
            error_message = _(u'Certains champs obligatoires sont vides.')
        return {
            'machine': machine_name,
            'temps': temps,
            'error_message': error_message
            }
