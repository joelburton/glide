# This stuff is added to every RST file before it's processed

# Colors; you'll also need to add CSS classes to your theme if you want these
# colors to actually appear, of course. You'll also need to edit the LaTeX
# writer to get them to appear in PDFs.
_colors = """
.. role:: black
.. role:: near-black
.. role:: dark-gray
.. role:: mid-gray
.. role:: gray
.. role:: silver
.. role:: light-silver
.. role:: moon-gray
.. role:: light-gray
.. role:: near-white
.. role:: white

.. role:: dark-red
.. role:: red
.. role:: light-red
.. role:: orange
.. role:: gold
.. role:: yellow
.. role:: light-yellow
.. role:: purple
.. role:: light-purple
.. role:: dark-pink
.. role:: hot-pink
.. role:: pink
.. role:: light-pink
.. role:: dark-green
.. role:: green
.. role:: light-green
.. role:: navy
.. role:: dark-blue
.. role:: blue
.. role:: light-blue
.. role:: lightest-blue
.. role:: washed-blue
.. role:: washed-green
.. role:: washed-yellow
.. role:: washed-red

.. role:: bg-black
.. role:: bg-near-black
.. role:: bg-dark-gray
.. role:: bg-mid-gray
.. role:: bg-gray
.. role:: bg-silver
.. role:: bg-light-silver
.. role:: bg-moon-gray
.. role:: bg-light-gray
.. role:: bg-near-white
.. role:: bg-white

.. role:: bg-dark-red
.. role:: bg-red
.. role:: bg-light-red
.. role:: bg-orange
.. role:: bg-gold
.. role:: bg-yellow
.. role:: bg-light-yellow
.. role:: bg-purple
.. role:: bg-light-purple
.. role:: bg-dark-pink
.. role:: bg-hot-pink
.. role:: bg-pink
.. role:: bg-light-pink
.. role:: bg-dark-green
.. role:: bg-green
.. role:: bg-light-green
.. role:: bg-navy
.. role:: bg-dark-blue
.. role:: bg-blue
.. role:: bg-light-blue
.. role:: bg-lightest-blue
.. role:: bg-washed-blue
.. role:: bg-washed-green
.. role:: bg-washed-yellow
.. role:: bg-washed-red

.. role:: inv-black
.. role:: inv-near-black
.. role:: inv-dark-gray
.. role:: inv-mid-gray
.. role:: inv-gray
.. role:: inv-silver
.. role:: inv-light-silver
.. role:: inv-moon-gray
.. role:: inv-light-gray
.. role:: inv-near-white
.. role:: inv-white

.. role:: inv-dark-red
.. role:: inv-red
.. role:: inv-light-red
.. role:: inv-orange
.. role:: inv-gold
.. role:: inv-yellow
.. role:: inv-light-yellow
.. role:: inv-purple
.. role:: inv-light-purple
.. role:: inv-dark-pink
.. role:: inv-hot-pink
.. role:: inv-pink
.. role:: inv-light-pink
.. role:: inv-dark-green
.. role:: inv-green
.. role:: inv-light-green
.. role:: inv-navy
.. role:: inv-dark-blue
.. role:: inv-blue
.. role:: inv-light-blue
.. role:: inv-lightest-blue
.. role:: inv-washed-blue
.. role:: inv-washed-green
.. role:: inv-washed-yellow
.. role:: inv-washed-red
"""

_roles = """
.. role:: ins
.. role:: del
.. role:: comment
.. role:: gone
.. role:: wrong
.. role:: muted
.. role:: small
.. role:: small-muted
.. role:: danger
.. role:: warning
.. role:: success
.. role:: err
.. role:: type
.. role:: bold
.. role:: ital
.. role:: caption

.. role:: gp
.. role:: c
.. role:: gs
.. role:: prompt

.. role:: emoji
.. role:: emoji-1x
.. role:: emoji-15x
.. role:: emoji-2x
.. role:: emoji-3x
.. role:: emoji-4x
.. role:: emoji-5x
.. role:: emoji-6x
.. role:: emoji-7x

.. role:: py(code)
   :language: python

.. role:: ts(code)
   :language: ts

.. role:: js(code)
   :language: js

.. role:: sql(code)
  :language: postgresql

.. role:: postgresql(code)
  :language: postgresql

.. role:: zsh(code)
  :language: zsh

.. role:: css(code)
  :language: css

.. role:: html(code)
  :language: html

.. role:: jsx(code)
  :language: jsx

.. role:: html+jinja(code)
  :language: html+jinja

.. role:: json(code)
  :language: json

.. role:: rb(code)
  :language: rb

.. role:: erb(code)
  :language: erb

.. role:: graphql(code)
  :language: graphql

.. role:: psql(code)
  :language: psql

.. role:: pycon(code)
  :language: pycon

.. role:: rst(code)
  :language: rst

.. role:: scss(code)
  :language: scss
"""

# Additional symbols to include
#
# Be cautious about just adding things here; not all symbols appear in all fonts
# nor will some obscure ones work in LaTeX
_symbols = """
.. |nbsp|      unicode:: U+000A0 .. NONBREAKING SPACE
.. |rarr|      unicode:: U+02192 .. RIGHTWARDS ARROW
.. |larr|      unicode:: U+02190 .. LEFTWARDS ARROW
.. |uarr|      unicode:: U+02191 .. UPWARDS ARROW
.. |darr|      unicode:: U+02193 .. DOWNWARDS ARROW
.. |lrarr|     unicode:: U+021C4 .. LEFT RIGHT ARROW
.. |plus|      unicode:: U+0002B .. PLUS SIGN
.. |times|     unicode:: U+000D7 .. MULTIPLICATION SIGN
.. |divide|    unicode:: U+000F7 .. DIVISION SIGN
.. |check|     unicode:: U+02713 .. CHECK MARK
.. |wrong|     unicode:: U+02717 .. BALLOT X 
.. |approx|    unicode:: U+02248 .. ALMOST EQUAL TO

.. |date|       date::
.. |key-legend| replace:: ``⌘`` Command |sp| |sp| ``⌃`` Ctrl |sp| |sp| ``⌥`` Alt/Opt |sp| |sp| ``⇧`` Shift |sp| |sp| ``fn`` Function |sp| |sp| ``⦿`` Click |sp| |sp| ``␣`` Space |sp| |sp| ``↵`` Enter |sp| |sp| ``⌫`` Backspace 
"""

# A new role for raw output that should only appear in HTML, and a
# directive that causes a linebreak <br> to appear only in revealjs
# This is useful for when we have a long line that we don't need to break in
# handouts-html or LaTeX, but looks better broken in RevealJS. Note: the
# handouts CSS needs to have ``.raw-reveal { display: none }``
_reveal_br = """
.. role:: raw-reveal(raw)
   :format: html
.. role:: raw-handouts(raw)
   :format: html 
.. role:: raw-html(raw)
    :format: html
    
.. |reveal-br|         replace:: :raw-reveal:`<br/>`
.. |br|                replace:: :raw-reveal:`<br/>`
.. |handouts-br|       replace:: :raw-handouts:`<br/>`
.. |all-br|            replace:: :raw-html:`<br/>``
.. |sp|                replace:: :raw-handouts:`&nbsp;`
"""

_icons = """ 
.. |i-macos|           replace:: :raw-html:`<i class="bi bi-apple          dark-gray"  title="MacOS"></i>`
.. |i-windows|         replace:: :raw-html:`<i class="bi bi-windows        blue"       title="Windows"></i>`
.. |i-linux|           replace:: :raw-html:`<i class="bi bi-ubuntu         orange"     title="Ubuntu Linux"></i>`
.. |i-chrome|          replace:: :raw-html:`<i class="bi bi-browser-chrome dark-blue"  title="Chrome"></i>`
.. |i-git|             replace:: :raw-html:`<i class="bi bi-git            orange"     title="Git"></i>`
.. |i-github|          replace:: :raw-html:`<i class="bi bi-github"                    title="GitHub"></i>`
.. |i-advanced|        replace:: :raw-html:`<i class="bi bi-rocket-takeoff purple"     title="Advanced"></i>`
.. |i-detail|          replace:: :raw-html:`<i class="bi bi-detail"                    title="Detail"></i>`
.. |i-terminal|        replace:: :raw-html:`<i class="bi bi-terminal"                  title="Terminal/Shell"></i>`
.. |i-youtube|         replace:: :raw-html:`<i class="bi bi-youtube        red"        title="YouTube"></i>`
.. |i-amazon|          replace:: :raw-html:`<i class="bi bi-amazon         orange"     title="Amazon"></i>`
.. |i-linkedin|        replace:: :raw-html:`<i class="bi bi-linkedin       blue"       title="Linkedin"></i>`
.. |i-android|         replace:: :raw-html:`<i class="bi bi-android2       green"      title="Android"></i>`
.. |i-facebook|        replace:: :raw-html:`<i class="bi bi-facebook       green"      title="Facebook"></i>`
.. |i-google|          replace:: :raw-html:`<i class="bi bi-google         red"        title="Google"></i>`
.. |i-slack|           replace:: :raw-html:`<i class="bi bi-slack          red"        title="Slack"></i>`
.. |i-stack-overflow|  replace:: :raw-html:`<i class="bi bi-stack-overflow red"        title="Stack Overflow"></i>`
.. |i-twitter|         replace:: :raw-html:`<i class="bi bi-twitter        blue"       title="Twitter"></i>`
.. |i-pair|            replace:: :raw-html:`<i class="bi bi-people-fill    purple"     title="Pair"></i>`
.. |i-security|        replace:: :raw-html:`<i class="bi bi-lock-fill      red"        title="Security"></i>`
.. |i-bookmark|        replace:: :raw-html:`<i class="bi bi-bookmark-star-fill purple" title="Bookmark"></i>`
.. |i-angellist|       replace:: :emoji:`🤞`
.. |i-star|            replace:: :emoji:`⭐`    
.. |i-file-code|       replace:: :raw-html:`<i class="bi bi-file-code"title="Code"></i>`    
.. |i-file-solution|   replace:: :raw-html:`<i class="bi bi-file-check" title="Solution"></i>`    
.. |i-yes|             replace:: :raw-html:`<i class="dark-green bi bi-check-circle-fill" title="Yes"></i>`    
.. |i-no|              replace:: :raw-html:`<i class="dark-red bi bi-x-circle-fill" title="No"></i>`    
.. |i-meh|             replace:: :raw-html:`<i class="gold bi bi-question-circle-fill" title="Meh"></i>`    
.. |i-stop|            replace:: :raw-html:`<i class="red margin-right-1 bi bi-sign-stop-fill" title="Stop"></i>`
"""

_bigo = """
.. |bigo-1|            replace:: `O(1)`
.. |bigo-logn|         replace:: `O(log n)`
.. |bigo-logn2|        replace:: `O(log`\\ :sub:`2` `n)`
.. |bigo-n|            replace:: `O(n)`
.. |bigo-nlogn|        replace:: `O(n log n)`
.. |bigo-ndlogn|       replace:: `O(n · log n)`
.. |bigo-nlog2n|       replace:: `O(n log`\\ :sub:`2` `n)`
.. |bigo-n2|           replace:: `O(n`\\ :sup:`2`\\ `)`
.. |bigo-2n|           replace:: `O(2`\\ :sup:`n`\\ `)`
.. |bigo-nfact|        replace:: `O(n`\\ `!)`
"""

glide_rst_prolog = _roles + _colors
glide_rst_epilog = _symbols + _reveal_br + _icons + _bigo