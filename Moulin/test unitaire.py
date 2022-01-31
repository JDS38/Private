import sys
sys.path.append("..")
import main
import unittest


class test(unittest.TestCase):

    def test_place_libre(self):
        self.assert_true(type(main.Pion()))
        self.assert_(main.Pion[(1,1)])

    def test_deplacement(self):
        self.assertListEqual(main.mouvements(), [(1, 1)])
        self.assertListEqual(main.mouvements(), [(2, 1)])
        self.assertListEqual(main.mouvements(), [(3, 1)])

if __name__ == '__main__':
    unittest.main()