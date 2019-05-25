from main import humanize

expressions = [
    {
        'exp': '13=2',
        'is_solve': False,
        'result': 'thirteen equals two'
    }, {
        'exp': '5 4+ 9 4  - 1321=2',
        'is_solve': False,
        'result': 'fifty-four plus ninety-four minus one ' +
                  'thousand three hundred and twenty-one equals two'
    }, {
        'exp': '4 654 765 842 224=2',
        'is_solve': False,
        'result': 'four trillion six hundred fifty-four billion ' +
                  'seven hundred sixty-five million eight hundred forty-two ' +
                  'thousand two hundred and twenty-four equals two'
    }, {
        'exp': '13=21',
        'is_solve': True,
        'result': 'thirteen equals thirteen'
    }, {
        'exp': '56 9 +431=',
        'is_solve': True,
        'result': 'five hundred and sixty-nine plus four hundred and ' +
                  'thirty-one equals one thousand'
    }, {
        'exp': str(10 ** 30003) + '=',
        'is_solve': True,
        'result': 'one dezmilliaillion equals one dezmilliaillion'
    }
]


def test_not_accepted_cars():
    assert humanize('asdf=sdf') == 'invalid input'
    assert humanize('5+6=dd21') == 'invalid input'
    assert humanize('') == 'invalid input'
    assert humanize('21=') == 'invalid input'
    assert humanize('21=') == 'invalid input'


def test_wrong_type():
    assert humanize(object) == 'invalid input'
    assert humanize(lambda x: x ** 2) == 'invalid input'
    assert humanize(12.21) == 'invalid input'
    assert humanize(12) == 'invalid input'
    assert humanize([1, 2, 3, 4]) == 'invalid input'
    assert humanize(('a', 'b')) == 'invalid input'


def test_on_expressions():
    for element in expressions:
        assert humanize(element['exp'], element['is_solve']) == element['result']
