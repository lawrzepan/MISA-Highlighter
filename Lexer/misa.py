from pygments.lexers import RegexLexer, words
from pygments.token import *

__all__ = ['MisaLexer']

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