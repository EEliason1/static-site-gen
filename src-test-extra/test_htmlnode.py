import unittest

from htmlnode import HTMLNode

class TestHTMLNode(unittest.TestCase):
    def test_props_to_html(self):
        node = HTMLNode(tag="a", props={"href": "https://www.google.com", "target": "_blank"})
        self.assertEqual(node.props_to_html(), ' href="https://www.google.com" target="_blank"')

    def test_props_to_html_empty(self):
        node = HTMLNode(tag="div", props={})
        self.assertEqual(node.props_to_html(), "")

    def test_htmlnode_repr(self):
        node = HTMLNode(tag="div", value="Hello", props={"class": "container"})
        self.assertEqual(repr(node), "HTMLNode(tag=div, value=Hello, children=[], props={'class': 'container'})")

    def test_htmlnode_repr_empty(self):
        node = HTMLNode()
        self.assertEqual(repr(node), "HTMLNode(tag=None, value=None, children=[], props={})")

if __name__ == "__main__":
    unittest.main()