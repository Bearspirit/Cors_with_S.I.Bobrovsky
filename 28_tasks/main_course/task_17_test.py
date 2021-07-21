import unittest
from task_17 import TreeOfLife

class SherlockValidString_test(unittest.TestCase):
    def test_Andrassil(self):
        self.assertEqual(TreeOfLife(3, 4, 4, [".+..","..+.",".+.."]), [".+..","..+.",".+.."])
        self.assertEqual(TreeOfLife(3, 4, 12, [".+..","..+.",".+.."]), [".+..","..+.",".+.."])
        self.assertEqual(TreeOfLife(3, 4, 8, [".+..","..+.",".+.."]), [".+..","..+.",".+.."])
        self.assertEqual(TreeOfLife(3, 4, 7, [".+..","..+.",".+.."]), ["++++","++++","++++"])
        self.assertEqual(TreeOfLife(3, 4, 3, [".+..","..+.",".+.."]), ["++++","++++","++++"])
        self.assertEqual(TreeOfLife(3, 4, 11, [".+..","..+.",".+.."]), ["++++","++++","++++"])
        self.assertEqual(TreeOfLife(3, 4, 2, ["++++","++++","++++"]), ["....","....","...."])
        self.assertEqual(TreeOfLife(3, 4, 3, ["++++","++++","++++"]), ["++++","++++","++++"])
        self.assertEqual(TreeOfLife(3, 4, 4, ["....","....","...."]), ["....","....","...."])
        self.assertEqual(TreeOfLife(3, 4, 5, ["....","....","...."]), ["++++","++++","++++"])

if __name__ == '__main__':
    unittest.main()