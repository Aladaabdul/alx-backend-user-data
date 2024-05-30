#!/usr/bin/env python3


"""filter_datum module"""


import re
from typing import List


def filter_datum(
        """filter_datum function

        """
        fields: List[str],
        redaction: str,
        message: str,
        separator: str
        ) -> str:
    pattern = r'({}=).*?(?={})'.format(
            '|'.join(re.escape(field) for field in fields),
            re.escape(separator))
    return re.sub(pattern, r'\1' + redaction, message)
