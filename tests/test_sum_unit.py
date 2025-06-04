import unittest
from app.main import suma

class TestSumaUnit(unittest.TestCase):
    def test_suma_positivos(self):
        self.assertEqual(suma(2, 3), 5)

    def test_suma_negativos(self):
        self.assertEqual(suma(-2, -3), -5)

if __name__ == "__main__":
    unittest.main()
