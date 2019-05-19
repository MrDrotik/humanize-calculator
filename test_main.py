from main import humanize
import pytest


class TestHumanize:

    def test_type_error(self):
        assert humanize('asdfsdf') == 'invalid input'
        assert humanize(self) == 'invalid input'
        assert humanize(lambda x: x**2) == 'invalid input'
        assert humanize(12.21) == 'invalid input'
        assert humanize(12) == 'invalid input'
        assert humanize([1, 2, 3, 4]) == 'invalid input'
        assert humanize(('a', 'b')) == 'invalid input'
        assert humanize('') == 'invalid input'



