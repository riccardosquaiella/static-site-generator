import unittest

from leafnode import LeafNode


class TestLeafNode(unittest.TestCase):
    def setUp(self):
        print("\n", unittest.TestCase.id(self))

    def test_leaf_to_html_p(self):
        node = LeafNode("p", "Hello, world!")
        self.assertEqual(node.to_html(), "<p>Hello, world!</p>")

    def test_leaf_to_html_a(self):
        node = LeafNode("a", "boot.dev", {"href": "https://www.boot.dev"})
        self.assertEqual(node.to_html(), '<a href="https://www.boot.dev">boot.dev</a>')

    def test_leaf_to_html_rawtext(self):
        node = LeafNode(None, "rawtext")
        self.assertEqual(node.to_html(), "rawtext")


if __name__ == "__main__":
    unittest.main()
