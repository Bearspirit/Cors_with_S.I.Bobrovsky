import unittest
from test_set import *

class TestPowerSetMethods(unittest.TestCase):
    def test_put_alot_elements(self):
        PS = PowerSet()
        for i in range(0, 20000):
            PS.put(str(i))
        self.assertEqual(PS.size(), 20000)


if __name__ == '__main__':
    unittest.main()