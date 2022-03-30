from unittest import TestCase
from unittest.mock import patch

from ..lib import hello


SRC = 'bat.metal_snake.lib'


class LibTests(TestCase):

    @patch(f'{SRC}.hello_rust', autospec=True)
    def test_hello(t, hello_rust):
        input_str = "from python"
        hello(input_str)
        hello_rust.assert_called_with(input_str)
