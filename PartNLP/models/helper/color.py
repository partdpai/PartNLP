"""
        PartNLP
            AUTHORS:
                MOSTAFA & SAMAN
"""
from dataclasses import dataclass


@dataclass
class Color:
    """
            Colors
    """
    header, blue = '\033[95m', '\033[94m'
    green, yellow = '\033[92m', '\033[93m'
    fail, endc, bold = '\033[91m', '\033[0m', '\033[1m',
    black = '\033[90m'
