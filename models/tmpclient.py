#!/usr/bin/python
# coding: utf8
from openerp import fields, models, api, _
import logging

_logger = logging.getLogger(__name__)


class TmpClient(models.Model):
    _name = 'tmpclient'
    _rec_name = 'N_Client'
    N_Client = fields.Char("N° Client")
    Civilite = fields.Char("Civilité")
    Nom_1 = fields.Char("Nom 1")
    Nom_2 = fields.Char("Nom 2")
    Rais_Soc = fields.Char("Rais. Soc.")
    Adresse_1 = fields.Char("Adresse (1)")
    Adresse_2 = fields.Char("Adresse (2)")
    Code_Postal = fields.Char("Code Postal")
    Ville = fields.Char("Ville")
    Pays = fields.Char("Pays")
    Telephone = fields.Char("Téléphone")
    Portable = fields.Char("Portable")
    Fax = fields.Char("Fax")
    E_mail = fields.Char("E-mail")
    URL = fields.Char("URL")
    Code_Categorie = fields.Char("Code Catégorie")
    Contfichier = fields.Char("Cont.fichier")
    Contfichier_bis = fields.Char("(Cont.fichier)")
    altitude_du_jardin = fields.Char("altitude du jardin")
    altitude_du_jardin_bis = fields.Char("(altitude du jardin)")
    surface_du_jardin = fields.Char("surface du jardin")
    surface_du_jardin_bis = fields.Char("(surface du jardin)")
    Critere_4 = fields.Char("Critère 4")
    Critere_4_bis = fields.Char("(Critère 4)")
    age_du_jardin = fields.Char("âge du jardin")
    age_du_jardin_bis = fields.Char("(âge du jardin)")
    type_de_client = fields.Char("type de client")
    type_de_client_bis = fields.Char("(type de client)")
    Code_Representant = fields.Char("Code Représentant")
    Code_Etiquette = fields.Char("Code Etiquette")
    Mode_de_Reglement = fields.Char("Mode de Règlement")
    Type_Classe = fields.Char("Type Classe")
    Taux_Remise_Lig = fields.Char("Taux Remise Lig.")
    Taux_Remise_Pied = fields.Char("Taux Remise Pied")
    Interdit = fields.Char("Interdit")
    Compte_Tiers = fields.Char("Compte Tiers")
    Date_Ent = fields.Char("Date Ent.")
    Date_Dern_Modif = fields.Char("Date Dern. Modif.")
    CA_N = fields.Char("CA N")
    CA_N_1 = fields.Char("CA N-1")
    CA_N_2 = fields.Char("CA N-2")
    Commentaire_client = fields.Char("Commentaire client")
    Identification_TVA = fields.Char("Identification TVA")
    Assurance = fields.Char("Assurance")
    Devise = fields.Char("Devise")
    Compte_Facture = fields.Char("Compte Facturé")
    Regroup_Facture = fields.Char("Regroup. Facture")
    Plafond = fields.Char("Plafond")
    Date_Dern_Modif_Plafond = fields.Char("Date Dern. Modif. Plafond")
    Objectif_CA = fields.Char("Objectif CA")
    Adresse_Exp = fields.Char("Adresse Exp.")
    Code_Postal_2 = fields.Char("Code Postal 2")
    Ville_2 = fields.Char("Ville_2")
    Pays_2 = fields.Char("Pays_2")
    Comment_Livraison = fields.Char("Comment. Livraison")
    Pays_ProvDest = fields.Char("Pays Prov./Dest.")
    Pays_d_origine = fields.Char("Pays d'origine")
    Port = fields.Char("Port")
    Code_Cond = fields.Char("Code Cond.")
    Nbre_Factures = fields.Char("Nbre Factures")
    Rempl_Taille = fields.Char("Rempl. Taille")
    Rempl_Variete = fields.Char("Rempl. Variété")
    Code_Pays_code_barre = fields.Char("Code Pays - code barre")
    Masquer_dans_les_listes = fields.Char("Masquer dans les listes")
    CNUF = fields.Char("CNUF")
    N_Ref = fields.Char("N° Réf.")
    Logo = fields.Char("Logo")
    N_Tarification = fields.Char("N° Tarification")
    Modele_Etiquette = fields.Char("Modèle Etiquette")
    Modele_de_Facture = fields.Char("Modèle de Facture")
    Code_Client = fields.Char("Code Client")
    type_de_plantation = fields.Char("type de plantation")
    type_d_entretien = fields.Char("type d'entretien")
    parrainage = fields.Char("parrainage")
    type_de_profil = fields.Char("type de profil")
    intermediaire = fields.Char("intermédiaire")
    Intermediaire_2 = fields.Char("Intermédiaire 2")
    NEWSLETTER = fields.Char("NEWSLETTER")
    Critere_14 = fields.Char("Critère 14")
    Critere_15 = fields.Char("Critère 15")
    Critere_16 = fields.Char("Critère 16")
    Critere_17 = fields.Char("Critère 17")
    Critere_18 = fields.Char("Critère 18")
    Nom_Livraison = fields.Char("Nom Livraison")
    Prenom_Livraison = fields.Char("Prénom Livraison")
    Ad_Liv_1 = fields.Char("Ad. Liv. 1")
    Ad_Liv_2 = fields.Char("Ad. Liv. 2")
    CP_Livraison = fields.Char("CP Livraison")
    Ville_Liv = fields.Char("Ville Liv.")
    Code_pays_Livraison = fields.Char("Code pays Livraison")
    Telephone_Livraison = fields.Char("Téléphone Livraison")
    Fax_Livraison = fields.Char("Fax Livraison")
    Portable_Livraison = fields.Char("Portable Livraison")
    E_mail_Livraison = fields.Char("E-mail Livraison")
    Commentaire_Livraison = fields.Char("Commentaire Livraison")
    Zone_Exp = fields.Char("Zone Exp.")
    Incoterm = fields.Char("Incoterm")
    Type_transport = fields.Char("Type transport")
    Code_lieu_liv_UE = fields.Char("Code lieu liv. UE")
    Lieu_Livraison = fields.Char("Lieu Livraison")
    Transporteur = fields.Char("Transporteur")
    N_Ordre_Tournee_Livraison = fields.Char("N° Ordre Tournée Livraison")
    N_adresse_livraison = fields.Char("N° adresse livraison")
    N_ordre_Livraison = fields.Char("N° ordre Livraison")
    CA_N_Avoir = fields.Char("CA N Avoir")
    Taux_Avoir = fields.Char("Taux Avoir")
    Commentaire_client_2 = fields.Char("Commentaire client 2")
    Date_Der_commande = fields.Char("Date Der. commande")
    Commentaire_client_3 = fields.Char("Commentaire client 3")
    Numerique_1 = fields.Char("Numérique 1")
    Mouvementer_des_Consignes = fields.Char("Mouvementer des Consignes")
    Consignes_valorisees = fields.Char("Consignes valorisées")
    Statut_de_relance = fields.Char("Statut de relance")
    Statut_rel_precedent = fields.Char("Statut rel. précédent")
    Consignes_en_compte = fields.Char("Consignes en compte")
    Facture_EDI = fields.Char("Facture EDI")
    URL2 = fields.Char("URL2")
    Periodicite_releve = fields.Char("Periodicité relevé")
    Lie_au_client_N = fields.Char("Lié au client N°")
    Taux_d_escompte = fields.Char("Taux d'escompte")
    Escompte_precompte = fields.Char("Escompte précompté")
    Identifiant_Xol = fields.Char("Identifiant Xol")
    N_de_societe_XoL = fields.Char("N° de société XoL")
    Qualification_Client = fields.Char("Qualification Client")
    Ancienne_Qualification = fields.Char("Ancienne Qualification")
    Animation_1 = fields.Char("Animation 1")
    Animation_2 = fields.Char("Animation 2")
    Animation_3 = fields.Char("Animation 3")
    Animation_4 = fields.Char("Animation 4")
    Animation_5 = fields.Char("Animation 5")
    Animation_6 = fields.Char("Animation 6")
    Mode_d_expedition = fields.Char("Mode d'expédition")

    @api.multi
    def get_pays(self, pays):
        return {
            'ZWE': 'ZW',
            'ZMB': 'ZM',
            'ZAF': 'ZA',
            'YEM': 'YE',
            'WSM': 'WS',
            'WLF': 'WF',
            'VUT': 'VU',
            'VNM': 'VN',
            'VIR': 'VI',
            'VGB': 'VG',
            'VEN': 'VE',
            'VCT': 'VC',
            'VAT': 'VA',
            'UZB': 'UZ',
            'USA': 'US',
            'URY': 'UY',
            'UMI': 'UM',
            'UKR': 'UA',
            'UGA': 'UG',
            'TZA': 'TZ',
            'TWN': 'TW',
            'TUV': 'TV',
            'TUR': 'TR',
            'TUN': 'TN',
            'TTO': 'TT',
            'TON': 'TO',
            'TLS': 'TL',
            'TKM': 'TM',
            'TKL': 'TK',
            'TJK': 'TJ',
            'THA': 'TH',
            'TGO': 'TG',
            'TCD': 'TD',
            'TCA': 'TC',
            'SYR': 'SY',
            'SYC': 'SC',
            'SXM': 'SX',
            'SWZ': 'SZ',
            'SWE': 'SE',
            'SVN': 'SI',
            'SVK': 'SK',
            'SUR': 'SR',
            'STP': 'ST',
            'SSD': 'SS',
            'SRB': 'RS',
            'SPM': 'PM',
            'SOM': 'SO',
            'SMR': 'SM',
            'SLV': 'SV',
            'SLE': 'SL',
            'SLB': 'SB',
            'SJM': 'SJ',
            'SHN': 'SH',
            'SGS': 'GS',
            'SGP': 'SG',
            'SEN': 'SN',
            'SDN': 'SD',
            'SAU': 'SA',
            'RWA': 'RW',
            'RUS': 'RU',
            'ROU': 'RO',
            'REU': 'RE',
            'QAT': 'QA',
            'PYF': 'PF',
            'PSE': 'PS',
            'PRY': 'PY',
            'PRT': 'PT',
            'PRK': 'KP',
            'PRI': 'PR',
            'POL': 'PL',
            'PNG': 'PG',
            'PLW': 'PW',
            'PHL': 'PH',
            'PER': 'PE',
            'PCN': 'PN',
            'PAN': 'PA',
            'PAK': 'PK',
            'OMN': 'OM',
            'NZL': 'NZ',
            'NRU': 'NR',
            'NPL': 'NP',
            'NOR': 'NO',
            'NLD': 'NL',
            'NIU': 'NU',
            'NIC': 'NI',
            'NGA': 'NG',
            'NFK': 'NF',
            'NER': 'NE',
            'NCL': 'NC',
            'NAM': 'NA',
            'MYT': 'YT',
            'MYS': 'MY',
            'MWI': 'MW',
            'MUS': 'MU',
            'MTQ': 'MQ',
            'MSR': 'MS',
            'MRT': 'MR',
            'MOZ': 'MZ',
            'MNP': 'MP',
            'MNG': 'MN',
            'MNE': 'ME',
            'MMR': 'MM',
            'MLT': 'MT',
            'MLI': 'ML',
            'MKD': 'MK',
            'MHL': 'MH',
            'MEX': 'MX',
            'MDV': 'MV',
            'MDG': 'MG',
            'MDA': 'MD',
            'MCO': 'MC',
            'MAR': 'MA',
            'MAF': 'MF',
            'MAC': 'MO',
            'LVA': 'LV',
            'LUX': 'LU',
            'LTU': 'LT',
            'LSO': 'LS',
            'LKA': 'LK',
            'LIE': 'LI',
            'LCA': 'LC',
            'LBY': 'LY',
            'LBR': 'LR',
            'LBN': 'LB',
            'LAO': 'LA',
            'KWT': 'KW',
            'KOR': 'KR',
            'KNA': 'KN',
            'KIR': 'KI',
            'KHM': 'KH',
            'KGZ': 'KG',
            'KEN': 'KE',
            'KAZ': 'KZ',
            'JPN': 'JP',
            'JOR': 'JO',
            'JEY': 'JE',
            'JAM': 'JM',
            'ITA': 'IT',
            'ISR': 'IL',
            'ISL': 'IS',
            'IRQ': 'IQ',
            'IRN': 'IR',
            'IRL': 'IE',
            'IOT': 'IO',
            'IND': 'IN',
            'IMN': 'IM',
            'IDN': 'ID',
            'HUN': 'HU',
            'HTI': 'HT',
            'HRV': 'HR',
            'HND': 'HN',
            'HMD': 'HM',
            'HKG': 'HK',
            'GUY': 'GY',
            'GUM': 'GU',
            'GUF': 'GF',
            'GTM': 'GT',
            'GRL': 'GL',
            'GRD': 'GD',
            'GRC': 'GR',
            'GNQ': 'GQ',
            'GNB': 'GW',
            'GMB': 'GM',
            'GLP': 'GP',
            'GIN': 'GN',
            'GIB': 'GI',
            'GHA': 'GH',
            'GGY': 'GG',
            'GEO': 'GE',
            'GBR': 'GB',
            'GAB': 'GA',
            'FSM': 'FM',
            'FRO': 'FO',
            'FRA': 'FR',
            'FLK': 'FK',
            'FJI': 'FJ',
            'FIN': 'FI',
            'ETH': 'ET',
            'EST': 'EE',
            'ESP': 'ES',
            'ESH': 'EH',
            'ERI': 'ER',
            'EGY': 'EG',
            'ECU': 'EC',
            'DZA': 'DZ',
            'DOM': 'DO',
            'DNK': 'DK',
            'DMA': 'DM',
            'DJI': 'DJ',
            'DEU': 'DE',
            'CZE': 'CZ',
            'CYP': 'CY',
            'CYM': 'KY',
            'CXR': 'CX',
            'CUW': 'CW',
            'CUB': 'CU',
            'CRI': 'CR',
            'CPV': 'CV',
            'COM': 'KM',
            'COL': 'CO',
            'COK': 'CK',
            'COG': 'CG',
            'COD': 'CD',
            'CMR': 'CM',
            'CIV': 'CI',
            'CHN': 'CN',
            'CHL': 'CL',
            'CHE': 'CH',
            'CCK': 'CC',
            'CAN': 'CA',
            'CAF': 'CF',
            'BWA': 'BW',
            'BVT': 'BV',
            'BTN': 'BT',
            'BRN': 'BN',
            'BRB': 'BB',
            'BRA': 'BR',
            'BOL': 'BO',
            'BMU': 'BM',
            'BLZ': 'BZ',
            'BLR': 'BY',
            'BLM': 'BL',
            'BIH': 'BA',
            'BHS': 'BS',
            'BHR': 'BH',
            'BGR': 'BG',
            'BGD': 'BD',
            'BFA': 'BF',
            'BES': 'BQ',
            'BEN': 'BJ',
            'BEL': 'BE',
            'BDI': 'BI',
            'AZE': 'AZ',
            'AUT': 'AT',
            'AUS': 'AU',
            'ATG': 'AG',
            'ATF': 'TF',
            'ATA': 'AQ',
            'ASM': 'AS',
            'ARM': 'AM',
            'ARG': 'AR',
            'ARE': 'AE',
            'AND': 'AD',
            'ALB': 'AL',
            'ALA': 'AX',
            'AIA': 'AI',
            'AGO': 'AO',
            'AFG': 'AF',
            'ABW': 'AW',

        }[pays]


    @api.multi
    def is_empty_char(self, value):			# Cette fonction retourne value si elle contient une valeur ou une chaine vide si non 
        if value:
            return value
        else:
            return ""

    @api.multi
    def is_empty_float(self, value):	# Cette fonction retourne value si elle contient un nombre ou 0 si non 
        if value:
            return float(value)
        else:
            return 0

    @api.model
    def create(self, values):	# Cette fonction retourne un record et permet la création d'un client
        record = super(TmpClient, self).create(values)
        Nom_1 = self.is_empty_char(values.get('Nom_1'))
        Nom_2 = self.is_empty_char(values.get('Nom_2'))
        Ville = self.is_empty_char(values.get('Ville'))
        Code_Postal = self.is_empty_char(values.get('Code_Postal'))
        E_mail = self.is_empty_char(values.get('E_mail'))
        URL = self.is_empty_char(values.get('URL'))
        FAX = self.is_empty_char(values.get('FAX'))
        Telephone = self.is_empty_char(values.get('Telephone'))
        Portable = self.is_empty_char(values.get('Portable'))
        Adresse_1 = self.is_empty_char(values.get('Adresse_1'))
        Adresse_2 = self.is_empty_char(values.get('Adresse_2'))
        N_Client = self.is_empty_char(values.get('N_Client'))

        #livraison

        Nom_Livraison = self.is_empty_char(values.get('Nom_Livraison'))
        Prenom_Livraison = self.is_empty_char(values.get('Prenom_Livraison'))
        Ad_Liv_1 = self.is_empty_char(values.get('Ad_Liv_1'))
        Ad_Liv_2 = self.is_empty_char(values.get('Ad_Liv_2'))
        CP_Livraison = self.is_empty_char(values.get('CP_Livraison'))
        Ville_Liv = self.is_empty_char(values.get('Ville_Liv'))
        Code_pays_Livraison = self.is_empty_char(values.get('Code_pays_Livraison'))
        Pays = self.is_empty_char(values.get('Pays'))
        Telephone_Livraison = self.is_empty_char(values.get('Telephone_Livraison'))
        Fax_Livraison = self.is_empty_char(values.get('Fax_Livraison'))
        Portable_Livraison = self.is_empty_char(values.get('Portable_Livraison'))
        E_mail_Livraison = self.is_empty_char(values.get('E_mail_Livraison'))
        Commentaire_Livraison = self.is_empty_char(values.get('Commentaire_Livraison'))

        code_pays = self.env['res.country'].search([('code','=',self.get_pays(Pays))])
        code_Code_pays_Livraison = self.env['res.country'].search([('code','=',self.get_pays(Code_pays_Livraison))])



        valuesc = {  # 'comment': False,
            # 'function': False,
            'notify_email': 'always',
            # 'message_follower_ids': False,
            'company_type': 'person',
            'N_Client': N_Client,  # N_Client
            # 'property_stock_customer': 9,
            'street': Adresse_1,  # Adresse_1
            # 'property_account_receivable_id': 227,
            # 'property_account_position_id': False,
            # 'property_payment_term_id': False,
            'city': Ville,
            'country_id': code_pays.id,
            # 'user_id': False,
            # 'opt_out': False,
            'zip': Code_Postal,  # Code_Postal
            # 'title': False,
            # 'company_id': 1,
            # 'message_ids': False,
            # 'parent_id': False,
            # 'supplier': False,
            # 'property_supplier_payment_term_id': False,
            'type': 'contact',
            'email': E_mail,  # E_mail
            # 'is_company': False,
            'website': URL,  # v
            'customer': True,
            'fax': FAX,  # FAX
            'street2': Adresse_2,  # Adresse_2
            'child_ids': [[0, False,
                           {u'function': False, u'city': Ville_Liv, u'name': Nom_Livraison + " " + Prenom_Livraison, u'zip': CP_Livraison, u'title': False,
                            u'mobile': Portable_Livraison, u'street2': Ad_Liv_2, u'country_id': code_Code_pays_Livraison.id, u'comment': False,
                            u'phone': Telephone_Livraison, u'street': Ad_Liv_1, u'customer': Commentaire_Livraison,
                            u'supplier': False, u'state_id': False, u'type': u'delivery', u'email': E_mail_Livraison,
                            u'lang': u'fr_FR'}]], #adress liv
            'phone': Telephone,
            # 'user_ids': [],
            'active': True,
            'lang': 'fr_FR',
            # 'property_stock_supplier': 8,
            'name': Nom_1 + " " + Nom_2,  # nom
            'mobile': Portable,
            # 'ref': N_Client, #N_Client
            # 'property_account_payable_id': 292,
            'state_id': False,
            'category_id': [],
            'importe': True,
        }
        # client = self.env['res.partner'].search([('ref','=',self.N_Client)])
        # if client:
        #   _logger.error("Ce Client existe déjà !")
        # else:
        self.env['res.partner'].create(valuesc)
        return record


# class Partner(models.Model):
#     _inherit = 'res.partner'
#
#     @api.model
#     def create(self, values):
#         _logger.info("----------------> client iciiiiiiiiiiiiiiiiiiiiiiii : " + str(values))
#         return super(Partner, self).create(values)
