import re

from pygments.token import *
from pygments.lexer import bygroups, RegexLexer
from pygments.util import ClassNotFound


class CommentableHttpLexer(RegexLexer):
    name = 'Commentable HTTP'
    aliases = ['commentable-http']
    filenames = ['*.commentable-http']

    flags = re.DOTALL

    tokens = {
        'root': [
            # Request
            (r'(GET|POST|PUT|DELETE|HEAD|OPTIONS|TRACE|PATCH)( +)([^ ]+)( +)'
             r'(HTTP)(/)(1\.[01]|2(?:\.0)?|3)?(.*?#?[^\n]*?)(\n|\Z)',
             bygroups(Name.Function, Text, Name.Namespace, Text,
                      Keyword.Reserved, Operator, Number, Comment, Text),
             'headers'),

            # Response
            (r'(HTTP)(/)(1\.[01]|2(?:\.0)?|3)( +)(\d{3})'
             r'(?:( +)([^\n^#]*))?(# [^\n]*)?(\n|\Z)',
             bygroups(Keyword.Reserved, Operator, Number, Text, Number, Text,
                      Name.Exception, Comment, Text),
             'headers'),
        ],
        'headers': [
            (r'([^\s:]+)( *)(:)( *)([^\n#]+)(# [^\n]+)?(\n|\Z)',
             bygroups(
                 Name.Attribute, Text, Operator, Text, Literal, Comment, Text)),
            (r'\n', Text, 'content')
        ],
        'content': [
            (r'.+', Text)
        ]
    }
