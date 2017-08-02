#!/usr/bin/python
# coding: utf8
from openerp import fields, models, api, _
from openerp.exceptions import ValidationError
from datetime import datetime
# from dateutil.relativedelta import relativedelta
# from openerp.tools import DEFAULT_SERVER_DATE_FORMAT, DEFAULT_SERVER_DATETIME_FORMAT
import logging
class puthod_partner(models.Model):
    _inherit = 'res.partner'

    N_Client_id = fields.Many2one(comodel_name="tmpclient", string="N° Client", required=False)
    N_Client_comp_id = fields.Many2one(comodel_name="tmpclient", string="N° Client", required=False,
                                       compute='_compute_Client')
    importe = fields.Boolean(string="importe",default = False)


    @api.multi
    def unlink(self):
        for s in self:
            if s.N_Client_id:
                self.N_Client_id.unlink()
                return super(puthod_partner, s).unlink()

    @api.multi
    @api.depends('N_Client_id', 'N_Client_id.Nom_1', 'N_Client_id.Nom_2', 'N_Client_id.Ville',
                 'N_Client_id.Code_Postal', 'N_Client_id.E_mail', 'N_Client_id.URL', 'N_Client_id.Fax',
                 'N_Client_id.Telephone', 'N_Client_id.Portable', 'N_Client_id.Adresse_1', 'N_Client_id.Adresse_2')
    def _compute_Client(self):

        for s in self:
            if s.N_Client_id:
                Nom_1 = s.N_Client_id.Nom_1
                Nom_2 = s.N_Client_id.Nom_2
                Ville = s.N_Client_id.Ville
                Code_Postal = s.N_Client_id.Code_Postal
                E_mail = s.N_Client_id.E_mail
                URL = s.N_Client_id.URL
                Fax = s.N_Client_id.Fax
                Telephone = s.N_Client_id.Telephone
                Portable = s.N_Client_id.Portable
                Adresse_1 = s.N_Client_id.Adresse_1
                Adresse_2 = s.N_Client_id.Adresse_2

                s.street = Adresse_1,  # Adresse_1
                s.city = Ville
                s.zip = Code_Postal  # Code_Postal
                s.email = E_mail  # E_mail
                s.website = URL  # v
                s.fax = Fax  # FAX
                s.street2 = Adresse_2  # Adresse_2
                s.phone = Telephone
                s.name = str(Nom_1) + " " + str(Nom_2)  # nom
                s.mobile = Portable
