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
            new_id = fiche_id.veicule_ids.ids[-1]
        else:
            error_message = _(u'Certains champs obligatoires sont vides.')
        return {
            'vehicle': vehicle_name,
            'fiche_veicule_id': new_id,
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
            new_id = fiche_id.materiel_ids.ids[-1]
        else:
            error_message = _(u'Certains champs obligatoires sont vides.')
        return {
            'materiel': materiel_name,
            'fiche_materiel_id': new_id,
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
            fiche_id.machine_ids = [(0, 0, {
                                    'machine_id': int(machine),
                                    'temps': temps,
                                    })]
            new_id = fiche_id.machine_ids.ids[-1]
        else:
            error_message = _(u'Certains champs obligatoires sont vides.')
        return {
            'machine': machine_name,
            'fiche_machine_id': new_id,
            'temps': temps,
            'error_message': error_message
            }


    @http.route(['/addfourniture'], type='json', auth="user", website=True)
    def addfourniture(self, fiche, fourniture, qty):
        user = request.env.user
        cr, uid, context = request.cr, request.uid, request.context
        _logger.info("POINTER user = " + str(uid))
        fiche_id = request.env['fiche.chantier'].sudo().search([('id', '=', fiche)])
        error_message = ""
        fourniture_name = ""
        if fourniture:
            fourniture_name = request.env['product.product'].sudo().search([('id','=', int(fourniture))]).name
            fiche_id.fourniture_ids = [(0, 0, {
                                    'fourniture_id': int(fourniture),
                                    'quantity': qty,
                                    })]
            new_id = fiche_id.fourniture_ids.ids[-1]
        else:
            error_message = _(u'Certains champs obligatoires sont vides.')
        return {
            'fourniture': fourniture_name,
            'fiche_fourniture_id': new_id,
            'qty': qty,
            'error_message': error_message
            }


    @http.route(['/addkit'], type='json', auth="user", website=True)
    def addkit(self, fiche, kit, qty):
        user = request.env.user
        cr, uid, context = request.cr, request.uid, request.context
        _logger.info("POINTER user = " + str(uid))
        fiche_id = request.env['fiche.chantier'].sudo().search([('id', '=', fiche)])
        error_message = ""
        kit_name = ""
        if kit:
            kit_name = request.env['product.product'].sudo().search([('id','=', int(kit))]).name
            fiche_id.kit_ids = [(0, 0, {
                                    'kit_id': int(kit),
                                    'quantity': qty,
                                    })]
            new_id = fiche_id.kit_ids.ids[-1]
        else:
            error_message = _(u'Certains champs obligatoires sont vides.')
        return {
            'kit': kit_name,
            'fiche_kit_id': new_id,
            'qty': qty,
            'error_message': error_message
            }


    @http.route(['/addtuteurage'], type='json', auth="user", website=True)
    def addtuteurage(self, fiche, tuteurage, qty):
        user = request.env.user
        cr, uid, context = request.cr, request.uid, request.context
        _logger.info("POINTER user = " + str(uid))
        fiche_id = request.env['fiche.chantier'].sudo().search([('id', '=', fiche)])
        error_message = ""
        tuteurage_name = ""
        if tuteurage:
            tuteurage_name = request.env['product.product'].sudo().search([('id','=', int(tuteurage))]).name
            fiche_id.tuteurage_ids = [(0, 0, {
                                    'tuteurage_id': int(tuteurage),
                                    'quantity': qty,
                                    })]
            new_id = fiche_id.tuteurage_ids.ids[-1]
        else:
            error_message = _(u'Certains champs obligatoires sont vides.')
        return {
            'tuteurage': tuteurage_name,
            'fiche_tuteurage_id': new_id,
            'qty': qty,
            'error_message': error_message
            }


    @http.route(['/addvigitaux'], type='json', auth="user", website=True)
    def addvigitaux(self, fiche, date, vigitaux, comment):
        user = request.env.user
        cr, uid, context = request.cr, request.uid, request.context
        _logger.info("POINTER user = " + str(uid))
        fiche_id = request.env['fiche.chantier'].sudo().search([('id', '=', fiche)])
        error_message = ""
        vigitaux_name = ""
        if vigitaux:
            vigitaux_name = request.env['product.product'].sudo().search([('id','=', int(vigitaux))]).name
            fiche_id.vigitaux_ids = [(0, 0, {
                                    'date': date,
                                    'vigitaux_id': int(vigitaux),
                                    'commentaire': comment,
                                    })]
            new_id = fiche_id.vigitaux_ids.ids[-1]
        else:
            error_message = _(u'Certains champs obligatoires sont vides.')
        return {
            'vigitaux': vigitaux_name,
            'fiche_vigitaux_id': new_id,
            'date': date,
            'comment': comment,
            'error_message': error_message
            }


    @http.route(['/addengrai'], type='json', auth="user", website=True)
    def addengrai(self, fiche, engrais, qty):
        user = request.env.user
        cr, uid, context = request.cr, request.uid, request.context
        _logger.info("POINTER user = " + str(uid))
        fiche_id = request.env['fiche.chantier'].sudo().search([('id', '=', fiche)])
        error_message = ""
        engrais_name = ""
        if engrais:
            engrais_name = request.env['product.product'].sudo().search([('id','=', int(engrais))]).name
            fiche_id.engrais_ids = [(0, 0, {
                                    'engrais_id': int(engrais),
                                    'quantity': qty,
                                    })]
            new_id = fiche_id.engrais_ids.ids[-1]
        else:
            error_message = _(u'Certains champs obligatoires sont vides.')
        return {
            'engrais': engrais_name,
            'fiche_engrais_id': new_id,
            'qty': qty,
            'error_message': error_message
            }


    @http.route(['/addgazon'], type='json', auth="user", website=True)
    def addgazon(self, fiche, gazons, qty):
        user = request.env.user
        cr, uid, context = request.cr, request.uid, request.context
        _logger.info("POINTER user = " + str(uid))
        fiche_id = request.env['fiche.chantier'].sudo().search([('id', '=', fiche)])
        error_message = ""
        gazons_name = ""
        if gazons:
            gazons_name = request.env['product.product'].sudo().search([('id','=', int(gazons))]).name
            fiche_id.gazons_ids = [(0, 0, {
                                    'gazons_id': int(gazons),
                                    'quantity': qty,
                                    })]
            new_id = fiche_id.gazons_ids.ids[-1]
        else:
            error_message = _(u'Certains champs obligatoires sont vides.')
        return {
            'gazons': gazons_name,
            'fiche_gazons_id': new_id,
            'qty': qty,
            'error_message': error_message
            }


    @http.route(['/addgmateriel'], type='json', auth="user", website=True)
    def addgmateriel(self, fiche, gmateriel, qty):
        user = request.env.user
        cr, uid, context = request.cr, request.uid, request.context
        _logger.info("POINTER user = " + str(uid))
        fiche_id = request.env['fiche.chantier'].sudo().search([('id', '=', fiche)])
        error_message = ""
        gmateriel_name = ""
        if gmateriel:
            gmateriel_name = request.env['product.product'].sudo().search([('id','=', int(gmateriel))]).name
            fiche_id.gmateriel_ids = [(0, 0, {
                                    'gmateriel_id': int(gmateriel),
                                    'quantity': qty,
                                    })]
            new_id = fiche_id.gmateriel_ids.ids[-1]
        else:
            error_message = _(u'Certains champs obligatoires sont vides.')
        return {
            'gmateriel': gmateriel_name,
            'fiche_gmateriel_id': new_id,
            'qty': qty,
            'error_message': error_message
            }


    @http.route(['/addescalier'], type='json', auth="user", website=True)
    def addescalier(self, fiche, escalier, qty):
        user = request.env.user
        cr, uid, context = request.cr, request.uid, request.context
        _logger.info("POINTER user = " + str(uid))
        fiche_id = request.env['fiche.chantier'].sudo().search([('id', '=', fiche)])
        error_message = ""
        escalier_name = ""
        if escalier:
            escalier_name = request.env['product.product'].sudo().search([('id','=', int(escalier))]).name
            fiche_id.escalier_ids = [(0, 0, {
                                    'gazons_id': int(escalier),
                                    'quantity': qty,
                                    })]
            new_id = fiche_id.escalier_ids.ids[-1]
        else:
            error_message = _(u'Certains champs obligatoires sont vides.')
        return {
            'escalier': escalier_name,
            'fiche_escalier_id': new_id,
            'qty': qty,
            'error_message': error_message
            }


    @http.route(['/addoutils'], type='json', auth="user", website=True)
    def addoutils(self, fiche, outils, qty):
        user = request.env.user
        cr, uid, context = request.cr, request.uid, request.context
        _logger.info("POINTER user = " + str(uid))
        fiche_id = request.env['fiche.chantier'].sudo().search([('id', '=', fiche)])
        error_message = ""
        outils_name = ""
        if outils:
            outils_name = request.env['product.product'].sudo().search([('id','=', int(outils))]).name
            fiche_id.outils_ids = [(0, 0, {
                                    'outils_id': int(outils),
                                    'quantity': qty,
                                    })]
            new_id = fiche_id.outils_ids.ids[-1]
        else:
            error_message = _(u'Certains champs obligatoires sont vides.')
        return {
            'outils': outils_name,
            'fiche_outils_id': new_id,
            'qty': qty,
            'error_message': error_message
            }


    @http.route(['/addclotures'], type='json', auth="user", website=True)
    def addclotures(self, fiche, cloture, qty):
        user = request.env.user
        cr, uid, context = request.cr, request.uid, request.context
        _logger.info("POINTER user = " + str(uid))
        fiche_id = request.env['fiche.chantier'].sudo().search([('id', '=', fiche)])
        error_message = ""
        cloture_name = ""
        if cloture:
            cloture_name = request.env['product.product'].sudo().search([('id','=', int(cloture))]).name
            fiche_id.cloture_ids = [(0, 0, {
                                    'cloture_id': int(cloture),
                                    'quantity': qty,
                                    })]
            new_id = fiche_id.cloture_ids.ids[-1]
        else:
            error_message = _(u'Certains champs obligatoires sont vides.')
        return {
            'cloture': cloture_name,
            'fiche_cloture_id': new_id,
            'qty': qty,
            'error_message': error_message
            }


    @http.route(['/adddivers'], type='json', auth="user", website=True)
    def adddivers(self, fiche, divers, qty):
        user = request.env.user
        cr, uid, context = request.cr, request.uid, request.context
        _logger.info("POINTER user = " + str(uid))
        fiche_id = request.env['fiche.chantier'].sudo().search([('id', '=', fiche)])
        error_message = ""
        divers_name = ""
        if divers:
            divers_name = request.env['product.product'].sudo().search([('id','=', int(divers))]).name
            fiche_id.divers_ids = [(0, 0, {
                                    'divers_id': int(divers),
                                    'quantity': qty,
                                    })]
            new_id = fiche_id.divers_ids.ids[-1]
        else:
            error_message = _(u'Certains champs obligatoires sont vides.')
        return {
            'divers': divers_name,
            'fiche_divers_id': new_id,
            'qty': qty,
            'error_message': error_message
            }


    @http.route(['/addterrasses'], type='json', auth="user", website=True)
    def addterrasses(self, fiche, terrasse, qty):
        user = request.env.user
        cr, uid, context = request.cr, request.uid, request.context
        _logger.info("POINTER user = " + str(uid))
        fiche_id = request.env['fiche.chantier'].sudo().search([('id', '=', fiche)])
        error_message = ""
        terrasse_name = ""
        if terrasse:
            terrasse_name = request.env['product.product'].sudo().search([('id','=', int(terrasse))]).name
            fiche_id.terrasse_ids = [(0, 0, {
                                    'terrasse_id': int(terrasse),
                                    'quantity': qty,
                                    })]
            new_id = fiche_id.terrasse_ids.ids[-1]
        else:
            error_message = _(u'Certains champs obligatoires sont vides.')
        return {
            'terrasse': terrasse_name,
            'fiche_terrasse_id': new_id,
            'qty': qty,
            'error_message': error_message
            }


    @http.route(['/addsclotures'], type='json', auth="user", website=True)
    def addsclotures(self, fiche, scloture, qty):
        user = request.env.user
        cr, uid, context = request.cr, request.uid, request.context
        _logger.info("POINTER user = " + str(uid))
        fiche_id = request.env['fiche.chantier'].sudo().search([('id', '=', fiche)])
        error_message = ""
        scloture_name = ""
        if scloture:
            scloture_name = request.env['product.product'].sudo().search([('id','=', int(scloture))]).name
            fiche_id.scloture_ids = [(0, 0, {
                                        'scloture_id': int(scloture),
                                        'quantity': qty,
                                        })]
            new_id = fiche_id.scloture_ids.ids[-1]
        else:
            error_message = _(u'Certains champs obligatoires sont vides.')
        return {
            'scloture': scloture_name,
            'fiche_scloture_id': new_id,
            'qty': qty,
            'error_message': error_message
            }


    @http.route(['/addcomment'], type='json', auth="user", website=True)
    def addcomment(self, fiche, comment):
        user = request.env.user
        cr, uid, context = request.cr, request.uid, request.context
        _logger.info("POINTER comennnnnnnnnnnnnnnnt = " + str(uid))
        fiche_id = request.env['fiche.chantier'].sudo().search([('id', '=', fiche)])
        fiche_id.remarqs = comment
        return {
            'comment': comment,
            }


    @http.route(['/addwork'], type='json', auth="user", website=True)
    def addwork(self, fiche, employee, tesk, type, heure_deb, heure_fin):
        user = request.env.user
        cr, uid, context = request.cr, request.uid, request.context
        _logger.info("POINTER WORKKKKKKKKKKKKKKKKKKKKKKKKKKK = " + str(uid))
        fiche_id = request.env['fiche.chantier'].sudo().search([('id', '=', fiche)])
        error_message = ""
        item_ids = request.env['employees.subtasks'].sudo().search([('employee', '=', int(employee)), ('fiche_chantier_subtask_id.fiche_chantier_id', '=', int(fiche))])
        dd = datetime.strptime(heure_deb,'%H:%M')
        df = datetime.strptime(heure_fin,'%H:%M')
        #Check time : Start < End 
        if dd > df:
            error_message = _(u"Heure début > Heure fin !")
            _logger.info("POINTER 11111111111111111111111 = ")
        #Check intersections between time
        for item in item_ids:
            idd = datetime.strptime(item.heure_deb,'%H:%M')
            idf = datetime.strptime(item.heure_fin,'%H:%M')
            if (df > idd and df < idf) or (dd > idd and dd < idf) or (dd > idd and df < idf) or (dd < idd and df > idf):
                error_message = _(u"Intersection entre plages horaires !")
                _logger.info("POINTER 2222222222222222222222 = ")
        #/Check intersections between time
        if error_message == "":
            vals = {
                    'employee': employee,
                    'heure_deb': heure_deb,
                    'heure_fin': heure_fin,
                    'type': type,
                    'fiche_chantier_subtask_id': tesk
                    }
            request.env['employees.subtasks'].sudo().create(vals)
        _logger.info("POINTER WORKKKKKKKKKKKKKKKKKKKKKKKKKKK = ")
        return {
            'error_message': error_message
            }