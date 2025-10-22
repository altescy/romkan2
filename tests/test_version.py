import unittest

import romkan2


class TestVersion(unittest.TestCase):
    def test_version(self):
        self.assertIsInstance(romkan2.__version__, str)
        self.assertEqual(romkan2.__version__, "0.1.0")
