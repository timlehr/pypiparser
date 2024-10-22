from pypiparser import PackageIndex
import unittest


class ParserTest(unittest.TestCase):
    _base_url = "https://test.pypi.org/simple"

    def test_index(self):
        index = PackageIndex(self._base_url)
        self.assertTrue(index.online)
        self.assertEqual(index.index_url, self._base_url.strip("/"))

    def test_packages(self):
        index = PackageIndex(self._base_url)
        self.assertTrue(index.provides_package("scarif-apps"))
        self.assertGreater(len(index.get_all_versions("scarif-apps")), 0)
        self.assertTrue(index.get_newest_version("scarif-apps"))
