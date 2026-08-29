# Copyright 2026 Joshua D
#
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU Affero General Public License as published
# by the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the
# GNU Affero General Public License for more details.
#
# SPDX-License-Identifier: AGPL-3.0-or-later
{
    "name": "Trinidad and Tobago - Base Localization",
    "version": "18.0.1.0.0",
    "summary": "Base Trinidad and Tobago geographic localization data",
    "description": """
Trinidad and Tobago Base Localization
======================================

Provides reusable Trinidad and Tobago localization data without imposing an
accounting chart or tax configuration.

Current scope:
- Trinidad and Tobago ISO-style first-level subdivisions for res.country.state
- Tobago as its first-level subdivision alongside Trinidad municipal areas

This module is intentionally a base/foundation module. Accounting, payroll,
statutory identifiers and tax rules should live in separate dependent modules.
""",
    "author": "Quadrintin Solutions",
    "category": "Localization",
    "license": "AGPL-3",
    "depends": ["base", "partner_extended_profile"],
    "data": [
        "data/res_country_state_data.xml",
        "data/res_country_data.xml",
    ],
    "installable": True,
    "application": False,
}
