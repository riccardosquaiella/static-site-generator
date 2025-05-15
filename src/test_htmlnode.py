import unittest

from htmlnode import HTMLNode


class TestHTMLNode(unittest.TestCase):
    def setUp(self):
        print("\n", unittest.TestCase.id(self))

    def test_raise_with_empty_tag(self):
        with self.assertRaises(ValueError) as cm:
            HTMLNode("")

    def test_props_to_html(self):
        node = HTMLNode("p", "ciao", [], {"class": "content", "id": "c1"})
        self.assertEqual(node.props_to_html(), ' class="content" id="c1"')

    def test_props_to_html_none(self):
        node = HTMLNode("p", "ciao", [])
        self.assertEqual("", node.props_to_html())

    def test_props_to_html_empty(self):
        node = HTMLNode("p", "ciao", [], {})
        self.assertEqual("", node.props_to_html())


if __name__ == "__main__":
    unittest.main()
