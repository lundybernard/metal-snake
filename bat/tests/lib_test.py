from unittest import TestCase

from bat.lib import (
    fib,
    rfib,
    minimize_distance,
    distance_transform,
    hello_world,
    np,
)


class LibTests(TestCase):

    def setUp(t) -> None:
        t.fibmap: dict[int, int] = {
            1: 0,
            2: 1,
            3: 1,
            4: 2,
            5: 3,
            6: 5,
            7: 8,
        }

    def test_fib(t) -> None:
        for n, v in t.fibmap.items():
            with t.subTest(f'fib({n})'):
                t.assertEqual(fib(n), v)

    def test_rfib(t) -> None:
        for n, v in t.fibmap.items():
            with t.subTest(f'rfib({n})'):
                t.assertEqual(rfib(n), v)

    def test_minimize_distance(t) -> None:
        # Given a list of dicts representing features on nodes
        # find the node (list index)
        # which minimizes the distance to all features
        with t.subTest('simple'):
            features = [
                {'grocery': True, 'park': False, 'bar': True},
                {'grocery': False, 'park': False, 'bar': True},
                {'grocery': False, 'park': False, 'bar': False},
                {'grocery': True, 'park': True, 'bar': False},
                {'grocery': False, 'park': False, 'bar': True},
                {'grocery': False, 'park': True, 'bar': False},
            ]
            ret = minimize_distance(features)
            t.assertEqual(ret, 3)

        with t.subTest('multiple solutions'):
            # Returns the lowest index (first) solution
            features = [
                {'grocery': False, 'park': False, 'bar': False},
                {'grocery': True, 'park': True, 'bar': True},
                {'grocery': True, 'park': True, 'bar': True},
            ]
            ret = minimize_distance(features)
            t.assertEqual(ret, 1)

        with t.subTest('no solution'):
            # returns the best match
            features = [
                {'grocery': False, 'park': False, 'bar': False},
                {'grocery': False, 'park': False, 'bar': False},
                {'grocery': False, 'park': True, 'bar': True},
            ]
            ret = minimize_distance(features)
            t.assertEqual(ret, 2)

    def test_distance_transform(t):
        # Given a List of Boolian values
        # return an array of integers for the distance to each True value
        data = [True, False, False, False, True, False]
        ret = distance_transform(data)
        np.testing.assert_array_equal(ret, np.array([0, 1, 2, 1, 0, 1]))

    def test_hello_world(t):
        ret = hello_world()
        t.assertEqual(ret, 'Hello World!')
