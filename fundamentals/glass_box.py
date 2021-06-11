import unittest

def he_is_older(age):
    if age >= 18:
        return True
    else:
        return False


class GlassBoxTest(unittest.TestCase):
    """
     reression test
    """
    def test_he_is_older(self):
        age = 20

        result = he_is_older(age)
        self.assertEqual(result, True)
    
    def test_is_minor(self):
        age = 15

        result = he_is_older(age)
        self.assertEqual(result, False)


if __name__ == '__main__':
    unittest.main()