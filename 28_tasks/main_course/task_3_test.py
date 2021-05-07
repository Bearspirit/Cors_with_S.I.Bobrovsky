import unittest
from task_3 import TheRabbitsFoot

class func_test(unittest.TestCase):
    def test_encode(self):
        self.assertEqual(TheRabbitsFoot("отдай мою кроличью лапку", True), "омоюу толл дюиа акчп йрьк")
        self.assertEqual(TheRabbitsFoot("я был сегодня в деревне", True), "яеяе бгвв ыодн лдее снр")

    def test_decode(self):
        self.assertEqual(TheRabbitsFoot("омоюу толл дюиа акчп йрьк", False), "отдаймоюкроличьюлапку")
        self.assertEqual(TheRabbitsFoot("яеяе бгвв ыодн лдее снр", False), "ябылсегоднявдеревне")
       

if __name__ == '__main__':
    unittest.main()