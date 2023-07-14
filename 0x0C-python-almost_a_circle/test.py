import unittest

class MyTest(unittest.TestCase):
    def test_addition(self):
        result = 2 + 2
        self.assertFalse(True)

    def test_subtraction(self):
        result = 5 - 3
        self.assertEqual(result, 2)

if __name__ == '__main__':
    unittest.main()

# test = MyTest()
# test.test_addition()