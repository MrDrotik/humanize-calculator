# Humanize-calculator 
This is a my solution for EVO Summer Python Lab'19 test. <br/>
Variant 1, task 2<br/><br/>
## Clone humanizer: 
    $ git clone https://github.com/MrDrotik/humanize-calculator
## Run pytest:
    $ pytest -v --pdb humanize-calculator/
## Run app:
    $ python3 humanize-calculator/run.py [-s] your_expression
### or
    $ python3 humanize-calculator/run.py [-s]
If you write argument "-s" (also "--solve"), expression has been solved.
<br/><br/><br/>
## Also you can run functions directly
    $ python3 -i humanize-calculator/main.py

### Convert arithmetic expression into a word.
    >>> humanize(arithmetic_expression[, is_solve_expression=False])
**arithmetic_expression** - your expression, can including only digits and arithmetic operands. Must contain one symbol "=". You must to place digits and operands on both sides of symbol "=". If flag is_solve_expression has been declared as true, characters can be only on the left side.

**is_solve_expression** - If this flag has declared as true, an expression would be solved.
<br/><br/>
### "humanize" your chunk.
    >>> humanize_chunk(chunk)
**chunk** - number or operand to convert to words.
<br/><br/>
### Get name of big numbers.
    >>> assemble_number_name(exponent)
**exponent** - Number of zeros (10^exponent). Must be multiple of three.
