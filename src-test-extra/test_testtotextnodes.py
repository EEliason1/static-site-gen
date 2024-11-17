import unittest
from textnode import TextNode, TextType
from splitnodes import text_to_textnodes

class TestTextToTextNodes(unittest.TestCase):

    def test_basic_text(self):
        text = "This is just normal text."
        result = text_to_textnodes(text)
        self.assertEqual(result, [
            TextNode("This is just normal text.", TextType.NORMAL)
        ])

    def test_bold_text(self):
        text = "This is **bold** text."
        result = text_to_textnodes(text)
        self.assertEqual(result, [
            TextNode("This is ", TextType.NORMAL),
            TextNode("bold", TextType.BOLD),
            TextNode(" text.", TextType.NORMAL)
        ])

    def test_italic_text(self):
        text = "This is *italic* text."
        result = text_to_textnodes(text)
        self.assertEqual(result, [
            TextNode("This is ", TextType.NORMAL),
            TextNode("italic", TextType.ITALIC),
            TextNode(" text.", TextType.NORMAL)
        ])

    def test_code_text(self):
        text = "This is `code block` in a sentence."
        result = text_to_textnodes(text)
        self.assertEqual(result, [
            TextNode("This is ", TextType.NORMAL),
            TextNode("code block", TextType.CODE),
            TextNode(" in a sentence.", TextType.NORMAL)
        ])

    def test_image(self):
        text = "Here is an ![obi wan image](https://i.imgur.com/fJRm4Vk.jpeg)."
        result = text_to_textnodes(text)
        self.assertEqual(result, [
            TextNode("Here is an ", TextType.NORMAL),
            TextNode("obi wan image", TextType.IMAGE, "https://i.imgur.com/fJRm4Vk.jpeg"),
            TextNode(".", TextType.NORMAL)
        ])

    def test_link(self):
        text = "This is a [link](https://boot.dev)."
        result = text_to_textnodes(text)
        self.assertEqual(result, [
            TextNode("This is a ", TextType.NORMAL),
            TextNode("link", TextType.LINK, "https://boot.dev"),
            TextNode(".", TextType.NORMAL)
        ])

    def test_mixed_content(self):
        text = "This is **bold** text, *italic* text, `code block`, an ![image](https://image.url), and a [link](https://link.url)."
        result = text_to_textnodes(text)
        self.assertEqual(result, [
            TextNode("This is ", TextType.NORMAL),
            TextNode("bold", TextType.BOLD),
            TextNode(" text, ", TextType.NORMAL),
            TextNode("italic", TextType.ITALIC),
            TextNode(" text, ", TextType.NORMAL),
            TextNode("code block", TextType.CODE),
            TextNode(", an ", TextType.NORMAL),
            TextNode("image", TextType.IMAGE, "https://image.url"),
            TextNode(", and a ", TextType.NORMAL),
            TextNode("link", TextType.LINK, "https://link.url"),
            TextNode(".", TextType.NORMAL)
        ])

    def test_no_inline_elements(self):
        text = "This is plain text with no special elements."
        result = text_to_textnodes(text)
        self.assertEqual(result, [
            TextNode("This is plain text with no special elements.", TextType.NORMAL)
        ])

    def test_empty_string(self):
        text = ""
        result = text_to_textnodes(text)
        self.assertEqual(result, [
            TextNode("", TextType.NORMAL)
        ])
    
    def test_multiple_links(self):
        text = "This is a [first link](https://first.link) and [second link](https://second.link)."
        result = text_to_textnodes(text)
        self.assertEqual(result, [
            TextNode("This is a ", TextType.NORMAL),
            TextNode("first link", TextType.LINK, "https://first.link"),
            TextNode(" and ", TextType.NORMAL),
            TextNode("second link", TextType.LINK, "https://second.link"),
            TextNode(".", TextType.NORMAL)
        ])

if __name__ == "__main__":
    unittest.main()
