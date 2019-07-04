from pypiparser import PackageIndex
import unittest


class ParserTest(unittest.TestCase):
    _base_url = "https://pypi.timlehr.com"

    def test_index(self):
        index = PackageIndex(self._base_url)
        self.assertTrue(index.online)
        self.assertEqual(index.base_url, self._base_url)
        self.assertEqual(index.index_url, "{}/simple".format(self._base_url))

    def test_packages(self):
        index = PackageIndex(self._base_url)
        self.assertTrue(index.provides_package("pyside2"))
        self.assertGreater(len(index.get_all_versions("pyside2")), 0)
        self.assertTrue(index.get_newest_version("PySide2"))
