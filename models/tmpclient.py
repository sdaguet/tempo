# -*- coding: utf-8 -*-
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
    Contfichier = fields.Char("(Cont.fichier)")
    altitude_du_jardin = fields.Char("altitude du jardin")
    altitude_du_jardin = fields.Char("(altitude du jardin)")
    surface_du_jardin = fields.Char("surface du jardin")
    surface_du_jardin = fields.Char("(surface du jardin)")
    Critere_4 = fields.Char("Critère 4")
    Critere_4 = fields.Char("(Critère 4)")
    age_du_jardin = fields.Char("âge du jardin")
    age_du_jardin = fields.Char("(âge du jardin)")
    type_de_client = fields.Char("type de client")
    type_de_client = fields.Char("(type de client)")
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
    Code_Postal = fields.Char("Code Postal")
    Ville = fields.Char("Ville")
    Pays = fields.Char("Pays")
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

    @api.model
    def create(self, values):
        record = super(TmpClient, self).create(values)
        Nom_1 = values.get('Nom_1')
        Ville = values.get('Ville')
        Code_Postal = values.get('Code_Postal')
        E_mail = values.get('E_mail')
        URL = values.get('URL')
        FAX = values.get('FAX')
        Telephone = values.get('Telephone')
        Adresse_1 = values.get('Adresse_1')
        Adresse_2 = values.get('Adresse_2')
        N_Client = values.get('N_Client')

        Nom_2 = values.get('Nom_2')
        if Nom_2:
            Nom_2 = Nom_2
        else:
            Nom_2 = ""


        valuesc = {'comment': False,
                   'function': False,
                   'notify_email': 'always',
                   'message_follower_ids': False,
                   'company_type': 'person',
                   # 'property_stock_customer': 9,
                   'street': Adresse_1, #Adresse_1
                   # 'property_account_receivable_id': 227,
                   'property_account_position_id': False,
                   'property_payment_term_id': False,
                   'city': Ville,
                   'user_id': False,
                   'opt_out': False,
                   'zip': Code_Postal, #Code_Postal
                   'title': False,
                   'country_id': False,
                   # 'company_id': 1,
                   'message_ids': False,
                   'parent_id': False,
                   'supplier': False,
                   'property_supplier_payment_term_id': False,
                   'type': 'contact',
                   'email': E_mail, #E_mail
                   'is_company': False,
                   'website': URL, #v
                   'customer': True,
                   'fax': FAX, #FAX
                   'street2': Adresse_2, #Adresse_2
                   'child_ids': [],
                   'phone': Telephone,
                   'user_ids': [],
                   'active': True,
                   'lang': 'fr_FR',
                   # 'property_stock_supplier': 8,
                   'name': Nom_1 + Nom_2, #nom
                   'mobile': False,
                   #'ref': N_Client, #N_Client
                   # 'property_account_payable_id': 292,
                   'state_id': False,
                   'category_id': []}
        #client = self.env['res.partner'].search([('ref','=',self.N_Client)])
        #if client:
         #   _logger.error("Ce Client existe déjà !")
        #else:
        self.env['res.partner'].create(valuesc)
        return record


class Partner(models.Model):
    _inherit = 'res.partner'

    @api.model
    def create(self, values):
        _logger.info("----------------> client iciiiiiiiiiiiiiiiiiiiiiiii : " + str(values))
        return super(Partner, self).create(values)
