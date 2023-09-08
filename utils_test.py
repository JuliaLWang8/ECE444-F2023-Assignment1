import utils
import unittest

class TestIntConversion(unittest.TestCase):

    u = utils.utils()

    def test_reversed(self):
        self.assertEqual(self.u.reversed(123), 321)
        self.assertEqual(self.u.reversed(-456), -654)
        self.assertEqual(self.u.reversed(0), 0)

        self.assertEqual(self.u.reversed("123"), 321)
        self.assertFalse(self.u.reversed("abcd"))

        self.assertEqual(self.u.reversed(13.28), 31)
        self.assertEqual(self.u.reversed(5678.62), 8765)
    
    def test_formatter(self):

        self.assertEqual(self.u.formatter(10), ("0b1010", "0o12"))
        self.assertEqual(self.u.formatter(328), ("0b101001000", "0o510"))
        
        self.assertEqual(self.u.formatter("10"), ("0b1010", "0o12"))
        self.assertFalse(self.u.formatter("abcd"))

        self.assertEqual(self.u.formatter(10.895), ("0b1010", "0o12"))
        self.assertEqual(self.u.formatter(328.12), ("0b101001000", "0o510"))

if __name__ == '__main__':
    unittest.main()