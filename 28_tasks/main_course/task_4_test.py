import unittest
from task_4 import PrintingCosts

class func_test(unittest.TestCase):
    def test_line_coast(self):
        self.assertEqual(PrintingCosts("FGHJ"), 88)
        self.assertEqual(PrintingCosts("ПРОМв"), 5*23)
        self.assertEqual(PrintingCosts("№;%:"), 64)

       


if __name__ == '__main__':
    unittest.main()