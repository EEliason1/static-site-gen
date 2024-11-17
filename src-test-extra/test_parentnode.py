import unittest
from htmlnode import LeafNode, ParentNode

class TestParentNode(unittest.TestCase):
    def test_parentnode_to_html(self):
        node = ParentNode(
            "p",
            [
                LeafNode("b", "Bold text"),
                LeafNode(None, "Normal text"),
                LeafNode("i", "italic text"),
                LeafNode(None, "Normal text"),
            ],
        )
        expected_html = "<p><b>Bold text</b>Normal text<i>italic text</i>Normal text</p>"
        self.assertEqual(node.to_html(), expected_html)

    def test_parentnode_no_tag(self):
        with self.assertRaises(ValueError):
            ParentNode(None, [LeafNode("b", "test")])

    def test_parentnode_no_children(self):
        with self.assertRaises(ValueError):
            ParentNode("div", [])

    def test_parentnode_with_props(self):
        node = ParentNode(
            "div", 
            [LeafNode("p", "Paragraph text")],
            props={"class": "container", "id": "main"}
        )
        expected_html = '<div class="container" id="main"><p>Paragraph text</p></div>'
        self.assertEqual(node.to_html(), expected_html)

    def test_parentnode_with_nested_parents(self):
        node = ParentNode(
            "div", 
            [
                ParentNode(
                    "section", 
                    [LeafNode("h1", "Header 1"), LeafNode("p", "Paragraph inside section")]
                ),
                ParentNode(
                    "footer", 
                    [LeafNode("p", "Footer paragraph")]
                ),
            ]
        )
        expected_html = (
            '<div>'
            '<section><h1>Header 1</h1><p>Paragraph inside section</p></section>'
            '<footer><p>Footer paragraph</p></footer>'
            '</div>'
        )
        self.assertEqual(node.to_html(), expected_html)

    def test_parentnode_with_mixed_children(self):
        node = ParentNode(
            "div", 
            [
                LeafNode("span", "First span"),
                ParentNode(
                    "section", 
                    [LeafNode("p", "Paragraph inside section")]
                ),
                LeafNode("span", "Second span")
            ]
        )
        expected_html = (
            '<div>'
            '<span>First span</span>'
            '<section><p>Paragraph inside section</p></section>'
            '<span>Second span</span>'
            '</div>'
        )
        self.assertEqual(node.to_html(), expected_html)

    def test_parentnode_empty_tag(self):
        with self.assertRaises(ValueError):
            ParentNode("", [LeafNode("b", "test")])

    def test_parentnode_deep_nesting(self):
        deep_node = ParentNode(
            "div",
            [ParentNode(
                "div",
                [ParentNode(
                    "div",
                    [ParentNode(
                        "div",
                        [LeafNode("p", "Deeply nested text")]
                    )]
                )]
            )]
        )
        expected_html = (
            '<div>'
            '<div>'
            '<div>'
            '<div>'
            '<p>Deeply nested text</p>'
            '</div>'
            '</div>'
            '</div>'
            '</div>'
        )
        self.assertEqual(deep_node.to_html(), expected_html)

    def test_parentnode_single_child_in_nested_parent(self):
        node = ParentNode(
            "div", 
            [ParentNode("section", [LeafNode("h1", "Title")])]
        )
        expected_html = (
            '<div>'
            '<section><h1>Title</h1></section>'
            '</div>'
        )
        self.assertEqual(node.to_html(), expected_html)

    def test_parentnode_single_child_with_mixed_nodes(self):
        node = ParentNode(
            "div", 
            [
                LeafNode("span", "A span"),
                ParentNode("footer", [LeafNode("p", "Footer paragraph")])
            ]
        )
        expected_html = (
            '<div>'
            '<span>A span</span>'
            '<footer><p>Footer paragraph</p></footer>'
            '</div>'
        )
        self.assertEqual(node.to_html(), expected_html)

    def test_parentnode_large_number_of_children(self):
        children = [LeafNode("p", f"Paragraph {i}") for i in range(1000)]
        node = ParentNode("div", children)
        expected_html = "<div>" + "".join([f"<p>Paragraph {i}</p>" for i in range(1000)]) + "</div>"
        self.assertEqual(node.to_html(), expected_html)

if __name__ == "__main__":
    unittest.main()
