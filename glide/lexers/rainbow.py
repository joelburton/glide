from pygments.token import String
from pygments.lexer import RegexLexer


class RainbowLinesLexer(RegexLexer):
    name = 'Rainbow Lines'
    aliases = ['rainbow-lines']
    filenames = ['*.rainbow-lines']

    tokens = {
        'root': [(r'.*\n', String.Affix, '2')],
        '2': [(r'.*\n', String.Backtick, '3')],
        '3': [(r'.*\n', String.Char, '4')],
        '4': [(r'.*\n', String.Doc, '5')],
        '5': [(r'.*\n', String.Escape, '6')],
        '6': [(r'.*\n', String.Interpol, '7')],
        '7': [(r'.*\n', String.Symbol, 'root')],
    }


class RainbowTwoLinesLexer(RegexLexer):
    name = 'Rainbow Two Lines'
    aliases = ['rainbow-2-lines']
    filenames = ['*.rainbow-2-lines']

    tokens = {
        'root': [(r'.*\n.*\n', String.Affix, '2')],
        '2': [(r'.*\n.*\n', String.Backtick, '3')],
        '3': [(r'.*\n.*\n', String.Char, '4')],
        '4': [(r'.*\n.*\n', String.Doc, '5')],
        '5': [(r'.*\n.*\n', String.Escape, '6')],
        '6': [(r'.*\n.*\n', String.Interpol, '7')],
        '7': [(r'.*\n.*\n', String.Symbol, 'root')],
    }
