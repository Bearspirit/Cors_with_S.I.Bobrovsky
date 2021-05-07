import unittest
import random
from task_3 import TheRabbitsFoot

class func_test(unittest.TestCase):
    def encode_test(self):
        self.assertEqual(TheRabbitsFoot("отдай мою кроличью лапку", True), "омоюу толл дюиа акчп йрьк")
        self.assertEqual(TheRabbitsFoot("я был сегодня в деревне", True), "яеяе бгвв ыодн ядее снр")

    def decode_test(self):
        self.assertEqual(TheRabbitsFoot("омоюу толл дюиа акчп йрьк", False), "отдаймоюкроличьюлапку")
        self.assertEqual(TheRabbitsFoot("яеяе бгвв ыодн ядее снр", False), "ябылсегоднявдеревне")
       

if __name__ == '__main__':
    unittest.main()