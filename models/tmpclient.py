#!/usr/bin/python
# coding: utf8
from openerp import fields, models, api, _
import logging
import time
_logger = logging.getLogger(__name__)


class TmpClient(models.Model):
    _name = 'tmpclient'
    _rec_name = 'n_client_0'

    age_du_jardin_24 = fields.Char("âge du jardin")
    age_du_jardin_25 = fields.Char("(âge du jardin)")
    n_client_0 = fields.Char("N° Client")
    civilit_1 = fields.Char("Civilité")
    nom_1_2 = fields.Char("Nom 1")
    nom_2_3 = fields.Char("Nom 2")
    rais_soc_4 = fields.Char("Rais. Soc.")
    adresse_1_5 = fields.Char("Adresse (1)")
    adresse_2_6 = fields.Char("Adresse (2)")
    code_postal_7 = fields.Char("Code Postal")
    ville_8 = fields.Char("Ville")
    pays_9 = fields.Char("Pays")
    t_l_phone_10 = fields.Char("Téléphone")
    portable_11 = fields.Char("Portable")
    fax_12 = fields.Char("Fax")
    e_mail_13 = fields.Char("E-mail")
    url_14 = fields.Char("URL")
    code_cat_gorie_15 = fields.Char("Code Catégorie")
    cont_fichier_16 = fields.Char("Cont.fichier")
    _cont_fichier_17 = fields.Char("(Cont.fichier)")
    altitude_du_jardin_18 = fields.Char("altitude du jardin")
    _altitude_du_jardin_19 = fields.Char("(altitude du jardin)")
    surface_du_jardin_20 = fields.Char("surface du jardin")
    _surface_du_jardin_21 = fields.Char("(surface du jardin)")
    crit_re_4_22 = fields.Char("Critère 4")
    _crit_re_4_23 = fields.Char("(Critère 4)")
    type_de_client_26 = fields.Char("type de client")
    type_de_client_27 = fields.Char("(type de client)")
    code_repr_sentant_28 = fields.Char("Code Représentant")
    code_etiquette_29 = fields.Char("Code Etiquette")
    mode_de_r_glement_30 = fields.Char("Mode de Règlement")
    type_classe_31 = fields.Char("Type Classe")
    taux_remise_lig_32 = fields.Char("Taux Remise Lig.")
    taux_remise_pied_33 = fields.Char("Taux Remise Pied")
    interdit_34 = fields.Char("Interdit")
    compte_tiers_35 = fields.Char("Compte Tiers")
    date_ent_36 = fields.Char("Date Ent.")
    date_dern_modif_37 = fields.Char("Date Dern. Modif.")
    ca_n_38 = fields.Char("CA N")
    ca_n_1_39 = fields.Char("CA N-1")
    ca_n_2_40 = fields.Char("CA N-2")
    commentaire_client_41 = fields.Char("Commentaire client")
    identification_tva_42 = fields.Char("Identification TVA")
    assurance_43 = fields.Char("Assurance")
    devise_44 = fields.Char("Devise")
    compte_factur_45 = fields.Char("Compte Facturé")
    regroup_facture_46 = fields.Char("Regroup. Facture")
    plafond_47 = fields.Char("Plafond")
    date_dern_modif_plafond_48 = fields.Char("Date Dern. Modif. Plafond")
    objectif_ca_49 = fields.Char("Objectif CA")
    adresse_exp_50 = fields.Char("Adresse Exp.")
    code_postal_51 = fields.Char("Code Postal")
    ville_52 = fields.Char("Ville")
    pays_53 = fields.Char("Pays")
    comment_livraison_54 = fields.Char("Comment. Livraison")
    pays_prov_dest_55 = fields.Char("Pays Prov./Dest.")
    pays_d_origine_56 = fields.Char("Pays d'origine")
    port_57 = fields.Char("Port")
    code_cond_58 = fields.Char("Code Cond.")
    nbre_factures_59 = fields.Char("Nbre Factures")
    rempl_taille_60 = fields.Char("Rempl. Taille")
    rempl_vari_t_61 = fields.Char("Rempl. Variété")
    code_pays_code_barre_62 = fields.Char("Code Pays - code barre")
    masquer_dans_les_listes_63 = fields.Char("Masquer dans les listes")
    cnuf_64 = fields.Char("CNUF")
    n_r_f_65 = fields.Char("N° Réf.")
    logo_66 = fields.Char("Logo")
    n_tarification_67 = fields.Char("N° Tarification")
    mod_le_etiquette_68 = fields.Char("Modèle Etiquette")
    mod_le_de_facture_69 = fields.Char("Modèle de Facture")
    code_client_70 = fields.Char("Code Client")
    type_de_plantation_71 = fields.Char("type de plantation")
    type_d_entretien_72 = fields.Char("type d'entretien")
    parrainage_73 = fields.Char("parrainage")
    type_de_profil_74 = fields.Char("type de profil")
    interm_diaire_75 = fields.Char("intermédiaire")
    interm_diaire_2_76 = fields.Char("Intermédiaire 2")
    newsletter_77 = fields.Char("NEWSLETTER")
    crit_re_14_78 = fields.Char("Critère 14")
    crit_re_15_79 = fields.Char("Critère 15")
    crit_re_16_80 = fields.Char("Critère 16")
    crit_re_17_81 = fields.Char("Critère 17")
    crit_re_18_82 = fields.Char("Critère 18")
    nom_livraison_83 = fields.Char("Nom Livraison")
    pr_nom_livraison_84 = fields.Char("Prénom Livraison")
    ad_liv_1_85 = fields.Char("Ad. Liv. 1")
    ad_liv_2_86 = fields.Char("Ad. Liv. 2")
    cp_livraison_87 = fields.Char("CP Livraison")
    ville_liv_88 = fields.Char("Ville Liv.")
    code_pays_livraison_89 = fields.Char("Code pays Livraison")
    t_l_phone_livraison_90 = fields.Char("Téléphone Livraison")
    fax_livraison_91 = fields.Char("Fax Livraison")
    portable_livraison_92 = fields.Char("Portable Livraison")
    e_mail_livraison_93 = fields.Char("E-mail Livraison")
    commentaire_livraison_94 = fields.Char("Commentaire Livraison")
    zone_exp_95 = fields.Char("Zone Exp.")
    incoterm_96 = fields.Char("Incoterm")
    type_transport_97 = fields.Char("Type transport")
    code_lieu_liv_ue_98 = fields.Char("Code lieu liv. UE")
    lieu_livraison_99 = fields.Char("Lieu Livraison")
    transporteur_100 = fields.Char("Transporteur")
    n_ordre_tourn_e_livraison_101 = fields.Char("N° Ordre Tournée Livraison")
    n_adresse_livraison_102 = fields.Char("N° adresse livraison")
    n_ordre_livraison_103 = fields.Char("N° ordre Livraison")
    ca_n_avoir_104 = fields.Char("CA N Avoir")
    taux_avoir_105 = fields.Char("Taux Avoir")
    commentaire_client_2_106 = fields.Char("Commentaire client 2")
    date_der_commande_107 = fields.Char("Date Der. commande")
    commentaire_client_3_108 = fields.Char("Commentaire client 3")
    num_rique_1_109 = fields.Char("Numérique 1")
    mouvementer_des_consignes_110 = fields.Char("Mouvementer des Consignes")
    consignes_valoris_es_111 = fields.Char("Consignes valorisées")
    statut_de_relance_112 = fields.Char("Statut de relance")
    statut_rel_pr_c_dent_113 = fields.Char("Statut rel. précédent")
    consignes_en_compte_114 = fields.Char("Consignes en compte")
    facture_edi_115 = fields.Char("Facture EDI")
    url2_116 = fields.Char("URL2")
    periodicit_relev_117 = fields.Char("Periodicité relevé")
    li_au_client_n_118 = fields.Char("Lié au client N°")
    taux_d_escompte_119 = fields.Char("Taux d'escompte")
    escompte_pr_compt_120 = fields.Char("Escompte précompté")
    identifiant_xol_121 = fields.Char("Identifiant Xol")
    n_de_soci_t_xol_122 = fields.Char("N° de société XoL")
    qualification_client_123 = fields.Char("Qualification Client")
    ancienne_qualification_124 = fields.Char("Ancienne Qualification")
    animation_1_125 = fields.Char("Animation 1")
    animation_2_126 = fields.Char("Animation 2")
    animation_3_127 = fields.Char("Animation 3")
    animation_4_128 = fields.Char("Animation 4")
    animation_5_129 = fields.Char("Animation 5")
    animation_6_130 = fields.Char("Animation 6")
    mode_d_exp_dition_131 = fields.Char("Mode d'expédition")

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

        nom_1_2 = self.is_empty_char(values.get('nom_1_2'))
        nom_2_3 = self.is_empty_char(values.get('nom_2_3'))
        ville_8 = self.is_empty_char(values.get('ville_8'))
        code_postal_7 = self.is_empty_char(values.get('code_postal_7'))
        e_mail_13 = self.is_empty_char(values.get('e_mail_13'))
        url_14 = self.is_empty_char(values.get('url_14'))
        fax_12 = self.is_empty_char(values.get('fax_12'))
        t_l_phone_10 = self.is_empty_char(values.get('t_l_phone_10'))
        portable_11 = self.is_empty_char(values.get('portable_11'))
        adresse_1_5 = self.is_empty_char(values.get('adresse_1_5'))
        adresse_2_6 = self.is_empty_char(values.get('adresse_2_6'))
        _n_client_0 = self.is_empty_char(values.get('_n_client_0'))
        type_de_client_26 = self.is_empty_char(values.get('type_de_client_26'))

        #livraison

        nom_livraison_83 = self.is_empty_char(values.get('nom_livraison_83'))
        pr_nom_livraison_84 = self.is_empty_char(values.get('pr_nom_livraison_84'))
        ad_liv_1_85 = self.is_empty_char(values.get('ad_liv_1_85'))
        ad_liv_2_86 = self.is_empty_char(values.get('ad_liv_2_86'))
        cp_livraison_87 = self.is_empty_char(values.get('cp_livraison_87'))
        ville_liv_88 = self.is_empty_char(values.get('ville_liv_88'))
        code_pays_livraison_89 = self.is_empty_char(values.get('code_pays_livraison_89'))
        pays_9 = self.is_empty_char(values.get('pays_9'))
        t_l_phone_livraison_90 = self.is_empty_char(values.get('t_l_phone_livraison_90'))
        fax_livraison_91 = self.is_empty_char(values.get('fax_livraison_91'))
        portable_livraison_92 = self.is_empty_char(values.get('portable_livraison_92'))
        e_mail_livraison_93 = self.is_empty_char(values.get('e_mail_livraison_93'))
        commentaire_livraison_94 = self.is_empty_char(values.get('commentaire_livraison_94'))
        code_pays = self.env['res.country'].search([('code','=',self.get_pays(pays_9))])
        code_pays_Livraison = self.env['res.country'].search([('code','=',self.get_pays(code_pays_livraison_89))])



        valuesc = {  # 'comment': False,
            # 'function': False,
            'notify_email': 'always',
            # 'message_follower_ids': False,
            'company_type': 'person',
            'N_Client': _n_client_0,  # N_Client
            # 'property_stock_customer': 9,
            'street': adresse_1_5,  # Adresse_1
            # 'property_account_receivable_id': 227,
            # 'property_account_position_id': False,
            # 'property_payment_term_id': False,
            'city': ville_8,
            'country_id': code_pays.id,
            # 'user_id': False,
            # 'opt_out': False,
            'zip': code_postal_7,  # Code_Postal
            # 'title': False,
            # 'company_id': 1,
            # 'message_ids': False,
            # 'parent_id': False,
            # 'supplier': False,
            # 'property_supplier_payment_term_id': False,
            'type': 'contact',
            'email': e_mail_13,  # E_mail
            # 'is_company': False,
            'website': url_14,  # v
            'customer': True,
            'fax': fax_12,  # FAX
            'street2': adresse_2_6,  # Adresse_2
            'child_ids': [[0, False,
                           {u'function': False, u'city': ville_liv_88, u'name': nom_livraison_83 + " " + pr_nom_livraison_84, u'zip': cp_livraison_87, u'title': False,
                            u'mobile': portable_livraison_92, u'street2': ad_liv_2_86, u'country_id': code_pays_Livraison.id, u'comment': False,
                            u'phone': t_l_phone_livraison_90, u'street': ad_liv_1_85, u'customer': commentaire_livraison_94,
                            u'supplier': False, u'state_id': False, u'type': u'delivery', u'email': e_mail_livraison_93,
                            u'lang': u'fr_FR'}]], #adress liv
            'phone': t_l_phone_10,
            # 'user_ids': [],
            'active': True,
            'lang': 'fr_FR',
            # 'property_stock_supplier': 8,
            'name': nom_1_2 + " " + nom_2_3,  # nom
            'mobile': portable_11,
            # 'ref': N_Client, #N_Client
            # 'property_account_payable_id': 292,
            'state_id': False,
            'category_id': [],
            'importe': True,
            'type_client': type_de_client_26,
        }
        # client = self.env['res.partner'].search([('ref','=',self.N_Client)])
        # if client:
        #   _logger.error("Ce Client existe déjà !")
        # else:

        obj_partner = self.env['res.partner'].search([('N_Client', '=', _n_client_0)])
        print "obj_partner"
        print obj_partner
        if obj_partner:
            obj_partner.child_ids.unlink()
            obj_partner.write(valuesc)
        else:
            self.env['res.partner'].create(valuesc)
        return record

    @api.multi
    def write(self, values):
        print "values"
        print values

        record = super(TmpClient, self).write(values)

        print "values"
        print values

        nom_1_2 = self.is_empty_char(values.get('nom_1_2'))
        nom_2_3 = self.is_empty_char(values.get('nom_2_3'))
        ville_8 = self.is_empty_char(values.get('ville_8'))
        code_postal_7 = self.is_empty_char(values.get('code_postal_7'))
        e_mail_13 = self.is_empty_char(values.get('e_mail_13'))
        url_14 = self.is_empty_char(values.get('url_14'))
        fax_12 = self.is_empty_char(values.get('fax_12'))
        t_l_phone_10 = self.is_empty_char(values.get('t_l_phone_10'))
        portable_11 = self.is_empty_char(values.get('portable_11'))
        adresse_1_5 = self.is_empty_char(values.get('adresse_1_5'))
        adresse_2_6 = self.is_empty_char(values.get('adresse_2_6'))
        _n_client_0 = self.is_empty_char(values.get('_n_client_0'))
        type_de_client_26 = self.is_empty_char(values.get('type_de_client_26'))

        # livraison

        nom_livraison_83 = self.is_empty_char(values.get('nom_livraison_83'))
        pr_nom_livraison_84 = self.is_empty_char(values.get('pr_nom_livraison_84'))
        ad_liv_1_85 = self.is_empty_char(values.get('ad_liv_1_85'))
        ad_liv_2_86 = self.is_empty_char(values.get('ad_liv_2_86'))
        cp_livraison_87 = self.is_empty_char(values.get('cp_livraison_87'))
        ville_liv_88 = self.is_empty_char(values.get('ville_liv_88'))
        code_pays_livraison_89 = self.is_empty_char(values.get('code_pays_livraison_89'))
        pays_9 = self.is_empty_char(values.get('pays_9'))
        t_l_phone_livraison_90 = self.is_empty_char(values.get('t_l_phone_livraison_90'))
        fax_livraison_91 = self.is_empty_char(values.get('fax_livraison_91'))
        portable_livraison_92 = self.is_empty_char(values.get('portable_livraison_92'))
        e_mail_livraison_93 = self.is_empty_char(values.get('e_mail_livraison_93'))
        commentaire_livraison_94 = self.is_empty_char(values.get('commentaire_livraison_94'))
        code_pays = self.env['res.country'].search([('code', '=', self.get_pays(pays_9))])
        code_pays_Livraison = self.env['res.country'].search([('code', '=', self.get_pays(code_pays_livraison_89))])

        valuesc = {  # 'comment': False,
            # 'function': False,
            'notify_email': 'always',
            # 'message_follower_ids': False,
            'company_type': 'person',
            'N_Client': _n_client_0,  # N_Client
            # 'property_stock_customer': 9,
            'street': adresse_1_5,  # Adresse_1
            # 'property_account_receivable_id': 227,
            # 'property_account_position_id': False,
            # 'property_payment_term_id': False,
            'city': ville_8,
            'country_id': code_pays.id,
            # 'user_id': False,
            # 'opt_out': False,
            'zip': code_postal_7,  # Code_Postal
            # 'title': False,
            # 'company_id': 1,
            # 'message_ids': False,
            # 'parent_id': False,
            # 'supplier': False,
            # 'property_supplier_payment_term_id': False,
            'type': 'contact',
            'email': e_mail_13,  # E_mail
            # 'is_company': False,
            'website': url_14,  # v
            'customer': True,
            'fax': fax_12,  # FAX
            'street2': adresse_2_6,  # Adresse_2
            'child_ids': [[0, False,
                           {u'function': False, u'city': ville_liv_88,
                            u'name': nom_livraison_83 + " " + pr_nom_livraison_84, u'zip': cp_livraison_87,
                            u'title': False,
                            u'mobile': portable_livraison_92, u'street2': ad_liv_2_86,
                            u'country_id': code_pays_Livraison.id, u'comment': False,
                            u'phone': t_l_phone_livraison_90, u'street': ad_liv_1_85,
                            u'customer': commentaire_livraison_94,
                            u'supplier': False, u'state_id': False, u'type': u'delivery', u'email': e_mail_livraison_93,
                            u'lang': u'fr_FR'}]],  # adress liv
            'phone': t_l_phone_10,
            # 'user_ids': [],
            'active': True,
            'lang': 'fr_FR',
            # 'property_stock_supplier': 8,
            'name': nom_1_2 + " " + nom_2_3,  # nom
            'mobile': portable_11,
            # 'ref': N_Client, #N_Client
            # 'property_account_payable_id': 292,
            'state_id': False,
            'category_id': [],
            'importe': True,
            'type_client': type_de_client_26,
        }

        print "valuesc"
        print valuesc

        obj_partner = self.env['res.partner'].search([('N_Client', '=', _n_client_0)])
        print "obj_partner"
        print obj_partner
        if obj_partner:
            obj_partner.child_ids.unlink()
            obj_partner.write(valuesc)
        else:
            self.env['res.partner'].create(valuesc)

        # client = self.env['res.partner'].search([('ref','=',self.N_Client)])
        # if client:
        #   _logger.error("Ce Client existe déjà !")
        # else:
        #self.env['res.partner'].write(valuesc)
        return record


# class Partner(models.Model):
#     _inherit = 'res.partner'
#
#     @api.model
#     def create(self, values):
#         _logger.info("----------------> client iciiiiiiiiiiiiiiiiiiiiiiii : " + str(values))
#         return super(Partner, self).create(values)
