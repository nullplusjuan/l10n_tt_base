# Copyright 2026 Joshua D
# SPDX-License-Identifier: AGPL-3.0-or-later
from odoo import fields, models


class L10nTTArea(models.Model):
    _name = "l10n.tt.area"
    _description = "Trinidad and Tobago Area / Community"
    _order = "name"

    name = fields.Char(required=True, index=True)
    state_id = fields.Many2one(
        "res.country.state",
        string="Municipality / Region",
        domain="[('country_id.code', '=', 'TT')]",
        ondelete="restrict",
    )
    active = fields.Boolean(default=True)

    _sql_constraints = [("l10n_tt_area_name_uniq", "unique(name)", "This Trinidad and Tobago area already exists.")]
