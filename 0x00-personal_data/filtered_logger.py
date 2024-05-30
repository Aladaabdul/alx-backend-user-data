#!/usr/bin/env python3


"""filter_datum module"""


import re
from typing import List


def filter_datum(
        fields: List[str],
        redaction: str,
        message: str,
        separator: str
        ) -> str:
    """filter_datum function

    """
    pattern = r'({}=).*?(?={})'.format(
            '|'.join(re.escape(field) for field in fields),
            re.escape(separator))
    return re.sub(pattern, r'\1' + redaction, message)
