"""
* Assignment: String Literals Emoticon
* Required: yes
* Complexity: easy
* Lines of code: 2 lines
* Time: 3 min

English:
    1. Print `Hello ð`
    2. Run doctests - all must succeed

Polish:
    1. Wypisz `Hello ð`
    2. Uruchom doctesty - wszystkie muszÄ siÄ powieÅÄ

Hints:
    * ð unicode codepoint is `\U0001F600`

Tests:
    >>> import sys; sys.tracebacklimit = 0

    >>> assert result is not Ellipsis, \
    'Assign your result to variable `result`'
    >>> assert type(result) is str, \
    'Variable `result` has invalid type, should be str'

    >>> 'ð' in result
    True
    >>> result
    'Hello ð'
"""

# Expected result: 'Hello ð'
# type: str
result = 'Hello \U0001F600'
