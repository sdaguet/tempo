# -*- coding: utf-8 -*-
from openerp import api, fields, models
from openerp.tools.translate import _
import logging
_logger = logging.getLogger(__name__)

class ProductPuthod(models.Model):
    _inherit = 'product.template'

    # def _get_product_template_type(self, cr, uid, context=None):
    #     res = super(ProductPuthod, self)._get_product_template_type(cr, uid, context=context)
    #     if 'intervention' not in [item[0] for item in res]:
    #         res.append(('intervention', _('Intervention')))
    #         return res




