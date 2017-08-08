#!/usr/bin/python
# coding: utf8
from openerp import fields, models, api, _
import logging
import time
_logger = logging.getLogger(__name__)

class TmpArticle(models.Model):

    _name = 'tmparticle'
    _rec_name = 'N_Article'
    N_Article = fields.Char("N° Article")
    Code_article = fields.Char("Code article")
    Code_Barre = fields.Char("Code Barre")
    Genre = fields.Char("Genre")
    Espece = fields.Char("Espece")
    Variete = fields.Char("Variete")
    Catalogue = fields.Char("Catalogue")
    Marque_Savoie = fields.Char("Marque Savoie")
    Presentation = fields.Char("Présentation")
    Presentation_bis = fields.Char("Présentation")
    Taille = fields.Char("Taille")
    Taille_bis = fields.Char("Taille importé")
    Famille = fields.Char("Famille")
    tarif = fields.Char("tarif")
    type_de_feuillage = fields.Char("type de feuillage")
    Famille_Presta = fields.Char("Famille/Presta")
    Promo_automne = fields.Char("Promo automne")
    Critere_7 = fields.Char("Critère 7")
    Critere_8 = fields.Char("Critère 8")
    Critere_9 = fields.Char("Critère 9")
    Libelle_commercial = fields.Char("Libellé commercial")
    Nom_francais = fields.Char("Nom français")
    N_conseil = fields.Char("N° conseil")
    Modele_etiquette = fields.Char("Modèle étiquette")
    Prix_Etiquette = fields.Char("Prix Etiquette")
    Code_comptable = fields.Char("Code comptable")
    Remise = fields.Char("Remise")
    TVA = fields.Char("TVA")
    Hauteur_mm = fields.Char("Hauteur mm")
    Poids_Brut = fields.Char("Poids Brut")
    Complement = fields.Char("Complément")
    Code_vente = fields.Char("Code vente")
    Conditionnement = fields.Char("Conditionnement")
    CA_N = fields.Char("CA N")
    CA_N_1 = fields.Char("CA N-1")
    CA_N_2 = fields.Char("CA N-2")
    Qte_N = fields.Char("Qté N")
    Qte_N_1 = fields.Char("Qté N-1")
    Qte_N_2 = fields.Char("Qté N-2")
    Masquer_dans_les_listes = fields.Char("Masquer dans les listes")
    Date_de_creation = fields.Char("Date de création")
    Derniere_modification = fields.Char("Dernière modification")
    Groupe_tarifaire = fields.Char("Groupe tarifaire")
    N_article_destockage = fields.Char("N° article déstockage")
    Coeff_destockage = fields.Char("Coeff. déstockage")
    Poids_Net = fields.Char("Poids Net")
    Type_fiscal = fields.Char("Type fiscal")
    Critere_10 = fields.Char("Critère 10")
    Critere_11 = fields.Char("Critère 11")
    Critere_12 = fields.Char("Critère 12")
    Critere_13 = fields.Char("Critère 13")
    Critere_14 = fields.Char("Critère 14")
    Critere_15 = fields.Char("Critère 15")
    Critere_16 = fields.Char("Critère 16")
    Critere_17 = fields.Char("Critère 17")
    Critere_18 = fields.Char("Critère 18")
    Gestion_du_stock = fields.Char("Gestion du stock")
    Unite_de_tarification = fields.Char("Unité de tarification")
    Sur_Appellation = fields.Char("Sur Appellation")
    Sous_Famille_article = fields.Char("Sous Famille article")
    Pays_d_origine = fields.Char("Pays d'origine")
    CA_N_Fourn = fields.Char("CA N Fourn.")
    CA_N_1_Fourn = fields.Char("CA N-1 Fourn.")
    CA_N_2_Fourn = fields.Char("CA N-2 Fourn.")
    Qte_N_bis = fields.Char("Qté N")
    Qte_N_1_bis = fields.Char("Qté N-1")
    Qte_N_2_bis = fields.Char("Qté N-2")
    CA_N_A_Nouveau = fields.Char("CA N A-Nouveau")
    Qte_N_A_Nouveau = fields.Char("Qté N A-Nouveau")
    Qte_N_Fourn_A_Nouveau = fields.Char("Qté N Fourn. A-Nouveau")
    CA_N_Fourn_A_Nouveau = fields.Char("CA N Fourn. A-Nouveau")
    Domaine_util_achat = fields.Char("Domaine util. achat")
    Domaine_util_vente = fields.Char("Domaine util. vente")
    Taux_prix_achat = fields.Char("Taux prix achat")
    Code_achat = fields.Char("Code achat")
    PCB_Article = fields.Char("PCB Artifcle")
    Origine = fields.Char("Origine")
    Prix_ref_marge = fields.Char("Prix ref marge")
    Code_Barre_2 = fields.Char("code barre 2")
    Gestion_de_Facteur = fields.Char("Gestion de Facteur")
    Code_Facteur = fields.Char("Code Facteur")
    Remplace_par = fields.Char("Remplacé par")
    N_Proprietaire = fields.Char("N° Propriétaire")
    Fourn_principal = fields.Char("Fourn. principal")
    Date_de_fin_d_achat = fields.Char("Date de fin d'achat")
    No_FPP = fields.Char("No FPP")
    Coef_FPP = fields.Char("Coef. FPP")
    Sem_Deb_Validite = fields.Char("Sem. Deb. Validité")
    Sem_Fin_Validite = fields.Char("Sem. Fin Validité")
    Secteur_par_defaut = fields.Char("Secteur par défaut")
    Critere_20 = fields.Char("Critère 20")
    Critere_21 = fields.Char("Critère 21")
    Commentaire_logistique = fields.Char("Commentaire logistique")
    Identifiant_XOL = fields.Char("Identifiant XOL")
    Article_Totalise = fields.Char("Article Totalisé")
    N_Article_Totalisateur = fields.Char("N° Article Totalisateur")
    Article_Financier = fields.Char("Article Financier")




    @api.multi
    def is_empty_char(self,value):
        if value:
            return value
        else:
            return ""

    @api.multi
    def is_empty_float(self,value):
        if value:
            return float(value)
        else:
            return 0


    @api.model
    def create(self, values):
            count = 0
            time.time()
            timestamp1 = time.time()
            #create tmparticle
            record = super(TmpArticle, self).create(values)
            timestamp2 = time.time()
            ec1 = timestamp2 -timestamp1
            _logger.info("Objet TMPARTICLE créé: %.2f" %(ec1))
            timestamp3 = time.time()

            Nom_francais = self.is_empty_char(values.get('Nom_francais'))
            Libelle_commercial = self.is_empty_char(values.get('Libelle_commercial'))
            Taille_bis = self.is_empty_char(values.get('Taille_bis'))
            Famille = self.is_empty_char(values.get('Famille'))

            timestamp4 = time.time()
            ec2 = timestamp4 - timestamp3
            _logger.info("Champs obligatoires verifié: %.2f " %(ec2))
            timestamp5 = time.time()

            Prix_Etiquette = self.is_empty_float(values.get('Prix_Etiquette'))
            Poids_Brut = self.is_empty_float(values.get('Poids_Brut'))

            Code_Barre = self.is_empty_char(values.get('Code_Barre'))
            N_Article = self.is_empty_char(values.get('N_Article'))

            TVA = self.is_empty_float(values.get('TVA'))
            taxe_id = []

            if TVA == 4:
                taxe_id = self.env['account.tax'].search([('amount','=','10')]).ids
            elif TVA == 2:
                taxe_id = self.env['account.tax'].search([('amount', '=', '20')]).ids



            # pour les categ
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
            xml_Hauteur_mm = self.env.ref("darb_puthod.product_attribute_Hauteur_mm")
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
            print "xml_record"
            print xml_genre

            valuesp = {
                # 'warranty': 0,
                # 'message_follower_ids': False,
                # 'property_account_creditor_price_difference': False,
                # 'standard_price': 0,
                'attribute_line_ids': [[0, False, {u'attribute_id': xml_genre.id, u'value_ids': []}],
                                       [0, False, {u'attribute_id': xml_espece.id, u'value_ids': []}],
                                       [0, False, {u'attribute_id': xml_variete.id, u'value_ids': []}],
                                       [0, False, {u'attribute_id': xml_taille.id, u'value_ids': []}],
                                       [0, False, {u'attribute_id': xml_taille_bis.id, u'value_ids': []}],
                                       [0, False, {u'attribute_id': xml_type_de_feuillage.id, u'value_ids': []}],
                                       [0, False, {u'attribute_id': xml_critere_7.id, u'value_ids': []}],
                                       [0, False, {u'attribute_id': xml_critere_8.id, u'value_ids': []}],
                                       [0, False, {u'attribute_id': xml_critere_9.id, u'value_ids': []}],
                                       [0, False, {u'attribute_id': xml_nom_francais.id, u'value_ids': []}],
                                       [0, False, {u'attribute_id': xml_modele_etiquette.id, u'value_ids': []}],
                                       [0, False, {u'attribute_id': xml_Hauteur_mm.id, u'value_ids': []}],
                                       [0, False, {u'attribute_id': xml_poids_brut.id, u'value_ids': []}],
                                       [0, False, {u'attribute_id': xml_ca_n.id, u'value_ids': []}],
                                       [0, False, {u'attribute_id': xml_ca_n_1.id, u'value_ids': []}],
                                       [0, False, {u'attribute_id': xml_ca_n_2.id, u'value_ids': []}],
                                       [0, False, {u'attribute_id': xml_qte_n.id, u'value_ids': []}],
                                       [0, False, {u'attribute_id': xml_qte_n_1.id, u'value_ids': []}],
                                       [0, False, {u'attribute_id': xml_qte_n_2.id, u'value_ids': []}],
                                       [0, False, {u'attribute_id': xml_critere_18.id, u'value_ids': []}],
                                       [0, False, {u'attribute_id': xml_sous_famille_article.id, u'value_ids': []}],
                                       [0, False, {u'attribute_id': xml_pays_d_origine.id, u'value_ids': []}],
                                       [0, False, {u'attribute_id': xml_fourn_principal.id, u'value_ids': []}]
                                       ], #attributes
                # 'uom_id': 1,
                # 'property_account_income_id': False,
                # 'description_purchase': False,
                'N_Article': N_Article,  # N_Article
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
                'name': Libelle_commercial + " " + Taille_bis + " - " + Nom_francais,  # name
                # 'property_account_expense_id': False,
                'famille': Famille,
                # 'categ_id': categ,
                'packaging_ids': [],
                'invoice_policy': u'order',
                'taxes_id': [[6, False, taxe_id]],
                # 'property_stock_account_output': False,
                'seller_ids': [],
                'list_price': Prix_Etiquette,  # Prix_Etiquette
                'barcode': Code_Barre,  # Code_Barre
                'weight': Poids_Brut,  # Poids_Brut
                'importe': True,
            }

            # valuesp = {
            #     #'warranty': 0,
            #     #'message_follower_ids': False,
            #     #'property_account_creditor_price_difference': False,
            #     #'standard_price': 0,
            #     #'attribute_line_ids': [],
            #     #'uom_id': 1,
            #     #'property_account_income_id': False,
            #     #'description_purchase': False,
            #     'N_Article': N_Article, #N_Article
            #     #'message_ids': False,
            #     'sale_ok': True,
            #     #'item_ids': [],
            #     #'description_picking': False,
            #     #'purchase_method': 'receive',
            #     'purchase_ok': True,
            #     #'sale_delay': 7,
            #     #'company_id': 1,
            #     #'property_valuation': False,
            #     'track_service': 'manual',
            #     #'uom_po_id': 1,
            #     #'property_cost_method': False,
            #     'type': u'consu',
            #     #'property_stock_account_input': False,
            #     #'property_stock_production': 7,
            #     #'supplier_taxes_id': [[6, False, [11]]],
            #     'volume': 0,
            #     #'route_ids': [[6, False, [8]]],
            #     'tracking': u'none',
            #     #'description_sale': False,
            #     'active': True,
            #     #'property_stock_inventory': 5,
            #     #'cost_method': False,
            #     #'valuation': False,
            #     #'image_medium': False,
            #     'name': Libelle_commercial + " " + Taille_bis + " - " +Nom_francais,# name
            #     #'property_account_expense_id': False,
            #     'famille' : Famille,
            #     #'categ_id': categ,
            #     'packaging_ids': [],
            #     'invoice_policy': u'order',
            #     'taxes_id': [[6, False, taxe_id]],
            #     #'property_stock_account_output': False,
            #     'seller_ids': [],
            #     'lst_price': Prix_Etiquette , #Prix_Etiquette
            #     'barcode': Code_Barre , #Code_Barre
            #     'weight' : Poids_Brut , #Poids_Brut
            #     'importe' : True ,
            #     }

            timestamp6 = time.time()
            ec3 = timestamp6 - timestamp5

            _logger.info("mapping minimum Términé: %.2f " %(ec3) )

            timestamp7 = time.time()

            #pour les attributs
            #self.env['product.product'].create(valuesp)
            #name = Libelle_commercial + " " + Taille_bis + " - " + Nom_francais
            #obj_template = self.env['product.template'].search([('name','=',name)])
            # if not obj_template :
            #     self.env['product.attribute.value'].

            print "obj_template"
            print obj_template

            self.env['product.template'].create(valuesp)



            timestamp8 = time.time()
            ec4 = timestamp8 - timestamp7



            # timestamp2 = time.time()
            # timestamp = timestamp2 - timestamp1
            # timestampadd = timestampadd + timestamp

            # print "This took %.2f seconds" % (timestampadd)
            # print "Record " + str(count)

            count = count + 1

            _logger.info("Objet product_product créé: %.2f " %(ec4))

            return record


# class ProductProduct(models.Model):
#     _inherit = 'product.template'
#
#     @api.model
#     def create(self, values):
#         _logger.info("------------> Article iciiiiiiiiiiiiiiiiiiiiiiii : " + str(values))
#         return super(ProductProduct, self).create(values)
#
# class Partner(models.Model):
#     _inherit = 'product.attribute.value'
#
#     @api.model
#     def create(self, values):
#         _logger.info("------------> Article iciiiiiiiiiiiiiiiiiiiiiiii : " + str(values))
#         return super(Partner, self).create(values)
#
# class Partner_attribute(models.Model):
#     _inherit = 'product.attribute'
#
#     @api.model
#     def create(self, values):
#         _logger.info("------------> Attribute iciiiiiiiiiiiiiiiiiiiiiiii : " + str(values))
#         return super(Partner_attribute, self).create(values)
