from unittest import TestCase
from unittest.mock import patch

from ..lib import fib, hello


SRC = 'bat.metal_snake.lib'


class LibTests(TestCase):

    def test_fib(t) -> None:
        fibmap: dict[int, int] = {
            1: 0,
            2: 1,
            3: 1,
            4: 2,
            5: 3,
            6: 5,
            7: 8,
        }

        for n, v in fibmap.items():
            with t.subTest(f'fib({n})'):
                t.assertEqual(fib(n), v)

    @patch(f'{SRC}.hello_rust', autospec=True)
    def test_hello(t, hello_rust):
        input_str = "from python"
        hello(input_str)
        hello_rust.assert_called_with(input_str)
