import unittest
from Prime_number import prime_numbers

class TestPrimeNumbers(unittest.Testcase):
    def test_answer(self):
        self.assertEquals(prime_numbers(11),[1,2,3,5,7,11])

    def test_negative(self):
        with self.assertRaises(TypeError):
            prime_numbers(-5)

    def test_returns_list(self):
        self.assertIsInstance(prime_numbers(5), list)

    def test_one_is_prime(self):
        self.assertIn(1, prime_numbers(5))

    def test_zero_is_not_prime(self):
        self.assertNotIn(0, prime_numbers(5))

if __name__=='__main__':
    unittest.main()
 
