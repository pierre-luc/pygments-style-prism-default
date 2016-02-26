This is a pygments style based on the popular prism  color scheme. This version is suitable for light backgrounds, whereas the original scheme is designed for dark backgrounds.


Installation
============

Source
------
::

   $ git clone https://github.com/pierre-luc/pygments-style-prism-default
   $ cd pygments-style-prism-default
   $ python setup.py install


Usage Sample
------------
::

   >>> from pygments.formatters import HtmlFormatter
   >>> HtmlFormatter(style='prism').style
   <class 'pygments_style_prism.PrismStyle'>


Export the style as CSS
-----------------------
::

   pygmentize -S prism -f html > prism.css
