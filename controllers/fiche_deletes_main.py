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
        _logger.info("POINTER user = " + str(uid))
        fiche_id = request.env['fiche.chantier'].sudo().search([('id', '=', fiche)])
        return {
            }
