import unittest
from textnode import TextNode, text_node_to_html_node

class TestTextNodeToHtmlNode(unittest.TestCase):

    def test_normal_text(self):
        node = TextNode("Just some text", "normal")
        html_node = text_node_to_html_node(node)
        self.assertEqual(html_node.to_html(), "Just some text")

    def test_bold_text(self):
        node = TextNode("Bold text", "bold")
        html_node = text_node_to_html_node(node)
        self.assertEqual(html_node.to_html(), "<b>Bold text</b>")

    def test_italic_text(self):
        node = TextNode("Italic text", "italic")
        html_node = text_node_to_html_node(node)
        self.assertEqual(html_node.to_html(), "<i>Italic text</i>")

    def test_code_text(self):
        node = TextNode("Code text", "code")
        html_node = text_node_to_html_node(node)
        self.assertEqual(html_node.to_html(), "<code>Code text</code>")

    def test_link(self):
        node = TextNode("Click here", "link", "https://www.example.com")
        html_node = text_node_to_html_node(node)
        self.assertEqual(html_node.to_html(), '<a href="https://www.example.com">Click here</a>')

    def test_image(self):
        node = TextNode("An image", "image", "image.jpg")
        html_node = text_node_to_html_node(node)
        self.assertEqual(html_node.to_html(), '<img src="image.jpg" alt="An image">')

    def test_link_without_url(self):
        node = TextNode("Click here", "link")
        with self.assertRaises(ValueError):
            text_node_to_html_node(node)

    def test_image_without_url(self):
        node = TextNode("An image", "image")
        with self.assertRaises(ValueError):
            text_node_to_html_node(node)

    def test_invalid_text_type(self):
        with self.assertRaises(ValueError) as context:
            TextNode("Unsupported type", "unsupported")
        self.assertEqual(str(context.exception), "Invalid text type: 'unsupported'. Must be one of normal, bold, italic, code, link, image")

if __name__ == "__main__":
    unittest.main()
