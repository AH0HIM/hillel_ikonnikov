import argparse

import xml.etree.ElementTree as ET
from link_analyzer import LinkAnalyzer


class XMLAnalyzer:
    def __new__(cls, *args, **kwargs):
        analyzer = super().__new__(cls)
        if not args and not kwargs:
            analyzer.path = cls.user_path_input()
        return analyzer

    def __init__(self, path=None):
        if path:
            self.path = path
        self.tree = None
        self.root = None
        self.link_analyzer = LinkAnalyzer()

    @staticmethod
    def user_path_input():
        parser = argparse.ArgumentParser()
        parser.add_argument('-x', '--xml_document_path', dest='xml_path', help="Help for ip parameter")
        args = parser.parse_args()
        if args.xml_path:
            xml_path = args.xml_path
        else:
            xml_path = input("Enter xml document absolute path:")
        return xml_path

    def get_root(self):
        self.tree = ET.parse(self.path)
        self.root = self.tree.getroot()

    def collect_text(self, tag, basket=[]):
        for tag_data in self.root.iter(tag):
            basket.append(tag_data.text)
        return basket

    @property
    def raw_links(self):
        """Get all possible links from xml document"""
        self.get_root()
        links = []
        for link_type in LinkAnalyzer.LINK_TYPES:
            links.extend(self.collect_text(link_type))
        return links

    def get_countries(self):
        countries = self.collect_text('country')
        for country in countries:
            if "liechtenstein" in country.lower():
                print("Hello Liechtenstein")
        return countries


if __name__ == "__main__":
    xml_an = XMLAnalyzer(
        r"C:\Projects\Hillel_Automation\simple_package_demo\XML parser\country_links.xml")  # args.xml_path / xml_path
    xml_an2 = XMLAnalyzer()  # args.xml_path / xml_path
    xml_an.get_root()
    xml_an.root.tag
    xml_an.root.text
    # print(xml_an.get_countries())
    print(xml_an.raw_links)
    input("wait for enter")
    print(xml_an.raw_links)
    xml_an.link_analyzer.check_links(xml_an.raw_links)
