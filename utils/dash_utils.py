import dash_html_components as html


def column(children, style={}, className='five columns'):
    """"Convenience function to return a column style html.Div. It uses
    a custom css determining the width of the columns based on the className.
    :param list children: List of children to put into the column.
    :param style dict: dict of style arguments for the column. Will overwrite
                       the css values
    :param st className: name pointing to the css class.
    """
    return html.Div(children=children, style=style, className=className)


def row(children, style={}, className='row'):
    """"Convenience function to return a row style html.Div. It uses
    a custom css determining the width of the columns based on the className.
    :param list children: List of children to put into the column.
    :param style dict: dict of style arguments for the column. Will overwrite
                       the css values
    :param st className: name pointing to the css class.
    """
    return html.Div(children=children, style=style, className=className)
