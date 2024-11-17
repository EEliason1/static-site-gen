import unittest
from htmlnode import LeafNode

class TestLeafNode(unittest.TestCase):

    def test_leafnode_to_html(self):
        node = LeafNode(tag="p", value="This is a paragraph of text.")
        self.assertEqual(node.to_html(), "<p>This is a paragraph of text.</p>")

    def test_leafnode_with_props(self):
        node = LeafNode(tag="a", value="Click me!", props={"href": "https://www.google.com"})
        self.assertEqual(node.to_html(), '<a href="https://www.google.com">Click me!</a>')

    def test_leafnode_no_tag(self):
        node = LeafNode(tag=None, value="Just raw text")
        self.assertEqual(node.to_html(), "Just raw text")

    def test_leafnode_no_value(self):
        with self.assertRaises(ValueError):
            LeafNode(tag="p", value=None)

    def test_leafnode_repr(self):
        node = LeafNode(tag="div", value="Hello", props={"class": "container"})
        self.assertEqual(repr(node), "LeafNode(tag=div, value=Hello, children=[], props={'class': 'container'})")

if __name__ == "__main__":
    unittest.main()