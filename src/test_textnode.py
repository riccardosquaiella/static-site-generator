import unittest

from textnode import TextNode, TextType, text_node_to_html_node


class TestTextNode(unittest.TestCase):
    def setUp(self):
        print("\n", unittest.TestCase.id(self))

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

    def test_text(self):
        node = TextNode("This is a text node", TextType.TEXT)
        html_node = text_node_to_html_node(node)
        self.assertEqual(html_node.to_html(), "This is a text node")

    def test_bold(self):
        node = TextNode("This is a text node", TextType.BOLD)
        html_node = text_node_to_html_node(node)
        self.assertEqual(html_node.tag, "b")
        self.assertEqual(html_node.to_html(), "<b>This is a text node</b>")

    def test_italic(self):
        node = TextNode("This is a text node", TextType.ITALIC)
        html_node = text_node_to_html_node(node)
        self.assertEqual(html_node.to_html(), "<i>This is a text node</i>")

    def test_code(self):
        node = TextNode("This is a text node", TextType.CODE)
        html_node = text_node_to_html_node(node)
        self.assertEqual(html_node.to_html(), "<code>This is a text node</code>")

    def test_link(self):
        node = TextNode("This is a link", TextType.LINK, "https://www.boot.dev")
        html_node = text_node_to_html_node(node)
        self.assertEqual(
            html_node.to_html(), '<a href="https://www.boot.dev">This is a link</a>'
        )

    def test_image(self):
        node = TextNode("This is an image", TextType.IMAGE, "./img.png")
        html_node = text_node_to_html_node(node)
        self.assertEqual(
            html_node.to_html(), '<img src="./img.png" alt="This is an image"></img>'
        )


if __name__ == "__main__":
    unittest.main()
