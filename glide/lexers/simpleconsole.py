from pygments.lexer import RegexLexer, bygroups
from pygments.token import *


class SimpleConsoleLexer(RegexLexer):
    name = 'Simple Console'
    aliases = ['simple-console']
    filenames = ['*.simple-console']

    tokens = {
        'root': [
            (r'\n', Text),
            (r'#.*$', Comment),
            (r'(.*\$ )([^#\n]*)', bygroups(Generic.Prompt, Generic.Strong)),
            (r'.+', Text),
        ],
    }
