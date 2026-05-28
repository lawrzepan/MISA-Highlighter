from pygments.lexers import RegexLexer, words
from pygments.token import *

__all__ = ['MisaLexer']

_zeroadic_instructions = (
    'nop',
    'ret',
    'break',
    'yield',
    'exit'
)

class MisaLexer:
    name = 'Misa'
    aliases = ['misa']
    filenames = ['*.misa']

    tokens = {
        'root': [
            (r'\s+', Whitespace),
            (r'#.*\n', Comment),
            (words())
        ]
    }