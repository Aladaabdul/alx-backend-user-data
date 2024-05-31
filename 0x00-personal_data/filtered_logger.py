#!/usr/bin/env python3


"""filter_datum module"""


import logging
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


class RedactingFormatter(logging.Formatter):
    """ Redacting Formatter class
        """

    REDACTION = "***"
    FORMAT = "[HOLBERTON] %(name)s %(levelname)s %(asctime)-15s: %(message)s"
    SEPARATOR = ";"

    def __init__(self, fields: List[str]):
        """init function

        """
        super(RedactingFormatter, self).__init__(self.FORMAT)
        self.fields = fields

    def format(self, record: logging.LogRecord) -> str:
        """def format function

        """
        original_message = super(RedactingFormatter, self).format(record)
        return filter_datum(
                self.fields,
                self.REDACTION,
                original_message,
                self.SEPARATOR
                )
