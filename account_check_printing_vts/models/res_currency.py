import logging
import math
import re
import time
import traceback

from odoo import api, fields, models, tools, _

_logger = logging.getLogger(__name__)

try:
    from num2words import num2words
except ImportError:
    _logger.warning("The num2words python library is not installed, amount-to-text features won't be fully available.")
    num2words = None

CURRENCY_DISPLAY_PATTERN = re.compile(r'(\w+)\s*(?:\((.*)\))?')

from odoo.addons.base.models.res_currency import Currency

@api.multi
def amount_to_text(self, amount):
    self.ensure_one()
    def _num2words(number, lang):
        try:
            return num2words(number, lang=lang).title()
        except NotImplementedError:
            return num2words(number, lang='en').title()

    if num2words is None:
        logging.getLogger(__name__).warning("The library 'num2words' is missing, cannot render textual amounts.")
        return ""
    
    
    
    formatted = "%.{0}f".format(2) % amount
    parts = formatted.partition('.')
    integer_value = int(parts[0])
    fractional_value = (parts[2] or 0)
     
    
    lang_code = self.env.context.get('lang') or self.env.user.lang
    lang = self.env['res.lang'].search([('code', '=', lang_code)])
    amount_words = tools.ustr('{amt_value} {amt_word}').format(
                    amt_value=_num2words(integer_value, lang=lang.iso_code),
                    amt_word=self.currency_unit_label,
                    )
    if not self.is_zero(amount - integer_value):
        amount_words += ' '  + str(fractional_value) +'/100 M.N.'
    else:
        amount_words += ' 00/100 M.N.'
#         amount_words += ' ' + _('and') + tools.ustr(' {amt_value} {amt_word}').format(
#                     amt_value=_num2words(fractional_value, lang=lang.iso_code),
#                     amt_word=self.currency_subunit_label,
#                     )
    return amount_words

Currency.amount_to_text=amount_to_text