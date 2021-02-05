from django.test import TestCase
import xml.etree.ElementTree as ET

from . import connector, data_util


class ConnectorTestCase(TestCase):
    def setUp(self):
        pass

    def test_connector(self):
        status, result = connector.search_book("holiday", 1)
        self.assertEqual(status, True)


class DataUtilTestCase(TestCase):
    def setUp(self):
        pass

    def test_parse(self):
        tree = ET.parse("./books/search_result.xml")
        root = tree.getroot()
        result = data_util.parse_tree(root)
        start = int(result['start'])
        end = int(result['end'])
        current_count = len(result['books'])
        self.assertEqual(current_count, end - start + 1)