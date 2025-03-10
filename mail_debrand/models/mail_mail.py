# Copyright 2019 O4SB - Graeme Gellatly
# Copyright 2019 Tecnativa - Ernesto Tejeda
# Copyright 2020 Onestein - Andrea Stirpe
# Copyright 2024 Modern Logic - Andrew Rahn
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl.html).
from odoo import models


class MailMail(models.AbstractModel):
    _inherit = "mail.mail"

    def _prepare_outgoing_body(self):
        body_html = super()._prepare_outgoing_body()
        return self.env["mail.render.mixin"].remove_href_odoo(
            body_html or "", to_keep=self.body
        )
