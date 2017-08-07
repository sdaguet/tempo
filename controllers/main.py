# -*- coding: utf-8 -*-
from openerp import http,  SUPERUSER_ID
from openerp.addons.website_project_issue.controllers.main import website_account
from openerp.http import request
from openerp.addons.web.http import request as reqst
from openerp import fields, models, api, _
from datetime import datetime, date
import time
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
        _logger.info("Current teams = " + str(list_teams))

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

    @http.route('/testajax', type='http', auth="user", website=True)
    def testajax(self, **kw):
        user = request.env.user
        cr, uid, context = request.cr, request.uid, request.context
        employes = request.registry.get('hr.employee')
        _logger.info("POINTER user = " + str(uid))

        return http.request.render('darb_puthod.testajax', {
                })

    @http.route(['/ajaxi'], type='json', auth="user", website=True)
    def ajaxi(self, fiche):
        user = request.env.user
        cr, uid, context = request.cr, request.uid, request.context
        employes = request.env['emplacement'].create({'name': fiche})
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

        return http.request.render('darb_puthod.listfiches', {
                    'fiches': fiche,
                })

    # fiche info

    @http.route(['/ficheslist/<int:fiche>/'], type='http', auth="user", website=True)
    def showfiche(self, fiche):
        user = request.env.user
        cr, uid, context = reqst.cr, reqst.uid, reqst.context

        fiche_id = request.env['fiche.chantier'].sudo().search([('id', '=', fiche)])
        list_teams = request.env['fiche.chantier'].sudo().search([('id', '=', fiche)]).equipe_id
        members = list_teams.ressource_list.ids
        members.append(list_teams.manager.id)
        members_employee = request.env['hr.employee'].sudo().search([('id', 'in', members)])
        vehicles = request.env['product.product'].sudo().search([('categ_id','=', request.env.ref('darb_puthod.product_category_vehicle').id)])
        materiels = request.env['product.product'].sudo().search([('categ_id','=', request.env.ref('darb_puthod.product_category_materiel').id)])
        machines = request.env['product.product'].sudo().search([('categ_id','=', request.env.ref('darb_puthod.product_category_machine').id)])
        fournitures = request.env['product.product'].sudo().search([('categ_id','=', request.env.ref('darb_puthod.product_category_fourniture').id)])
        kits = request.env['product.product'].sudo().search([('categ_id','=', request.env.ref('darb_puthod.product_category_kit').id)])
        tuteurage = request.env['product.product'].sudo().search([('categ_id','=', request.env.ref('darb_puthod.product_category_tuteurage').id)])
        vigitaux = request.env['product.product'].sudo().search([('categ_id','=', request.env.ref('darb_puthod.product_category_vigitaux').id)])
        gazons = request.env['product.product'].sudo().search([('categ_id','=', request.env.ref('darb_puthod.product_category_gazons').id)])
        engrais = request.env['product.product'].sudo().search([('categ_id','=', request.env.ref('darb_puthod.product_category_engrais').id)])
        gmateriel = request.env['product.product'].sudo().search([('categ_id','=', request.env.ref('darb_puthod.product_category_gmateriel').id)])
        escalier = request.env['product.product'].sudo().search([('categ_id','=', request.env.ref('darb_puthod.product_category_escalier').id)])
        outils = request.env['product.product'].sudo().search([('categ_id','=', request.env.ref('darb_puthod.product_category_outils').id)])
        cloture = request.env['product.product'].sudo().search([('categ_id','=', request.env.ref('darb_puthod.product_category_cloture').id)])
        divers = request.env['product.product'].sudo().search([('categ_id','=', request.env.ref('darb_puthod.product_category_divers').id)])
        terrasse = request.env['product.product'].sudo().search([('categ_id','=', request.env.ref('darb_puthod.product_category_terrasse').id)])
        tasks = fiche_id.subtasks

        return http.request.render('darb_puthod.ficheviewer', {
            'teams': members_employee,
            'fiche': fiche_id,
            'vehicles': vehicles,
            'materiels': materiels,
            'machines': machines,
            'fournitures': fournitures,
            'kits': kits,
            'tuteurages': tuteurage,
            'vigitaux_list': vigitaux,
            'gazons': gazons,
            'engrais': engrais,
            'gmateriels': gmateriel,
            'escaliers': escalier,
            'outils': outils,
            'clotures': cloture,
            'divers': divers,
            'terrasses': terrasse,
            'tasks': tasks,
        })

    @http.route('/ficheviewer', type='json', auth="user", website=True)
    def ficheviewer(self, **kw):
        user = request.env.user
        cr, uid, context = request.cr, request.uid, request.context
        fiche = request.registry.get('fiche.chantier')
        return {}

    @http.route('/getgantt', type='json', auth="user", website=True)
    def ganttdatas(self, fiche):
        gantclasses = ["ganttRed","ganttGreen","ganttOrange"]
        i=0
        tailleGantClasses=len(gantclasses)

        user = request.env.user
        cr, uid, context = request.cr, request.uid, request.context
        list_teams = request.env['fiche.chantier'].sudo().search([('id', '=', int(fiche))]).equipe_id
        _logger.info("Ramene mon gantt data = ")
        members = list_teams.ressource_list.ids
        members.append(list_teams.manager.id)
        members_employee = request.env['hr.employee'].sudo().search([('id', 'in', members)])

        rezult = []

        for mbr in members_employee:
            elmt = {
                'name': mbr.name,
                'desc': "",
                'values': []
            }

            item_ids = request.env['employees.subtasks'].sudo().search([('employee', '=', int(mbr.id)), ('fiche_chantier_subtask_id.fiche_chantier_id', '=', int(fiche))])
            for itm in item_ids:
                hdeb = itm.heure_deb
                hfin = itm.heure_fin
                if len(hfin) == 4 : hfin = '0' + hfin
                if len(hdeb) == 4 : hdeb = '0' + hdeb
                hdebtime = datetime.strptime(hdeb,'%H:%M').time()
                debdatetime = datetime.combine(date.today(), hdebtime)

                hfintime = datetime.strptime(hfin,'%H:%M').time()
                findatetime = datetime.combine(date.today(), hfintime)
                deb_timestamp = time.mktime(debdatetime.timetuple()) * 1000
                _logger.info("Generated DDDDDDDDDDDDDDDDDDDDDDDDDDDDDDD: " + str(hdeb))
                _logger.info("Generated FFFFFFFFFFFFFFFFFFFFFFFFFFFFFFF: " + str(hfin))
                fin_timestamp = time.mktime(findatetime.timetuple()) * 1000
                elmt['values'].append({
                    'from' : deb_timestamp,
                    'to' : fin_timestamp,
                    'label' : itm.fiche_chantier_subtask_id.subtask_id.name,
                    'customClass' : gantclasses[i],
                })
                i=(i+1)%tailleGantClasses
            rezult.append(elmt)
        return rezult


    @http.route(['/chantierslist'], type='http', auth="user", website=True)
    def chantiers_liste(self, product_id=None):
        user = request.env.user
        cr, uid, context = reqst.cr, reqst.uid, reqst.context

        fiche_chantier = request.env['fiche.chantier'].sudo().search([])

        return http.request.render('darb_puthod.listchantiers', {
                    'chantiers': fiche_chantier,
                })

    @http.route(['/chantiersForm'], type='http', auth="user", website=True)
    def chantiers_form(self, product_id=None):
        user = request.env.user
        cr, uid, context = reqst.cr, reqst.uid, reqst.context

        fiche_chantier = request.env['fiche.chantier'].sudo().search([])

        form = [1,2,3]
        return http.request.render('darb_puthod.formchantiers', {
                    'chantiers': fiche_chantier,
                })

    @http.route(['/chantiersnew'], type='http', auth="user", website=True)
    def chantiers_nvx(self, product_id=None):
        user = request.env.user
        cr, uid, context = reqst.cr, reqst.uid, reqst.context

        fiche_chantier = request.env['fiche.chantier'].sudo().search([])

        form = [1,2,3]
        return http.request.render('darb_puthod.newchantiers', {
            'chantiers': fiche_chantier,
            })


    @http.route(['/equiplist/chantier/<int:chantier_id>'], type='http', auth="user", website=True)
    def equiplist(self, chantier_id):
        user = request.env.user
        cr, uid, context = reqst.cr, reqst.uid, reqst.context

        equipe_ids = request.env['equipe'].sudo().search([])

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
            'inter_date': fields.Date.today(),
            }
        fiche_chantier = request.env['fiche.chantier'].create(vals)
        form = [1,2,3]

        return http.request.render('darb_puthod.formchantiers', {
                    'chantiers': fiche_chantier,
                })

    @http.route(['/equipes'], type='http', auth="user", website=True)
    def equipes_nvx(self, product_id=None):
        user = request.env.user
        cr, uid, context = reqst.cr, reqst.uid, reqst.context

        employees = request.env['hr.employee'].sudo().search(['|', ('equipe_id','=',False), ('equipe_id.active','=',False)])

        return http.request.render('darb_puthod.newequipes', {
            'employees': employees,
            'equipe': 0,
            })

    @http.route(['/equipes/<int:equipe_id>/<int:employee_id>'], type='http', auth="user", website=True)
    def createequip(self, equipe_id, employee_id):
        user = request.env.user
        cr, uid, context = reqst.cr, reqst.uid, reqst.context

        equipe_id = request.env['equipe'].sudo().search([('id','=',equipe_id)])
        employee = request.env['hr.employee'].sudo().search([('id','=',employee_id)])
        current_employee = request.env['hr.employee'].sudo().search([('user_id', '=', uid)])
        if equipe_id:
            employee.equipe_id = equipe_id.id
        else:
            manager_equipe_id = request.env['equipe'].sudo().search([('manager','in',current_employee.ids), ('active','=',True)])
            if manager_equipe_id: manager_equipe_id.active = False
            vals = {
                'manager': current_employee[0].id if current_employee else 1,
                'ressource_list': [(4, employee_id)],
                'active': True
                }
            equipe_id = request.env['equipe'].create(vals)
        form = [1,2,3]

        employees = request.env['hr.employee'].sudo().search(['|', ('equipe_id','=',False), ('equipe_id.active','=',False)])

        return http.request.render('darb_puthod.newequipes', {
            'employees': employees,
            'equipe': equipe_id.id,
                })
