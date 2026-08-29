import re
from odoo import _
from odoo.exceptions import ValidationError

def format_tt_phone(value, strict=False):
    """Normalize Trinidad & Tobago NANP numbers to +1 (868) XXX-XXXX."""
    if not value:
        return value
    raw = str(value).strip()
    digits = re.sub(r"\D", "", raw)
    if len(digits) == 7:
        local = digits
    elif len(digits) == 10 and digits.startswith("868"):
        local = digits[3:]
    elif len(digits) == 11 and digits.startswith("1868"):
        local = digits[4:]
    else:
        if strict:
            raise ValidationError(_("Phone numbers must be Trinidad and Tobago numbers in a valid 7-digit, 868XXXXXXX, or +1 (868) XXX-XXXX format."))
        return raw
    return f"+1 (868) {local[:3]}-{local[3:]}"
