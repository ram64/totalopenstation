import unittest

from totalopenstation.formats.carlson_rw5 import FormatParser

class TestCarlsonRW5Parser(unittest.TestCase):
    def setUp(self):
        with open('sample_data/Leica1200.rw5') as testdata:
            fp = FormatParser(testdata.read())
            self.pts = list(fp.points)

    def test_point_xy(self):
        self.assertAlmostEqual(self.pts[0].geometry.y, 942130.662, places=3)
        self.assertAlmostEqual(self.pts[0].geometry.x, 16556174.237, places=3)

    @unittest.expectedFailure
    def test_point_z(self):
        self.assertAlmostEqual(self.pts[0].geometry.z, 20.053, places=3)

    def test_feature(self):
        self.assertEqual(self.pts[0].id, '108')
        self.assertEqual(self.pts[1].desc, 'LIGHT POLE')
        self.assertEqual(self.pts[0].desc, 'FENCE1')
