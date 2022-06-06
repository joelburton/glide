from pygments.lexer import RegexLexer, bygroups
from pygments.token import *


class SimpleConsoleLexer(RegexLexer):
    name = 'Simple Console'
    aliases = ['simple-console']
    filenames = ['*.simple-console.txt']

    tokens = {
        'root': [
            # at the end of a line, reset it to text
            (r'\n', Text),
            # a prompt --- starts the line, with a comment
            (r'^([$%] )(.*?)( # .*)$', bygroups(Generic.Prompt, Generic.Strong, Comment)),
            # a prompt anywhere else --- with a comment
            (r'^([-\w() /~:@*]* [$%] )( # .*)$', bygroups(Generic.Prompt, Generic.Strong, Comment)),
            # a prompt --- starts the line
            (r'^([$%] )(.*)$', bygroups(Generic.Prompt, Generic.Strong)),
            # a prompt anywhere else
            (r'^([-\w() /~:@*]* [$%] )(.*)$', bygroups(Generic.Prompt, Generic.Strong)),
            # continuation lines must start with "> ", with a comment
            (r'^(> )(.*)( $ .*)$', bygroups(Generic.Prompt, Generic.Strong, Comment)),
            # continuation lines must start with "> "
            (r'^(> )(.*)$', bygroups(Generic.Prompt, Generic.Strong)),
            # a "#! " at the very start is a full-line error comment
            (r'^#! .*$', Comment.Multiline),
            # a " #! blah" is a comment
            (r'(.*?)( #! .*)$', bygroups(Text, Comment.Multiline)),
            # a "# " at the very start is a full-line comment
            (r'^# .*$', Comment),
            # a " # blah" is a comment
            (r'(.*?)( # .*)$', bygroups(Text, Comment)),
            (r'.+', Text),
        ],
    }
