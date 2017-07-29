#!/usr/bin/python
# coding: utf8
from openerp import fields, models, api, _
import logging
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
    Qte_N = fields.Char("Qté N")
    Qte_N_1 = fields.Char("Qté N-1")
    Qte_N_2 = fields.Char("Qté N-2")
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
    # code_barre = fields.Char("code barre")
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

    _sql_constraints = [
        ('N_Article_uniq', 'unique(N_Article)', _("A N_Article can only be assigned to one product !")),
    ]

    @api.model
    def create(self, values):
            record = super(TmpArticle, self).create(values)

            Nom_francais = values.get('Nom_francais')
            if Nom_francais:
                Nom_francais = Nom_francais
            else:
                Nom_francais = ""

            Libelle_commercial = values.get('Libelle_commercial')
            if Libelle_commercial:
                Libelle_commercial = Libelle_commercial
            else:
                Libelle_commercial = ""

            Taille_bis = values.get('Taille_bis')
            if Taille_bis:
                Taille_bis = Taille_bis
            else:
                Taille_bis = ""


            #tarif = float(values.get('tarif'))
            Prix_Etiquette = float(values.get('Prix_Etiquette'))
            #Code_Barre = values.get('Code_Barre')
            Poids_Brut = float(values.get('Poids_Brut'))
            #N_Article = int(values.get('N_Article'))
            valuesp = {
                #'warranty': 0,
                #'property_stock_procurement': 6,
                'message_follower_ids': False,
                'property_account_creditor_price_difference': False,
                #'standard_price': 0,
                'attribute_line_ids': [],
                #'uom_id': 1,
                'property_account_income_id': False,
                'description_purchase': False,
                'N_Article_id': record.id, #N_Article
                'message_ids': False,
                'sale_ok': True,
                'item_ids': [],
                'description_picking': False,
                'purchase_method': 'receive',
                'purchase_ok': True,
                #'sale_delay': 7,
                #'company_id': 1,
                'property_valuation': False,
                'track_service': 'manual',
                #'uom_po_id': 1,
                'property_cost_method': False,
                'type': u'consu',
                'property_stock_account_input': False,
                #'property_stock_production': 7,
                #'supplier_taxes_id': [[6, False, [11]]],
                'volume': 0,
                #'route_ids': [[6, False, [8]]],
                'tracking': u'none',
                'description_sale': False,
                'active': True,
                #'property_stock_inventory': 5,
                'cost_method': False,
                'valuation': False,
                'image_medium': False,
                'name': Libelle_commercial + " " + Taille_bis + " - " +Nom_francais,# name
                'property_account_expense_id': False,
                #'categ_id': 1,
                'packaging_ids': [],
                'invoice_policy': u'order',
                #'taxes_id': [[6, False, [6]]],
                'property_stock_account_output': False,
                'seller_ids': [],
                'list_price': Prix_Etiquette , #Prix_Etiquette
                # 'barcode': Code_Barre , #Code_Barre
                'weight' : Poids_Brut , #Poids_Brut
                }

            self.env['product.template'].create(valuesp)
            return record


class ProductTemplate(models.Model):
    _inherit = 'product.template'

    # @api.model
    # def create(self, values):
    #     _logger.info("------------> Article iciiiiiiiiiiiiiiiiiiiiiiii : " + str(values))
    #     return super(ProductTemplate, self).create(values)

class Partner(models.Model):
    _inherit = 'res.partner'

    # @api.model
    # def create(self, values):
    #     _logger.info("------------> Article iciiiiiiiiiiiiiiiiiiiiiiii : " + str(values))
    #     return super(Partner, self).create(values)
