import unittest
from task_16 import SherlockValidString

class SherlockValidString_test(unittest.TestCase):
    def test_der_parol_is_True(self):
        self.assertTrue(SherlockValidString("xyz"))
        self.assertTrue(SherlockValidString("xyzaa"))
        self.assertTrue(SherlockValidString("xxyyz"))
        self.assertTrue(SherlockValidString("xxyyzziii"))
        self.assertTrue(SherlockValidString("xyzxyzt"))
        self.assertTrue(SherlockValidString("xzzz"))
        self.assertTrue(SherlockValidString("xz"))
        self.assertTrue(SherlockValidString("xxxxxyyyyyy"))
        self.assertTrue(SherlockValidString("xyzxyzttt"))


    def test_der_parol_is_False(self):
        self.assertFalse(SherlockValidString("xyzzz"))
        self.assertFalse(SherlockValidString("xxyyza"))
        self.assertFalse(SherlockValidString("xxyyzabc"))
        self.assertFalse(SherlockValidString("xxyyzzzz"))
        self.assertFalse(SherlockValidString("xxyyzzziiioo"))
        self.assertFalse(SherlockValidString("xxzzzz"))
        self.assertFalse(SherlockValidString("xxxxxyyyyyyy"))
        self.assertFalse(SherlockValidString("xyzxyztttt"))


if __name__ == '__main__':
    unittest.main()