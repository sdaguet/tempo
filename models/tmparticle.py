#!/usr/bin/python
# coding: utf8
from openerp import fields, models, api, _
import logging
import time
_logger = logging.getLogger(__name__)

class TmpArticle(models.Model):

    _name = 'tmparticle'
    _rec_name = 'n_article_0'
    n_article_0 = fields.Char("N° Article")
    code_article_1 = fields.Char("Code article")
    code_barre_2 = fields.Char("Code Barre")
    genre_3 = fields.Char("Genre")
    espece_4 = fields.Char("Espece")
    variete_5 = fields.Char("Variete")
    catalogue_6 = fields.Char("Catalogue")
    marque_savoie_7 = fields.Char("Marque Savoie")
    pr_sentation_8 = fields.Char("Présentation")
    _pr_sentation_9 = fields.Char("Présentation")
    taille_10 = fields.Char("Taille")
    _taille_11 = fields.Char("Taille")
    famille_12 = fields.Char("Famille")
    tarif_13 = fields.Char("tarif")
    type_de_feuillage_14 = fields.Char("type de feuillage")
    famille_presta_15 = fields.Char("Famille/Presta")
    promo_automne_16 = fields.Char("Promo automne")
    crit_re_7_17 = fields.Char("Critère 7")
    crit_re_8_18 = fields.Char("Critère 8")
    crit_re_9_19 = fields.Char("Critère 9")
    libell_commercial_20 = fields.Char("Libellé commercial")
    nom_fran_ais_21 = fields.Char("Nom français")
    n_conseil_22 = fields.Char("N° conseil")
    mod_le_tiquette_23 = fields.Char("Modèle étiquette")
    prix_etiquette_24 = fields.Char("Prix Etiquette")
    code_comptable_25 = fields.Char("Code comptable")
    remise_26 = fields.Char("Remise")
    tva_27 = fields.Char("TVA")
    hauteur_mm_28 = fields.Char("Hauteur mm")
    poids_brut_29 = fields.Char("Poids Brut")
    compl_ment_30 = fields.Char("Complément")
    code_vente_31 = fields.Char("Code vente")
    conditionnement_32 = fields.Char("Conditionnement")
    ca_n_33 = fields.Char("CA N")
    ca_n_1_34 = fields.Char("CA N-1")
    ca_n_2_35 = fields.Char("CA N-2")
    qt_n_36 = fields.Char("Qté N")
    qt_n_1_37 = fields.Char("Qté N-1")
    qt_n_2_38 = fields.Char("Qté N-2")
    masquer_dans_les_listes_39 = fields.Char("Masquer dans les listes")
    date_de_cr_ation_40 = fields.Char("Date de création")
    derni_re_modification_41 = fields.Char("Dernière modification")
    groupe_tarifaire_42 = fields.Char("Groupe tarifaire")
    n_article_d_stockage_43 = fields.Char("N° article déstockage")
    coeff_d_stockage_44 = fields.Char("Coeff. déstockage")
    poids_net_45 = fields.Char("Poids Net")
    type_fiscal_46 = fields.Char("Type fiscal")
    crit_re_10_47 = fields.Char("Critère 10")
    crit_re_11_48 = fields.Char("Critère 11")
    crit_re_12_49 = fields.Char("Critère 12")
    crit_re_13_50 = fields.Char("Critère 13")
    crit_re_14_51 = fields.Char("Critère 14")
    crit_re_15_52 = fields.Char("Critère 15")
    crit_re_16_53 = fields.Char("Critère 16")
    crit_re_17_54 = fields.Char("Critère 17")
    crit_re_18_55 = fields.Char("Critère 18")
    gestion_du_stock_56 = fields.Char("Gestion du stock")
    unit_de_tarification_57 = fields.Char("Unité de tarification")
    sur_appellation_58 = fields.Char("Sur Appellation")
    sous_famille_article_59 = fields.Char("Sous Famille article")
    pays_d_origine_60 = fields.Char("Pays d'origine")
    ca_n_fourn_61 = fields.Char("CA N Fourn.")
    ca_n_1_fourn_62 = fields.Char("CA N-1 Fourn.")
    ca_n_2_fourn_63 = fields.Char("CA N-2 Fourn.")
    qt_n_64 = fields.Char("Qté N")
    qt_n_1_65 = fields.Char("Qté N-1")
    qt_n_2_66 = fields.Char("Qté N-2")
    ca_n_a_nouveau_67 = fields.Char("CA N A-Nouveau")
    qt_n_a_nouveau_68 = fields.Char("Qté N A-Nouveau")
    qt_n_fourn_a_nouveau_69 = fields.Char("Qté N Fourn. A-Nouveau")
    ca_n_fourn_a_nouveau_70 = fields.Char("CA N Fourn. A-Nouveau")
    domaine_util_achat_71 = fields.Char("Domaine util. achat")
    domaine_util_vente_72 = fields.Char("Domaine util. vente")
    taux_prix_achat_73 = fields.Char("Taux prix achat")
    code_achat_74 = fields.Char("Code achat")
    pcb_article_75 = fields.Char("PCB Article")
    origine_76 = fields.Char("Origine")
    prix_ref_marge_77 = fields.Char("Prix ref marge")
    code_barre_78 = fields.Char("code barre")
    gestion_de_facteur_79 = fields.Char("Gestion de Facteur")
    code_facteur_80 = fields.Char("Code Facteur")
    remplac_par_81 = fields.Char("Remplacé par")
    n_propri_taire_82 = fields.Char("N° Propriétaire")
    fourn_principal_83 = fields.Char("Fourn. principal")
    date_de_fin_d_achat_84 = fields.Char("Date de fin d'achat")
    no_fpp_85 = fields.Char("No FPP")
    coef_fpp_86 = fields.Char("Coef. FPP")
    sem_deb_validit_87 = fields.Char("Sem. Deb. Validité")
    sem_fin_validit_88 = fields.Char("Sem. Fin Validité")
    secteur_par_d_faut_89 = fields.Char("Secteur par défaut")
    crit_re_20_90 = fields.Char("Critère 20")
    crit_re_21_91 = fields.Char("Critère 21")
    commentaire_logistique_92 = fields.Char("Commentaire logistique")
    identifiant_xol_93 = fields.Char("Identifiant XOL")
    article_totalis_94 = fields.Char("Article Totalisé")
    n_article_totalisateur_95 = fields.Char("N° Article Totalisateur")
    article_financier_96 = fields.Char("Article Financier")

    @api.multi
    def is_empty_char(self,value):  # Cette fonction retourne value si elle contient une valeur ou une chaine vide si non
        if value:
            return value
        else:
            return ""

    @api.multi
    def is_empty_float(self,value):  # Cette fonction retourne value si elle contient un nombre ou 0 si non
        if value:
            return float(value)
        else:
            return 0

    @api.multi
    def check_value(self, value, value_id):  # value = la valeure de la colonne, value_id = xml_id de l'attribut
        if value != "":
            value_exist = self.env['product.attribute.value'].search(
                [('name', '=', value), ('attribute_id', '=', value_id.id)])

            if not value_exist:
                value_attr = self.env['product.attribute.value'].create(
                    {u'color': False, u'attribute_id': value_id.id, u'name': value})
            elif value_exist:
                value_attr = value_exist

            #logger_ajouté
			#print "ici check full"
            #print value_id.name
            _logger.info("check_value(self, value, value_id) : %r" % value_id.name)

            return [[6, False,[value_attr.id]]],value_attr
        else:
            empty_attr = self.env['product.attribute.value'].browse()
			#logger_ajouté
			#print "ici check empty"
            #print value_id.name
            _logger.info("check_value(self, value, value_id) : %r" % value_id.name)
            return [],empty_attr


    @api.model
    def create(self, values):   # Cette fonction retourne un record et permet la création d'un article
            # time.time()
            # timestamp1 = time.time()
            #create tmparticle
            record = super(TmpArticle, self).create(values)
            # timestamp2 = time.time()
            # ec1 = timestamp2 -timestamp1
            # _logger.info("Objet TMPARTICLE créé: %.2f" %(ec1))
            # timestamp3 = time.time()

            nom_fran_ais_21 = self.is_empty_char(values.get('nom_fran_ais_21'))
            libell_commercial_20 = self.is_empty_char(values.get('libell_commercial_20'))
            _taille_11 = self.is_empty_char(values.get('_taille_11'))
            famille_12 = self.is_empty_char(values.get('famille_12'))

            # timestamp4 = time.time()
            # ec2 = timestamp4 - timestamp3
            # _logger.info("Champs obligatoires verifié: %.2f " %(ec2))
            # timestamp5 = time.time()

            prix_etiquette_24 = self.is_empty_float(values.get('prix_etiquette_24'))
            poids_brut_29 = self.is_empty_float(values.get('poids_brut_29'))

            code_barre_2 = self.is_empty_char(values.get('code_barre_2'))
            code_article_1 = self.is_empty_char(values.get('code_article_1'))
            n_article_0 = self.is_empty_char(values.get('n_article_0'))
            marque_savoie_7 = self.is_empty_char(values.get('marque_savoie_7'))

            TVA = self.is_empty_float(values.get('tva_27'))
            taxe_id = []

            if TVA == 4:
                taxe_id = self.env['account.tax'].search([('amount','=','10')]).ids
            elif TVA == 2:
                taxe_id = self.env['account.tax'].search([('amount', '=', '20')]).ids

            #attributs id
            xml_genre = self.env.ref("darb_puthod.product_attribute_genre")
            xml_espece = self.env.ref("darb_puthod.product_attribute_espece")
            xml_variete = self.env.ref("darb_puthod.product_attribute_variete")
            xml_taille = self.env.ref("darb_puthod.product_attribute_taille")
            xml_taille_bis = self.env.ref("darb_puthod.product_attribute_taille_bis")
            xml_type_de_feuillage = self.env.ref("darb_puthod.product_attribute_type_de_feuillage")
            xml_critere_7 = self.env.ref("darb_puthod.product_attribute_critere_7")
            xml_critere_8 = self.env.ref("darb_puthod.product_attribute_critere_8")
            xml_critere_9 = self.env.ref("darb_puthod.product_attribute_critere_9")
            xml_nom_francais = self.env.ref("darb_puthod.product_attribute_nom_francais")
            xml_modele_etiquette = self.env.ref("darb_puthod.product_attribute_modele_etiquette")
            xml_hauteur_mm = self.env.ref("darb_puthod.product_attribute_hauteur_mm")
            xml_poids_brut = self.env.ref("darb_puthod.product_attribute_poids_brut")
            xml_ca_n = self.env.ref("darb_puthod.product_attribute_ca_n")
            xml_ca_n_1 = self.env.ref("darb_puthod.product_attribute_ca_n_1")
            xml_ca_n_2 = self.env.ref("darb_puthod.product_attribute_ca_n_2")
            xml_qte_n = self.env.ref("darb_puthod.product_attribute_qte_n")
            xml_qte_n_1 = self.env.ref("darb_puthod.product_attribute_qte_n_1")
            xml_qte_n_2 = self.env.ref("darb_puthod.product_attribute_qte_n_2")
            xml_critere_18 = self.env.ref("darb_puthod.product_attribute_critere_18")
            xml_sous_famille_article = self.env.ref("darb_puthod.product_attribute_sous_famille_article")
            xml_pays_d_origine = self.env.ref("darb_puthod.product_attribute_pays_d_origine")
            xml_fourn_principal = self.env.ref("darb_puthod.product_attribute_fourn_principal")

            #attribute values

            genre = self.is_empty_char(values.get('genre_3'))
            espece = self.is_empty_char(values.get('espece_4'))
            variete = self.is_empty_char(values.get('variete_5'))
            taille = self.is_empty_char(values.get('taille_10'))
            taille_bis = self.is_empty_char(values.get('_taille_11'))
            type_de_feuillage = self.is_empty_char(values.get('type_de_feuillage_14'))
            critere_7 = self.is_empty_char(values.get('crit_re_7_17'))
            critere_8 = self.is_empty_char(values.get('crit_re_8_18'))
            critere_9 = self.is_empty_char(values.get('crit_re_9_19'))
            nom_francais = self.is_empty_char(values.get('nom_fran_ais_21'))
            modele_etiquette = self.is_empty_char(values.get('mod_le_tiquette_23'))
            hauteur_mm = self.is_empty_char(values.get('hauteur_mm_28'))
            poids_brut = self.is_empty_char(values.get('poids_brut_29'))
            ca_n = self.is_empty_char(values.get('ca_n_33'))
            ca_n_1 = self.is_empty_char(values.get('ca_n_1_34'))
            ca_n_2 = self.is_empty_char(values.get('ca_n_2_35'))
            qte_n = self.is_empty_char(values.get('qt_n_36'))
            qte_n_1 = self.is_empty_char(values.get('qt_n_1_37'))
            qte_n_2 = self.is_empty_char(values.get('qt_n_2_38'))
            critere_18 = self.is_empty_char(values.get('crit_re_18_55'))
            sous_famille_article = self.is_empty_char(values.get('sous_famille_article_59'))
            pays_d_origine = self.is_empty_char(values.get('pays_d_origine_60'))
            fourn_principal = self.is_empty_char(values.get('fourn_principal_83'))

            #check values or create
            value_genre = self.check_value(genre,xml_genre)
            value_fourn_principal = self.check_value(fourn_principal,xml_fourn_principal)
            value_pays_d_origine = self.check_value(pays_d_origine,xml_pays_d_origine)
            value_sous_famille_article = self.check_value(sous_famille_article,xml_sous_famille_article)
            value_qte_n = self.check_value(qte_n,xml_qte_n)
            value_qte_n_1 = self.check_value(qte_n_1,xml_qte_n_1)
            value_qte_n_2 = self.check_value(qte_n_2,xml_qte_n_2)
            value_ca_n = self.check_value(ca_n,xml_ca_n)
            value_ca_n_1 = self.check_value(ca_n_1,xml_ca_n_1)
            value_ca_n_2 = self.check_value(ca_n_2,xml_ca_n_2)
            value_poids_brut = self.check_value(poids_brut,xml_poids_brut)
            value_hauteur_mm = self.check_value(hauteur_mm,xml_hauteur_mm)
            value_modele_etiquette = self.check_value(modele_etiquette,xml_modele_etiquette)
            value_nom_francais = self.check_value(nom_francais,xml_nom_francais)
            value_critere_7 = self.check_value(critere_7,xml_critere_7)
            value_critere_8 = self.check_value(critere_8,xml_critere_8)
            value_critere_18 = self.check_value(critere_18,xml_critere_18)
            value_critere_9 = self.check_value(critere_9,xml_critere_9)
            value_type_de_feuillage = self.check_value(type_de_feuillage,xml_type_de_feuillage)
            value_taille_bis = self.check_value(taille_bis,xml_taille_bis)
            value_taille = self.check_value(taille,xml_taille)
            value_variete = self.check_value(variete,xml_variete)
            value_espece = self.check_value(espece,xml_espece)

            valuesp = {
                # 'warranty': 0,
                # 'message_follower_ids': False,
                # 'property_account_creditor_price_difference': False,
                # 'standard_price': 0,
                'attribute_line_ids': [[0, False, {u'attribute_id': xml_genre.id, u'value_ids': value_genre[0]}],
                                       [0, False, {u'attribute_id': xml_espece.id, u'value_ids': value_espece[0]}],
                                       [0, False, {u'attribute_id': xml_variete.id, u'value_ids': value_variete[0]}],
                                       # [0, False, {u'attribute_id': xml_taille.id, u'value_ids': value_taille[0]}],
                                       [0, False, {u'attribute_id': xml_taille_bis.id, u'value_ids': value_taille_bis[0]}],
                                       # [0, False, {u'attribute_id': xml_type_de_feuillage.id, u'value_ids': value_type_de_feuillage[0]}],
                                       # [0, False, {u'attribute_id': xml_critere_7.id, u'value_ids': value_critere_7[0]}],
                                       # [0, False, {u'attribute_id': xml_critere_8.id, u'value_ids': value_critere_8[0]}],
                                       # [0, False, {u'attribute_id': xml_critere_9.id, u'value_ids': value_critere_9[0]}],
                                       # [0, False, {u'attribute_id': xml_nom_francais.id, u'value_ids': value_nom_francais[0]}],
                                       # [0, False, {u'attribute_id': xml_modele_etiquette.id, u'value_ids': value_modele_etiquette[0]}],
                                       # [0, False, {u'attribute_id': xml_hauteur_mm.id, u'value_ids': value_hauteur_mm[0]}],
                                       # [0, False, {u'attribute_id': xml_poids_brut.id, u'value_ids': value_poids_brut[0]}],
                                       # [0, False, {u'attribute_id': xml_ca_n.id, u'value_ids': value_ca_n[0]}],
                                       # [0, False, {u'attribute_id': xml_ca_n_1.id, u'value_ids': value_ca_n_1[0]}],
                                       # [0, False, {u'attribute_id': xml_ca_n_2.id, u'value_ids': value_ca_n_2[0]}],
                                       # [0, False, {u'attribute_id': xml_qte_n.id, u'value_ids': value_qte_n[0]}],
                                       # [0, False, {u'attribute_id': xml_qte_n_1.id, u'value_ids': value_qte_n_1[0]}],
                                       # [0, False, {u'attribute_id': xml_qte_n_2.id, u'value_ids': value_qte_n_2[0]}],
                                       # [0, False, {u'attribute_id': xml_critere_18.id, u'value_ids': value_critere_18[0]}],
                                       # [0, False, {u'attribute_id': xml_sous_famille_article.id, u'value_ids': value_sous_famille_article[0]}],
                                       # [0, False, {u'attribute_id': xml_pays_d_origine.id, u'value_ids': value_pays_d_origine[0]}],
                                       # [0, False, {u'attribute_id': xml_fourn_principal.id, u'value_ids': value_fourn_principal[0]}],
                                       ], #attributes
                # 'uom_id': 1,
                # 'property_account_income_id': False,
                # 'description_purchase': False,
                'n_article': n_article_0,  # N_Article
                # 'message_ids': False,
                'sale_ok': True,
                # 'item_ids': [],
                # 'description_picking': False,
                # 'purchase_method': 'receive',
                'purchase_ok': True,
                # 'sale_delay': 7,
                # 'company_id': 1,
                # 'property_valuation': False,
                'track_service': 'manual',
                # 'uom_po_id': 1,
                # 'property_cost_method': False,
                'type': u'consu',
                # 'property_stock_account_input': False,
                # 'property_stock_production': 7,
                # 'supplier_taxes_id': [[6, False, [11]]],
                'volume': 0,
                # 'route_ids': [[6, False, [8]]],
                'tracking': u'none',
                # 'description_sale': False,
                'active': True,
                # 'property_stock_inventory': 5,
                # 'cost_method': False,
                # 'valuation': False,
                # 'image_medium': False,
                'name': libell_commercial_20,  # name
                # 'property_account_expense_id': False,
                'famille': famille_12,
                'libelle_commercial': libell_commercial_20,
                # 'categ_id': categ,
                'packaging_ids': [],
                'invoice_policy': u'delivery',
                'taxes_id': [[6, False, taxe_id]],
                # 'property_stock_account_output': False,
                'seller_ids': [],
                'default_code': code_article_1,
                'list_price': prix_etiquette_24,  # Prix_Etiquette
                'barcode': code_barre_2,  # Code_Barre
                'weight': poids_brut_29,  # Poids_Brut
                'importe': True,
            }

            # timestamp6 = time.time()
            # ec3 = timestamp6 - timestamp5
            #
            # _logger.info("mapping minimum Términé: %.2f " %(ec3) )
            #
            # timestamp7 = time.time()

            print "n_aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa"
            print valuesp.get('n_article')

            #pour les attributs
            obj_template = self.env['product.template'].search([('libelle_commercial','=',libell_commercial_20)])

			#logger ajouté
			#print "obj_template"
            #print obj_template
            _logger.info("create(self, values): %r" % obj_template)

            if obj_template.id :
                name = libell_commercial_20 + " " + _taille_11 + " - " + nom_fran_ais_21

                for al in obj_template.attribute_line_ids:
                    if al.attribute_id.id == xml_genre.id:
						#logger_ajoutéf
						#print "al.value_ids bef"
                        #print al.value_ids
                        _logger.info("create(self, values): %r" % al.value_ids)

						#logger_ajouté
						#print "value_genre[1]"
                        #print value_genre[1]
                        _logger.info("create(self, values): %r" % value_genre[1])

                        al.value_ids = al.value_ids + value_genre[1]

						#logger_ajouté
						#print "al.value_ids"
                        #print al.value_ids
                        _logger.info("create(self, values): %r" % al.value_ids)

                    if al.attribute_id.id == xml_espece.id:
                        al.value_ids = al.value_ids + value_espece[1]

                    if al.attribute_id.id == xml_variete.id:
                        al.value_ids = al.value_ids + value_variete[1]

                    if al.attribute_id.id == xml_taille.id:
                        al.value_ids = al.value_ids + value_taille[1]

                    if al.attribute_id.id == xml_taille_bis.id:
                        al.value_ids = al.value_ids + value_taille_bis[1]

                    if al.attribute_id.id == xml_type_de_feuillage.id:
                        al.value_ids = al.value_ids + value_type_de_feuillage[1]

                    if al.attribute_id.id == xml_critere_7.id:
                        al.value_ids = al.value_ids + value_critere_7[1]

                    if al.attribute_id.id == xml_critere_8.id:
                        al.value_ids = al.value_ids + value_critere_8[1]

                    if al.attribute_id.id == xml_critere_9.id:
                        al.value_ids = al.value_ids + value_critere_9[1]

                    if al.attribute_id.id == xml_critere_18.id:
                        al.value_ids = al.value_ids + value_critere_18[1]

                    if al.attribute_id.id == xml_nom_francais.id:
                        al.value_ids = al.value_ids + value_nom_francais[1]

                    if al.attribute_id.id == xml_modele_etiquette.id:
                        al.value_ids = al.value_ids + value_modele_etiquette[1]

                    if al.attribute_id.id == xml_hauteur_mm.id:
                        al.value_ids = al.value_ids + value_hauteur_mm[1]

                    if al.attribute_id.id == xml_poids_brut.id:
                        al.value_ids = al.value_ids + value_poids_brut[1]

                    if al.attribute_id.id == xml_ca_n.id:
                        al.value_ids = al.value_ids + value_ca_n[1]

                    if al.attribute_id.id == xml_ca_n_1.id:
                        al.value_ids = al.value_ids + value_ca_n_1[1]

                    if al.attribute_id.id == xml_ca_n_2.id:
                        al.value_ids = al.value_ids + value_ca_n_2[1]

                    if al.attribute_id.id == xml_qte_n.id:
                        al.value_ids = al.value_ids + value_qte_n[1]

                    if al.attribute_id.id == xml_qte_n_1.id:
                        al.value_ids = al.value_ids + value_qte_n_1[1]

                    if al.attribute_id.id == xml_qte_n_2.id:
                        al.value_ids = al.value_ids + value_qte_n_2[1]

                    if al.attribute_id.id == xml_sous_famille_article.id:
                        al.value_ids = al.value_ids + value_sous_famille_article[1]

                    if al.attribute_id.id == xml_pays_d_origine.id:
                        al.value_ids = al.value_ids + value_pays_d_origine[1]

                    if al.attribute_id.id == xml_fourn_principal.id:
                        al.value_ids = al.value_ids + value_fourn_principal[1]
                obj_template.create_variant_ids()
                record_product_last = obj_template.product_variant_ids.ids

                #testé et approuvé ! il faut bien prende the last one

                #lent = len(record_product_last)
                #last = record_product_last[lent - 1]
                last = record_product_last[-1]

                last_product = self.env['product.product'].browse(last)

                #dict product product

                valuespp = {
                    #'warranty': 0,
                    #'message_follower_ids': False,
                    #'property_account_creditor_price_difference': False,
                    #'standard_price': 0,
                    #'attribute_line_ids': [],
                    #'uom_id': 1,
                    #'property_account_income_id': False,
                    #'description_purchase': False,
                    'n_article': n_article_0, #N_Article
                    #'message_ids': False,
                    'sale_ok': True,
                    #'item_ids': [],
                    #'description_picking': False,
                    #'purchase_method': 'receive',
                    'purchase_ok': True,
                    #'sale_delay': 7,
                    #'company_id': 1,
                    #'property_valuation': False,
                    'track_service': 'manual',
                    #'uom_po_id': 1,
                    #'property_cost_method': False,
                    'type': u'consu',
                    #'property_stock_account_input': False,
                    #'property_stock_production': 7,
                    #'supplier_taxes_id': [[6, False, [11]]],
                    'volume': 0,
                    #'route_ids': [[6, False, [8]]],
                    'tracking': u'none',
                    #'description_sale': False,
                    'active': True,
                    #'property_stock_inventory': 5,
                    #'cost_method': False,
                    #'valuation': False,
                    #'image_medium': False,
                    'name_puthod': libell_commercial_20 + " " + _taille_11 + " - " +nom_fran_ais_21,# name
                    #'property_account_expense_id': False,
                    'famille_p' : famille_12,
                    #'categ_id': categ,
                    'packaging_ids': [],
                    'invoice_policy': u'delivery',
                    'taxes_id': [[6, False, taxe_id]],
                    #'property_stock_account_output': False,
                    'seller_ids': [],
                    'lst_price': prix_etiquette_24 , #Prix_Etiquette
                    'barcode': code_barre_2 , #Code_Barre
                    'weight' : poids_brut_29 , #Poids_Brut
                    'default_code': code_article_1,
                    #'importe' : True,
                    'marque_savoie' : marque_savoie_7,
                    }

                last_product.write(valuespp)
                obj_product = self.env['product.product'].search([('barcode','=',False),('importe','=',True)])
                if obj_product:
                    print "ici active not"
                    for op in obj_product:
                        print "oooooooooooooooooop"
                        print op
                        op.write({'active': False ,})

                #on peut compute sur les valeurs concérné et fixer le n_article

                #logger ajouté
				#print "record_product last"
                #print last
                _logger.info("create(self, values): %r " %(last))
				
            else :
                print "iciiiiiiiiiii creation"
                print "n_aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa creas"
                print valuesp.get('n_article')
                self.env['product.template'].create(valuesp)



            # timestamp8 = time.time()
            # ec4 = timestamp8 - timestamp7
            # timestamp2 = time.time()
            # timestamp = timestamp2 - timestamp1
            # timestampadd = timestampadd + timestamp
            # print "This took %.2f seconds" % (timestampadd)
            # print "Record " + str(count)
            # _logger.info("Objet product_product créé: %.2f " %(ec4))

            return record

    @api.multi
    def write(self, values):
        print "values"
        print values

        record = super(TmpArticle, self).write(values)

        print "values"
        print values

        obj_product = self.env['product.product'].search([('barcode', '=', False), ('importe', '=', True)])
        if obj_product:
            print "ici active not"
            for op in obj_product:
                print "oooooooooooooooooop"
                print op
                op.write({'active': False, })
        # attributs id
        xml_genre = self.env.ref("darb_puthod.product_attribute_genre")
        xml_espece = self.env.ref("darb_puthod.product_attribute_espece")
        xml_variete = self.env.ref("darb_puthod.product_attribute_variete")
        xml_taille = self.env.ref("darb_puthod.product_attribute_taille")
        xml_taille_bis = self.env.ref("darb_puthod.product_attribute_taille_bis")
        xml_type_de_feuillage = self.env.ref("darb_puthod.product_attribute_type_de_feuillage")
        xml_critere_7 = self.env.ref("darb_puthod.product_attribute_critere_7")
        xml_critere_8 = self.env.ref("darb_puthod.product_attribute_critere_8")
        xml_critere_9 = self.env.ref("darb_puthod.product_attribute_critere_9")
        xml_nom_francais = self.env.ref("darb_puthod.product_attribute_nom_francais")
        xml_modele_etiquette = self.env.ref("darb_puthod.product_attribute_modele_etiquette")
        xml_hauteur_mm = self.env.ref("darb_puthod.product_attribute_hauteur_mm")
        xml_poids_brut = self.env.ref("darb_puthod.product_attribute_poids_brut")
        xml_ca_n = self.env.ref("darb_puthod.product_attribute_ca_n")
        xml_ca_n_1 = self.env.ref("darb_puthod.product_attribute_ca_n_1")
        xml_ca_n_2 = self.env.ref("darb_puthod.product_attribute_ca_n_2")
        xml_qte_n = self.env.ref("darb_puthod.product_attribute_qte_n")
        xml_qte_n_1 = self.env.ref("darb_puthod.product_attribute_qte_n_1")
        xml_qte_n_2 = self.env.ref("darb_puthod.product_attribute_qte_n_2")
        xml_critere_18 = self.env.ref("darb_puthod.product_attribute_critere_18")
        xml_sous_famille_article = self.env.ref("darb_puthod.product_attribute_sous_famille_article")
        xml_pays_d_origine = self.env.ref("darb_puthod.product_attribute_pays_d_origine")
        xml_fourn_principal = self.env.ref("darb_puthod.product_attribute_fourn_principal")

        # attribute values

        genre = self.is_empty_char(values.get('genre_3'))
        espece = self.is_empty_char(values.get('espece_4'))
        variete = self.is_empty_char(values.get('variete_5'))
        taille = self.is_empty_char(values.get('taille_10'))
        taille_bis = self.is_empty_char(values.get('_taille_11'))
        type_de_feuillage = self.is_empty_char(values.get('type_de_feuillage_14'))
        critere_7 = self.is_empty_char(values.get('crit_re_7_17'))
        critere_8 = self.is_empty_char(values.get('crit_re_8_18'))
        critere_9 = self.is_empty_char(values.get('crit_re_9_19'))
        nom_francais = self.is_empty_char(values.get('nom_fran_ais_21'))
        modele_etiquette = self.is_empty_char(values.get('mod_le_tiquette_23'))
        hauteur_mm = self.is_empty_char(values.get('hauteur_mm_28'))
        poids_brut = self.is_empty_char(values.get('poids_brut_29'))
        ca_n = self.is_empty_char(values.get('ca_n_33'))
        ca_n_1 = self.is_empty_char(values.get('ca_n_1_34'))
        ca_n_2 = self.is_empty_char(values.get('ca_n_2_35'))
        qte_n = self.is_empty_char(values.get('qt_n_36'))
        qte_n_1 = self.is_empty_char(values.get('qt_n_1_37'))
        qte_n_2 = self.is_empty_char(values.get('qt_n_2_38'))
        critere_18 = self.is_empty_char(values.get('crit_re_18_55'))
        sous_famille_article = self.is_empty_char(values.get('sous_famille_article_59'))
        pays_d_origine = self.is_empty_char(values.get('pays_d_origine_60'))
        fourn_principal = self.is_empty_char(values.get('fourn_principal_83'))

        # check values or create
        value_genre = self.check_value(genre, xml_genre)
        value_fourn_principal = self.check_value(fourn_principal, xml_fourn_principal)
        value_pays_d_origine = self.check_value(pays_d_origine, xml_pays_d_origine)
        value_sous_famille_article = self.check_value(sous_famille_article, xml_sous_famille_article)
        value_qte_n = self.check_value(qte_n, xml_qte_n)
        value_qte_n_1 = self.check_value(qte_n_1, xml_qte_n_1)
        value_qte_n_2 = self.check_value(qte_n_2, xml_qte_n_2)
        value_ca_n = self.check_value(ca_n, xml_ca_n)
        value_ca_n_1 = self.check_value(ca_n_1, xml_ca_n_1)
        value_ca_n_2 = self.check_value(ca_n_2, xml_ca_n_2)
        value_poids_brut = self.check_value(poids_brut, xml_poids_brut)
        value_hauteur_mm = self.check_value(hauteur_mm, xml_hauteur_mm)
        value_modele_etiquette = self.check_value(modele_etiquette, xml_modele_etiquette)
        value_nom_francais = self.check_value(nom_francais, xml_nom_francais)
        value_critere_7 = self.check_value(critere_7, xml_critere_7)
        value_critere_8 = self.check_value(critere_8, xml_critere_8)
        value_critere_18 = self.check_value(critere_18, xml_critere_18)
        value_critere_9 = self.check_value(critere_9, xml_critere_9)
        value_type_de_feuillage = self.check_value(type_de_feuillage, xml_type_de_feuillage)
        value_taille_bis = self.check_value(taille_bis, xml_taille_bis)
        value_taille = self.check_value(taille, xml_taille)
        value_variete = self.check_value(variete, xml_variete)
        value_espece = self.check_value(espece, xml_espece)

        nom_fran_ais_21 = self.is_empty_char(values.get('nom_fran_ais_21'))
        libell_commercial_20 = self.is_empty_char(values.get('libell_commercial_20'))
        _taille_11 = self.is_empty_char(values.get('_taille_11'))
        famille_12 = self.is_empty_char(values.get('famille_12'))

        prix_etiquette_24 = self.is_empty_float(values.get('prix_etiquette_24'))
        poids_brut_29 = self.is_empty_float(values.get('poids_brut_29'))

        code_barre_2 = self.is_empty_char(values.get('code_barre_2'))
        code_article_1 = self.is_empty_char(values.get('code_article_1'))
        n_article_0 = self.is_empty_char(values.get('n_article_0'))
        marque_savoie_7 = self.is_empty_char(values.get('marque_savoie_7'))

        TVA = self.is_empty_float(values.get('tva_27'))
        taxe_id = []

        if TVA == 4:
            taxe_id = self.env['account.tax'].search([('amount', '=', '10')]).ids
        elif TVA == 2:
            taxe_id = self.env['account.tax'].search([('amount', '=', '20')]).ids

            #dict product template

            valuesp = {
                # 'warranty': 0,
                # 'message_follower_ids': False,
                # 'property_account_creditor_price_difference': False,
                # 'standard_price': 0,
                'attribute_line_ids': [[0, False, {u'attribute_id': xml_genre.id, u'value_ids': value_genre[0]}],
                                       [0, False, {u'attribute_id': xml_espece.id, u'value_ids': value_espece[0]}],
                                       [0, False, {u'attribute_id': xml_variete.id, u'value_ids': value_variete[0]}],
                                       # [0, False, {u'attribute_id': xml_taille.id, u'value_ids': value_taille[0]}],
                                       [0, False,
                                        {u'attribute_id': xml_taille_bis.id, u'value_ids': value_taille_bis[0]}],
                                       # [0, False, {u'attribute_id': xml_type_de_feuillage.id, u'value_ids': value_type_de_feuillage[0]}],
                                       # [0, False, {u'attribute_id': xml_critere_7.id, u'value_ids': value_critere_7[0]}],
                                       # [0, False, {u'attribute_id': xml_critere_8.id, u'value_ids': value_critere_8[0]}],
                                       # [0, False, {u'attribute_id': xml_critere_9.id, u'value_ids': value_critere_9[0]}],
                                       # [0, False, {u'attribute_id': xml_nom_francais.id, u'value_ids': value_nom_francais[0]}],
                                       # [0, False, {u'attribute_id': xml_modele_etiquette.id, u'value_ids': value_modele_etiquette[0]}],
                                       # [0, False, {u'attribute_id': xml_hauteur_mm.id, u'value_ids': value_hauteur_mm[0]}],
                                       # [0, False, {u'attribute_id': xml_poids_brut.id, u'value_ids': value_poids_brut[0]}],
                                       # [0, False, {u'attribute_id': xml_ca_n.id, u'value_ids': value_ca_n[0]}],
                                       # [0, False, {u'attribute_id': xml_ca_n_1.id, u'value_ids': value_ca_n_1[0]}],
                                       # [0, False, {u'attribute_id': xml_ca_n_2.id, u'value_ids': value_ca_n_2[0]}],
                                       # [0, False, {u'attribute_id': xml_qte_n.id, u'value_ids': value_qte_n[0]}],
                                       # [0, False, {u'attribute_id': xml_qte_n_1.id, u'value_ids': value_qte_n_1[0]}],
                                       # [0, False, {u'attribute_id': xml_qte_n_2.id, u'value_ids': value_qte_n_2[0]}],
                                       # [0, False, {u'attribute_id': xml_critere_18.id, u'value_ids': value_critere_18[0]}],
                                       # [0, False, {u'attribute_id': xml_sous_famille_article.id, u'value_ids': value_sous_famille_article[0]}],
                                       # [0, False, {u'attribute_id': xml_pays_d_origine.id, u'value_ids': value_pays_d_origine[0]}],
                                       # [0, False, {u'attribute_id': xml_fourn_principal.id, u'value_ids': value_fourn_principal[0]}],
                                       ],  # attributes
                # 'uom_id': 1,
                # 'property_account_income_id': False,
                # 'description_purchase': False,
                'n_article': n_article_0,  # N_Article
                # 'message_ids': False,
                'sale_ok': True,
                # 'item_ids': [],
                # 'description_picking': False,
                # 'purchase_method': 'receive',
                'purchase_ok': True,
                # 'sale_delay': 7,
                # 'company_id': 1,
                # 'property_valuation': False,
                'track_service': 'manual',
                # 'uom_po_id': 1,
                # 'property_cost_method': False,
                'type': u'consu',
                # 'property_stock_account_input': False,
                # 'property_stock_production': 7,
                # 'supplier_taxes_id': [[6, False, [11]]],
                'volume': 0,
                # 'route_ids': [[6, False, [8]]],
                'tracking': u'none',
                # 'description_sale': False,
                'active': True,
                # 'property_stock_inventory': 5,
                # 'cost_method': False,
                # 'valuation': False,
                # 'image_medium': False,
                'name': libell_commercial_20,  # name
                # 'property_account_expense_id': False,
                'famille': famille_12,
                'libelle_commercial': libell_commercial_20,
                # 'categ_id': categ,
                'packaging_ids': [],
                'invoice_policy': u'delivery',
                'taxes_id': [[6, False, taxe_id]],
                # 'property_stock_account_output': False,
                'seller_ids': [],
                'default_code': code_article_1,
                'list_price': prix_etiquette_24,  # Prix_Etiquette
                'barcode': code_barre_2,  # Code_Barre
                'weight': poids_brut_29,  # Poids_Brut
                'importe': True,
            }

            obj_trmplate_write = self.env['product.template'].search([('n_article', '=', n_article_0)])
            if obj_trmplate_write:
                obj_trmplate_write.write(valuesp)
            else:
                print "product template write not"


            # dict product product

            valuespp = {
                # 'warranty': 0,
                # 'message_follower_ids': False,
                # 'property_account_creditor_price_difference': False,
                # 'standard_price': 0,
                # 'attribute_line_ids': [],
                # 'uom_id': 1,
                # 'property_account_income_id': False,
                # 'description_purchase': False,
                'n_article': n_article_0,  # N_Article
                # 'message_ids': False,
                'sale_ok': True,
                # 'item_ids': [],
                # 'description_picking': False,
                # 'purchase_method': 'receive',
                'purchase_ok': True,
                # 'sale_delay': 7,
                # 'company_id': 1,
                # 'property_valuation': False,
                'track_service': 'manual',
                # 'uom_po_id': 1,
                # 'property_cost_method': False,
                'type': u'consu',
                # 'property_stock_account_input': False,
                # 'property_stock_production': 7,
                # 'supplier_taxes_id': [[6, False, [11]]],
                'volume': 0,
                # 'route_ids': [[6, False, [8]]],
                'tracking': u'none',
                # 'description_sale': False,
                'active': True,
                # 'property_stock_inventory': 5,
                # 'cost_method': False,
                # 'valuation': False,
                # 'image_medium': False,
                'name_puthod': libell_commercial_20 + " " + _taille_11 + " - " + nom_fran_ais_21,  # name
                # 'property_account_expense_id': False,
                'famille_p': famille_12,
                # 'categ_id': categ,
                'packaging_ids': [],
                'invoice_policy': u'delivery',
                'taxes_id': [[6, False, taxe_id]],
                # 'property_stock_account_output': False,
                'seller_ids': [],
                'lst_price': prix_etiquette_24,  # Prix_Etiquette
                'barcode': code_barre_2,  # Code_Barre
                'weight': poids_brut_29,  # Poids_Brut
                'default_code': code_article_1,
                # 'importe' : True,
                'marque_savoie': marque_savoie_7,
            }

            obj_product_write = self.env['product.product'].search([('n_article', '=', n_article_0)])
            if obj_product_write:
                obj_product_write.write(valuespp)
            else:
                print "product product write not"
                print n_article_0

        return record


class ProductTemplate(models.Model):
    _inherit = 'product.template'

    @api.model
    def create(self, values):  # Cette fonction retourne super(ProductTemplate, self).create(values)
        _logger.info("create(self, values): " + str(values))
        return super(ProductTemplate, self).create(values)

class ProductProduct(models.Model):
    _inherit = 'product.product'

    @api.model
    def create(self, values):  # Cette fonction retourne super(ProductProduct, self).create(values)
        _logger.info("create(self, values): " + str(values))

        record = super(ProductProduct, self).create(values)

        #logger ajouté
		#print "record product"
        #print record
        _logger.info("create(self, values): %r " %(record))

        return record



class Partner(models.Model):
    _inherit = 'product.attribute.value'

    @api.model
    def create(self, values):  # Cette fonction retourne super(Partner, self).create(values) 
        _logger.info("create(self, values): " + str(values))
        return super(Partner, self).create(values)

class Partner_attribute(models.Model):
    _inherit = 'product.attribute'

    @api.model
    def create(self, values):  # Cette fonction retourne super(Partner_attribute, self).create(values)
        _logger.info("create(self, values): " + str(values))
        return super(Partner_attribute, self).create(values)
