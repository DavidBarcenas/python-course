import unittest

def sum(num1, num2):
    return num1 + num2

class BlackBoxTest(unittest.TestCase):
    """
        unit testing and integration testing
    """
    def test_add_two_positives(self):
        num_1 = 10
        num_2 = 5

        result = sum(num_1, num_2)
        self.assertEqual(result, 15)

    
    def test_add_two_negatives(self):
        num_1 = -10
        num_2 = -7

        result = sum(num_1, num_2)
        self.assertEqual(result, -17)


if __name__ == '__main__':
    unittest.main()