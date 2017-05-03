from pygments.lexers import get_all_lexers
from pygments.styles import get_all_styles


def lexers():
    lexer_list = []
    for item in get_all_lexers():
        if item[1]:
            lexer_list.append(item)
    return lexer_list


def language_choices():
    lexer_list = lexers()
    lang_list = []
    for item in lexer_list:
        lang_tuple = (item[1][0], item[0])
        lang_list.append(lang_tuple)
    lang_choices = sorted(lang_list)
    return lang_choices


def style_choices():
    style_list = []
    for item in get_all_styles():
        style_tuple = (item, item)
        style_list.append(style_tuple)
    sty_choices = sorted(style_list)
    return sty_choices
