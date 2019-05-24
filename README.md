# Humanize-calculator 
This is my solution for EVO Summer Python Lab'19 test 
Variant 1, task 2<br/><br/>
####Clone humanizer:
    $ git clone https://github.com/MrDrotik/humanize-calculator
####Run app:<br/>
    $ python3 -i humanize-calculator/main.py
<br/>
###Convert arithmetic expression into word.<br/>
    >>> humanize(arithmetic_expression[, is_solve_regex=False])
**arithmetic_expression** - your expression, can including only digits and arithmetic operands. May be contain one symbol "=". You must to place digits and operands on both sides of symbol "=". If flag is_solve_regex declared as true, characters are needed only on the left side.

**is_solve_regex** - If this flag is declared as true, the expression will be solved.
<br/>
### "humanize" your chunk.
    >>> humanize_chunk(chunk)
**chunk** - number or operand to convert to words.
<br/>
### Get name of big numbers.
    >>> assemble_number_name(exponent)
**exponent** - Number of zeros (10^exponent). Must be multiple of three.