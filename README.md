# Trinidad and Tobago - Base Localization

Foundation localization module for Odoo 18. It provides TT subdivisions, reusable area/community records, S-42 six-digit postal-code validation for Trinidad and Tobago contacts, and phone normalization to `+1 (868) XXX-XXXX`.

`res.partner.zip` remains the canonical postal-code field. The localization exposes `tt_s42_postal_code` as a writable alias rather than storing a second copy of the same postal code.

## License
GNU Affero General Public License v3 or later. See `LICENSE`.

SPDX-License-Identifier: AGPL-3.0-or-later
