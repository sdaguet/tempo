# -*- coding: utf-8 -*-
from openerp import api,fields,models

import logging
_logger = logging.getLogger(__name__)


			
class sale_order_line(models.Model):

    _inherit = 'sale.order.line'
    price_brut = fields.Float('prix brut HT')
    
