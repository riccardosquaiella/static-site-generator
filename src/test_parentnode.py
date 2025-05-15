import unittest

from leafnode import LeafNode
from parentnode import ParentNode


class TestParentNode(unittest.TestCase):
    def setUp(self):
        print("\n", unittest.TestCase.id(self))

    def test_to_html_with_children(self):
        child_node = LeafNode("span", "child")
        parent_node = ParentNode("div", [child_node])
        self.assertEqual(parent_node.to_html(), "<div><span>child</span></div>")

    def test_to_html_with_grandchildren(self):
        grandchild_node = LeafNode("b", "grandchild")
        child_node = ParentNode("span", [grandchild_node])
        parent_node = ParentNode("div", [child_node])
        self.assertEqual(
            parent_node.to_html(),
            "<div><span><b>grandchild</b></span></div>",
        )

    def test_to_html_with_whole_family(self):
        grandchild_node1 = LeafNode("b", "grandchild1")
        grandchild_node2 = LeafNode("b", "grandchild2")
        child_node1 = ParentNode("span", [grandchild_node1])
        child_node2 = ParentNode("span", [grandchild_node2])
        parent_node = ParentNode("div", [child_node1, child_node2])
        self.assertEqual(
            parent_node.to_html(),
            "<div><span><b>grandchild1</b></span><span><b>grandchild2</b></span></div>",
        )

    def test_to_html_no_children(self):
        parent_node = ParentNode("div", [])
        self.assertEqual(
            parent_node.to_html(),
            "<div></div>",
        )


if __name__ == "__main__":
    unittest.main()
