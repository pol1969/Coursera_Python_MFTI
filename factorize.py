class TestFactorize(unittest.TestCase):

    def test_wrong_types_raise_exception(self):
        with self.subTest(x='string'):
            self.assertRaises(TypeError, factorize, 'string')
        with self.subTest(x=1.5):
            self.assertRaises(TypeError, factorize, 1.5)

    def test_negative(self):
        for x in [-1, -10, -100]:
            with self.subTest(x):
                self.assertRaises(ValueError, 
                                  factorize, x)

    def test_zero_and_one_cases(self):
        with self.subTest(x=0):
            self.assertEqual(factorize(0),(0,))
        with self.subTest(x=1):
            self.assertEqual(factorize(1),(1,))

    def test_simple_numbers(self):
        with self.subTest(x=3):
            self.assertEqual(factorize(3),(3,))

        with self.subTest(x=13):
            self.assertEqual(factorize(13),(13,))
        
        with self.subTest(x=29):
            self.assertEqual(factorize(29),(29,))


    def test_two_simple_multipliers(self):
        with self.subTest(x=6):
            self.assertEqual(factorize(6),(2,3))
        with self.subTest(x=26):
            self.assertEqual(factorize(26),(2,13))
        with self.subTest(x=121):
            self.assertEqual(factorize(121),(11,11))

    def test_many_multipliers(self):
        with self.subTest(x=1001):
            self.assertEqual(factorize(1001),(7,11,13))
        with self.subTest(x=9699690):
            self.assertEqual(factorize(9699690),
                             (2,3,5,7,11,13,17,19))
 


