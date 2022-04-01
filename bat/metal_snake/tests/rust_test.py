from unittest import TestCase

from ..rust import (
    rfib,
    hello_rust,
    error_rust,
)


class LibTests(TestCase):

    def test_rfib(t) -> None:
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
                t.assertEqual(rfib(n), v)

    def test_hello(t):
        input_str = "from python"
        hello_rust(input_str)

    def test_error_rust(t):
        with t.assertRaises(RuntimeError) as err:
            error_rust()

        t.assertEqual(
            err.exception.args,
            ("Raise Runtime Error: 'Test Exception'", )
        )
