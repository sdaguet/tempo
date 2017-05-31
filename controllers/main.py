# -*- coding: utf-8 -*-
from openerp import http,  SUPERUSER_ID
from openerp.addons.website_project_issue.controllers.main import website_account
from openerp.http import request
from openerp.addons.web.http import request as reqst
import logging
_logger = logging.getLogger(__name__)

# class DarbtechSupportContract(http.Controller):
#     @http.route('/darbtech_support_contract/darbtech_support_contract/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/darbtech_support_contract/darbtech_support_contract/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('darbtech_support_contract.listing', {
#             'root': '/darbtech_support_contract/darbtech_support_contract',
#             'objects': http.request.env['darbtech_support_contract.darbtech_support_contract'].search([]),
#         })

#     @http.route('/darbtech_support_contract/darbtech_support_contract/objects/<model("darbtech_support_contract.darbtech_support_contract"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('darbtech_support_contract.object', {
#             'object': obj
#         })

class WebsiteContractDarbtech(http.Controller):

    @http.route(['/my/contracts/<int:product_id>'], type='http', auth="user", website=True)
    def product_followup(self, product_id=None):
        user = request.env.user
        cr, uid, context = reqst.cr, reqst.uid, reqst.context

        product_id_lines = reqst.registry['darbtech_support_contract.client.product.contract.details'].search(cr, SUPERUSER_ID, [
            ('partner_id', 'in', [user.partner_id.id]),
            ('product_id', 'in', [product_id])
        ], context=context)
        _logger.info("Contracts Details product_id_lines : " + str(product_id_lines))
        darbtech_issue_lst = reqst.registry['project.issue'].search(cr, SUPERUSER_ID, [
                ('partner_id', 'in', [user.partner_id.id])
            ], context=context)
        _logger.info("Contracts Details darbtech_issue_lst : " + str(darbtech_issue_lst))
        darbtech_task_lst = reqst.registry['project.task'].search(cr, SUPERUSER_ID, [
                ('partner_id', 'in', [user.partner_id.id])
            ], context=context)
        _logger.info("Contracts Details darbtech_task_lst : " + str(darbtech_task_lst))

        darbtech_issues =  reqst.registry['project.issue'].browse(cr, SUPERUSER_ID, darbtech_issue_lst, context=context)
        _logger.info("Contracts Issues : " + str(darbtech_issues))
        darbtech_tasks = reqst.registry['project.task'].browse(cr, SUPERUSER_ID, darbtech_task_lst, context=context)
        _logger.info("Contracts Tasks : " + str(darbtech_tasks))
        darbtech_product_details =  reqst.registry['darbtech_support_contract.client.product.contract.details'].browse(cr, SUPERUSER_ID, product_id_lines, context=context)
        _logger.info("Contracts Details darbtech_product_details: " + str(darbtech_product_details))
        product_details =  reqst.registry['product.product'].browse(cr, SUPERUSER_ID, [product_id], context=context)
        _logger.info("Contracts Details : " + str(darbtech_product_details))


        return http.request.render('darbtech_support_contract.product_followup', {
                    'contractlst': darbtech_product_details,
                    'prodct': product_details,
                    'dt_tasks': darbtech_tasks,
                    'dt_issues': darbtech_issues,
                })

class WebsiteAccount(website_account):
    @http.route(['/my', '/my/home'], type='http', auth="user", website=True)
    def account(self):
        _logger.info("WebsiteAccount : Start")
        response = super(WebsiteAccount, self).account()
        _logger.info("WebsiteAccount : Super => Call")
        user = request.env.user
        _logger.info("WebsiteAccount : User => Get info (request.env)")
        cr, uid, context = reqst.cr, reqst.uid, reqst.context
        _logger.info("WebsiteAccount : User => Get info (cr, uid,...)")

        if user.partner_id.customer == True:
            _logger.info("WebsiteAccount : User => is consumer")
            # Load Darbtech Categories
            darbtech_categ_lst = reqst.registry['product.category'].search(cr, SUPERUSER_ID, [
                ('name', 'in', ['Darbtech Service']),
            ], context=context)
            _logger.info("Categories : " + str(darbtech_categ_lst))

            # Load contracts of these categories
            # TODO : Corriger les droits sur cette vue. Pour l'instant ils sont court-circuités.
            darbtech_contracts_lst = reqst.registry['client.product.contract'].search(cr, SUPERUSER_ID, [
                ('partner_id', 'in', [user.partner_id.id])
            ], context=context)

            _logger.info("Partener ID : " + str(user.partner_id.id))

            darbtech_contracts =  reqst.registry['client.product.contract'].browse(cr, SUPERUSER_ID, darbtech_contracts_lst, context=context)
            _logger.info("Contracts : " + str(darbtech_contracts[0].product_uom_qty))

        else:
            _logger.info("WebsiteAccount : User => is NOT consumer")
            darbtech_contracts = False
            darbtech_tasks = False
            darbtech_issues = False
        response.qcontext.update({
            'contracts': darbtech_contracts
        })
        return response





class QueryURL(object):
    def __init__(self, path='', **args):
        self.path = path
        self.args = args

    def __call__(self, path=None, **kw):
        if not path:
            path = self.path
        for k,v in self.args.items():
            kw.setdefault(k,v)
        l = []
        for k,v in kw.items():
            if v:
                if isinstance(v, list) or isinstance(v, set):
                    l.append(werkzeug.url_encode([(k,i) for i in v]))
                else:
                    l.append(werkzeug.url_encode([(k,v)]))
        if l:
            path += '?' + '&'.join(l)
        return path
