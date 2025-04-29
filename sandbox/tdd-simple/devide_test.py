import unittest
from devide import devide


class TestDevide(unittest.TestCase):
    def test_error_args_required(self):
        with self.assertRaises(ValueError) as context:
            devide(None, None)

        self.assertEqual("arguments are required", str(context.exception))

    def test_error_devided_by_zero(self):
        with self.assertRaises(ZeroDivisionError):
            devide(4, 0)

    def test_success_devide(self):
        self.assertEqual(2, devide(4, 2))


if __name__ == '__main__':
    unittest.main()
