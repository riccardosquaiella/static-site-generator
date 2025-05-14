import unittest

from textnode import TextNode, TextType


class TestTextNode(unittest.TestCase):
    def test_eq(self):
        node = TextNode("This is a text node", TextType.BOLD)
        node2 = TextNode("This is a text node", TextType.BOLD)
        self.assertEqual(node, node2)
        self.assertIsNone(node.url)
        self.assertIsNone(node2.url)

    def test_eq_different_text_type(self):
        node = TextNode("This is a text node", TextType.ITALIC)
        node2 = TextNode("This is a text node", TextType.BOLD)
        self.assertNotEqual(node, node2)
        self.assertEqual(node.text, node2.text)
        self.assertEqual(node.url, node2.url)
        self.assertNotEqual(node.text_type, node2.text_type)

    def test_eq_different_url(self):
        node = TextNode("This is a text node", TextType.LINK, "url")
        node2 = TextNode("This is a text node", TextType.BOLD)
        self.assertNotEqual(node, node2)
        self.assertEqual(node.text, node2.text)
        self.assertNotEqual(node.text_type, node2.text_type)
        self.assertNotEqual(node.url, node2.url)

    def test_raise_exception_init(self):
        for type in TextType:
            match type:
                case TextType.LINK | TextType.IMAGE:
                    TextNode("This is a text node", type, "url")
                case _:
                    with self.assertRaises(Exception):
                        TextNode("This is a text node", type, "url")


if __name__ == "__main__":
    unittest.main()
