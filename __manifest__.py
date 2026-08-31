# Copyright 2026 Joshua D
# SPDX-License-Identifier: AGPL-3.0-or-later
{
    "name": "Trinidad and Tobago - Base Localization",
    "version": "18.0.4.0.0",
    "summary": "Base Trinidad and Tobago geographic, addressing and phone localization data",
    "author": "Quadrintin Solutions",
    "category": "Localization",
    "license": "AGPL-3",
    "depends": ["base", "contacts", "partner_extended_profile"],
    "data": [
        "security/ir.model.access.csv",
        "data/res_country_state_data.xml",
        "data/partner_identity_type_data.xml",
        "data/l10n_tt_area_data.xml",
        "data/l10n_tt_occupation_data.xml",
        "views/l10n_tt_area_views.xml",
        "views/res_partner_views.xml",
    ],
    "installable": True,
    "application": False,
}
