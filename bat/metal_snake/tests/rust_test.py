from unittest import TestCase

from ..rust import hello_rust, error_rust


class LibTests(TestCase):

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
