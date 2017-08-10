# -*- coding: utf-8 -*-
from openerp import api, fields, models
import collections
import logging
_logger = logging.getLogger(__name__)

class EntretienReport(models.AbstractModel):
    _name = 'report.darb_puthod.report_entretien'

    @api.multi
    def col(products):
        counter = collections.Counter(products)
        #logger ajouté
		#print(counter)
        _logger.info("col(products): %r" % counter)
        return counter

    @api.multi
    def a_faire(self,doc,tache):

        e = []

        count = 0
        #logger ajouté
        #print "counttttttttttttttt"
        #print count
        _logger.info("a_faire(self,doc,tache): %r" % count)		

        fiches = self.env['fiche.chantier'].search([('chantier_id','=',doc.id)])
        
        #logger ajouté
        #print "fichessssssssssssssss"
        #print fiches
        _logger.info("a_faire(self,doc,tache): %r" % fiches)
        
        #logger ajouté		
		#print "tacheeeeeeeeeeeeeeeee"
        #print tache.id
        _logger.info("a_faire(self,doc,tache): %r" % tache.id)         
        
        if fiches:

            for f in fiches:
                if f :
                    for s in f.subtasks:
                        #logger ajouté
						#print "subtasksssssssssssssssss"
                        #print s.subtask_id
                        _logger.info("a_faire(self,doc,tache): %r" % s.subtask_id)
                        if s.subtask_id.id == tache.id:
                            count = count + 1
                            if s.employee_subtask_ids.ids:
                                for tmp in s.employee_subtask_ids.ids:
                                    e.append(self.env['employees.subtasks'].browse(tmp))
                else: break
        #logger ajouté
		#print "counttttttttttttttt2"
        #print count
		_logger.info("a_faire(self,doc,tache): %r" % count)

        #print "subtaskssssssssssssssssse"
        #print e
        _logger.info("a_faire(self,doc,tache): %r" % e)
        
        return count,e

    @api.multi
    def render_html(self, data=None):
        report = self.env['report']._get_report_from_name('darb_puthod.report_entretien')

        docargs = {
            'doc_ids': self._ids,
            'doc_model': report.model,
            'docs': self.env['chantier'].browse(self._ids),
            'a_faire': self.a_faire,
            }

        return self.env['report'].render('darb_puthod.report_entretien', docargs)