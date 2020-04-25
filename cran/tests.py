from django.test import TestCase

from .utilites import parse_description, parse_package, get_description_from_url
class PackageTestCase(TestCase):
    def setUp(self):
        self.packages = open("cran/testdata/PACKAGES").read()

    def test_parse_packages(self):
        for package in self.packages.split("\n\n"):
            parse_package(package)

    def test_download_and_extract_description(self):
        url = "http://cran.r-project.org/src/contrib/aaSEA_1.1.0.tar.gz"
        description = get_description_from_url(url, "aaSEA")
        print(description)
        print(parse_description(description))


