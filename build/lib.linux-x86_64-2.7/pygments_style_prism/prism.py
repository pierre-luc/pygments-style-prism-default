# -*- coding: utf-8 -*-
"""
    pygments.styles.prism
    ~~~~~~~~~~~~~~~~~~~~~~~

    Mimic the prism.js color scheme.

    :copyright: Copyright 2006-2013 by the Pygments team, see AUTHORS.
    :license: BSD, see LICENSE for details.
"""

from pygments.style import Style
from pygments.token import Keyword, Name, Comment, String, Error, Text, \
     Number, Operator, Generic, Whitespace, Punctuation, Other, Literal

class PrismStyle(Style):
    """
    prism.js default color scheme.
    """

    background_color = "#fafafa" #272822
    highlight_color = "#e6e3c3" #49483e

    keywordsColor = "#0077aa"
    textColor = "#000000"

    styles = {
        # No corresponding class for the following:
        Text:                      "#272822", # class:  '' #f8f8f2
        Whitespace:                "",        # class: 'w'
        Error:                     "#960050 bg:#1e0010", # class: 'err'
        Other:                     "",        # class 'x'

        Comment:                   "#75715e", # class: 'c'
        Comment.Multiline:         "#5fcda6", # class: 'cm'
        Comment.Preproc:           "",        # class: 'cp'
        Comment.Single:            "",        # class: 'c1'
        Comment.Special:           "",        # class: 'cs'

        Keyword:                   keywordsColor, # class: 'k'
        Keyword.Constant:          "",        # class: 'kc'
        Keyword.Declaration:       "",        # class: 'kd'
        Keyword.Namespace:         "#f92672", # class: 'kn'
        Keyword.Pseudo:            "",        # class: 'kp'
        Keyword.Reserved:          "",        # class: 'kr'
        Keyword.Type:              "",        # class: 'kt'

        Operator:                  "#a67f59", # class: 'o'
        Operator.Word:             "",        # class: 'ow' - like keywords

        Punctuation:               "#111111", # class: 'p' #f8f8f2

        Name:                      "#111111", # class: 'n'
        Name.Attribute:            textColor, # class: 'na' - to be revised
        Name.Builtin:              "",        # class: 'nb'
        Name.Builtin.Pseudo:       "",        # class: 'bp'
        Name.Class:                "#990055", # class: 'nc' - to be revised
        Name.Constant:             keywordsColor, # class: 'no' - to be revised
        Name.Decorator:            textColor, # class: 'nd' - to be revised
        Name.Entity:               "",        # class: 'ni'
        Name.Exception:            textColor, # class: 'ne'
        Name.Function:             textColor, # class: 'nf'
        Name.Property:             "#990055", # class: 'py'
        Name.Label:                "",        # class: 'nl'
        Name.Namespace:            "",        # class: 'nn' - to be revised
        Name.Other:                textColor, # class: 'nx'
        Name.Tag:                  "#f92672", # class: 'nt' - like a keyword
        Name.Variable:             "",        # class: 'nv' - to be revised
        Name.Variable.Class:       "",        # class: 'vc' - to be revised
        Name.Variable.Global:      "",        # class: 'vg' - to be revised
        Name.Variable.Instance:    "",        # class: 'vi' - to be revised

        Number:                    "#ae81ff", # class: 'm'
        Number.Float:              "",        # class: 'mf'
        Number.Hex:                "",        # class: 'mh'
        Number.Integer:            "",        # class: 'mi'
        Number.Integer.Long:       "",        # class: 'il'
        Number.Oct:                "",        # class: 'mo'

        Literal:                   "#ae81ff", # class: 'l'
        Literal.Date:              "#a67f59", # class: 'ld'

        String:                    "#669900", # class: 's'
        String.Backtick:           "",        # class: 'sb'
        String.Char:               "",        # class: 'sc'
        String.Doc:                "",        # class: 'sd' - like a comment
        String.Double:             "",        # class: 's2'
        String.Escape:             "#8045FF", # class: 'se'
        String.Heredoc:            "",        # class: 'sh'
        String.Interpol:           "",        # class: 'si'
        String.Other:              "",        # class: 'sx'
        String.Regex:              "#a67f59", # class: 'sr'
        String.Single:             "",        # class: 's1'
        String.Symbol:             "",        # class: 'ss'

        Generic:                   "",        # class: 'g'
        Generic.Deleted:           "",        # class: 'gd',
        Generic.Emph:              "italic",  # class: 'ge'
        Generic.Error:             "",        # class: 'gr'
        Generic.Heading:           "",        # class: 'gh'
        Generic.Inserted:          "",        # class: 'gi'
        Generic.Output:            "",        # class: 'go'
        Generic.Prompt:            "",        # class: 'gp'
        Generic.Strong:            "bold",    # class: 'gs'
        Generic.Subheading:        "",        # class: 'gu'
        Generic.Traceback:         "",        # class: 'gt'
    }
