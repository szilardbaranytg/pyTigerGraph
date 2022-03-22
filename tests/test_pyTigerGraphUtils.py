import re
import unittest
from datetime import datetime

from pyTigerGraphUnitTest import pyTigerGraphUnitTest


class test_pyTigerGraphUtils(pyTigerGraphUnitTest):
    conn = None

    def test_01_safeChar(self):
        ret = self.conn._safeChar(" _space")
        self.assertEqual(ret, '%20_space')
        ret = self.conn._safeChar("/_slash")
        self.assertEqual(ret, '%2F_slash')
        ret = self.conn._safeChar("ñ_LATIN_SMALL_LETTER_N_WITH_TILDE")
        self.assertEqual(ret, '%C3%B1_LATIN_SMALL_LETTER_N_WITH_TILDE')
        ret = self.conn._safeChar(12345)
        self.assertEqual(ret, "12345")
        ret = self.conn._safeChar(12.345)
        self.assertEqual(ret, "12.345")
        now = datetime.now()
        ret = self.conn._safeChar(now)
        exp = str(now).replace(" ", "%20").replace(":", "%3A")
        self.assertEqual(ret, exp)
        ret = self.conn._safeChar(True)
        self.assertEqual(ret, "True")

    def test_02_echo(self):
        ret = self.conn.echo()
        self.assertIsInstance(ret, str)
        self.assertEqual("Hello GSQL", ret)
        ret = self.conn.echo(True)
        self.assertIsInstance(ret, str)
        self.assertEqual("Hello GSQL", ret)

    def test_03_getVersion(self):
        ret = self.conn.getVersion()
        self.assertIsInstance(ret, list)
        self.assertGreater(len(ret), 0)

    def test_04_getVer(self):
        ret = self.conn.getVer()
        self.assertIsInstance(ret, str)
        m = re.match(r"[0-9]+\.[0-9]+\.[0-9]", ret)
        self.assertIsNotNone(m)


if __name__ == '__main__':
    unittest.main()
