# Copyright 2026 Joshua D
# SPDX-License-Identifier: AGPL-3.0-or-later
import re
from odoo import _, api, fields, models
from odoo.exceptions import ValidationError
from ..tools.phone import format_tt_phone


class ResPartner(models.Model):
    _inherit = "res.partner"

    tt_area_id = fields.Many2one("l10n.tt.area", string="TT Area / Community", ondelete="restrict")
    occupation_id = fields.Many2one("l10n.tt.occupation", string="Occupation", ondelete="restrict")
    tt_s42_postal_code = fields.Char(related="zip", string="S-42 Postal Code", readonly=False)

    _tt_phone_fields = ("phone", "mobile", "mobile2", "phone_work")

    @api.onchange("tt_area_id")
    def _onchange_tt_area_id(self):
        tt_country = self.env.ref("base.tt", raise_if_not_found=False)
        for partner in self.filtered("tt_area_id"):
            partner.city = partner.tt_area_id.name
            if partner.tt_area_id.state_id:
                partner.state_id = partner.tt_area_id.state_id
            if tt_country:
                partner.country_id = tt_country

    @api.constrains("zip", "country_id")
    def _check_tt_s42_postal_code(self):
        for partner in self:
            if not partner.zip:
                continue
            is_tt = partner.country_id and partner.country_id.code == "TT"
            if is_tt and not re.fullmatch(r"\d{6}", partner.zip.strip()):
                raise ValidationError(_("Trinidad and Tobago S-42 postal codes must contain exactly 6 digits."))

    @api.model
    def _normalize_tt_phone_vals(self, vals):
        vals = dict(vals)
        for field_name in self._tt_phone_fields:
            if field_name in vals and vals.get(field_name):
                vals[field_name] = format_tt_phone(vals[field_name], strict=False)
        return vals

    @api.model_create_multi
    def create(self, vals_list):
        records = super().create([self._normalize_tt_phone_vals(vals) for vals in vals_list])
        # onchange does not run during ORM create, so keep generic city/state/country synchronized.
        tt_country = self.env.ref("base.tt", raise_if_not_found=False)
        for record in records.filtered("tt_area_id"):
            sync = {"city": record.tt_area_id.name}
            if record.tt_area_id.state_id:
                sync["state_id"] = record.tt_area_id.state_id.id
            if tt_country:
                sync["country_id"] = tt_country.id
            super(ResPartner, record).write(sync)
        return records

    def write(self, vals):
        vals = self._normalize_tt_phone_vals(vals)
        if vals.get("tt_area_id"):
            area = self.env["l10n.tt.area"].browse(vals["tt_area_id"]).exists()
            if area:
                tt_country = self.env.ref("base.tt", raise_if_not_found=False)
                vals.setdefault("city", area.name)
                if area.state_id:
                    vals.setdefault("state_id", area.state_id.id)
                if tt_country:
                    vals.setdefault("country_id", tt_country.id)
        return super().write(vals)
