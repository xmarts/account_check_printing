from odoo import models, api

from odoo.addons.l10n_ca_check_printing.models.account_payment import account_payment
from odoo.addons.l10n_ca_check_printing.report.print_check import report_print_check 

#@api.multi
def do_print_checks(self):
    if self:
        check_layout = self[0].company_id.account_check_printing_layout
        return self.env.ref('l10n_ca_check_printing.%s' % check_layout).report_action(self)
    return super(account_payment, self).do_print_checks()

account_payment.do_print_checks = do_print_checks

def _check_build_page_info(self, i, p):

    
    month = self.payment_date.strftime("%m")
     

    page = super(report_print_check, self)._check_build_page_info(i, p)
    dia = self.payment_date.strftime("  %d de ")
    mes = switch(int(month))
    year = self.payment_date.strftime(" del %Y")

    date = dia + mes + year



    page.update({
        #'sequence_number': self.check_number if (self.journal_id.check_manual_sequencing and self.check_number != 0) else False,
        'date_label': self.company_id.account_check_printing_date_label,
        'payment_date_canada': date,
        'memo': '',
        'amount': round(self.amount,2),
    #    'payment_date_canada': format_date(self.env, self.payment_date, date_format='yyyy-MM-dd'),
    })
    return page

def switch(m):
    switcher = {
        1: "Enero",
        2: "Febrero",
        3: "Marzo",
        4: "Abril",
        5: "Mayo",
        6: "Junio",
        7: "Julio",
        8: "Agosto",
        9: "Septiembre",
        10: "Octubre",
        11: "Noviembre",
        12: "Diciembre"
    }

    return(switcher.get(m, "Invalid month"))

report_print_check._check_build_page_info = _check_build_page_info