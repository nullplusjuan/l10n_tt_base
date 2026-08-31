# Copyright 2026 Joshua D
# SPDX-License-Identifier: AGPL-3.0-or-later
from odoo import fields, models


class L10nTTOccupation(models.Model):
    _name = "l10n.tt.occupation"
    _description = "Trinidad and Tobago Occupation"
    _order = "sequence, name"

    name = fields.Char(required=True, index=True)
    code = fields.Char(index=True)
    category = fields.Selection([
        ("management", "Management / Business"),
        ("professional", "Professional"),
        ("technical", "Technical / Associate Professional"),
        ("clerical", "Clerical / Administrative"),
        ("service", "Services / Sales"),
        ("agriculture", "Agriculture / Fisheries"),
        ("trades", "Skilled Trades"),
        ("plant", "Plant / Machinery / Drivers"),
        ("elementary", "Elementary / General Work"),
        ("other", "Other / Not in Labour Force"),
    ], required=True, default="other", index=True)
    sequence = fields.Integer(default=10)
    active = fields.Boolean(default=True)

    _sql_constraints = [("l10n_tt_occupation_code_uniq", "unique(code)", "Occupation codes must be unique.")]
