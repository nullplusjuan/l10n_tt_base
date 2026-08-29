from odoo import api, models

from ..tools.phone import format_tt_phone


class ResPartner(models.Model):
    _inherit = "res.partner"

    _tt_phone_fields = ("phone", "mobile", "mobile2", "phone_work")

    @api.model
    def _normalize_tt_phone_vals(self, vals):
        vals = dict(vals)
        for field_name in self._tt_phone_fields:
            if field_name in vals and vals.get(field_name):
                vals[field_name] = format_tt_phone(vals[field_name], strict=False)
        return vals

    @api.model_create_multi
    def create(self, vals_list):
        return super().create([self._normalize_tt_phone_vals(vals) for vals in vals_list])

    def write(self, vals):
        return super().write(self._normalize_tt_phone_vals(vals))
