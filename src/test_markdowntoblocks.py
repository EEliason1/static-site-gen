import unittest
from markdowntoblocks import markdown_to_blocks

class TestMarkdownToBlocks(unittest.TestCase):

    def test_heading_and_paragraph(self):
        markdown = """# Heading

This is a paragraph with **bold** text."""
        expected = [
            "# Heading",
            "This is a paragraph with **bold** text."
        ]
        result = markdown_to_blocks(markdown)
        self.assertEqual(result, expected)

    def test_list_and_code_block(self):
        markdown = (
            "* List item 1\n"
            "* List item 2\n\n"
            "```\n"
            "def hello():\n"
            "    return \"Hello, world!\"\n"
            "```"
        )
        expected = [
            "* List item 1\n* List item 2",
            "```\ndef hello():\n    return \"Hello, world!\"\n```"
        ]
        result = markdown_to_blocks(markdown)
        self.assertEqual(result, expected)

    def test_multiple_paragraphs(self):
        markdown = """First paragraph.

Second paragraph.

Third paragraph."""
        expected = [
            "First paragraph.",
            "Second paragraph.",
            "Third paragraph."
        ]
        result = markdown_to_blocks(markdown)
        self.assertEqual(result, expected)

    def test_blockquote(self):
        markdown = """> This is a blockquote.

This is normal text."""
        expected = [
            "> This is a blockquote.",
            "This is normal text."
        ]
        result = markdown_to_blocks(markdown)
        self.assertEqual(result, expected)

    def test_mixed_content(self):
        markdown = """# Heading

Paragraph with **bold** and *italic* text.

* List item
* Another list item"""
        expected = [
            "# Heading",
            "Paragraph with **bold** and *italic* text.",
            "* List item\n* Another list item"
        ]
        result = markdown_to_blocks(markdown)
        self.assertEqual(result, expected)

    def test_empty_input(self):
        markdown = ""
        expected = []
        result = markdown_to_blocks(markdown)
        self.assertEqual(result, expected)

    def test_only_whitespace(self):
        markdown = "   \n\n  \n"
        expected = []
        result = markdown_to_blocks(markdown)
        self.assertEqual(result, expected)

    def test_code_block(self):
        markdown = """```
print("Hello, world!")
```"""
        expected = ["```\nprint(\"Hello, world!\")\n```"]
        result = markdown_to_blocks(markdown)
        self.assertEqual(result, expected)

    def test_list_with_empty_lines(self):
        markdown = """* Item 1

* Item 2

* Item 3"""
        expected = ["* Item 1", "* Item 2", "* Item 3"]
        result = markdown_to_blocks(markdown)
        self.assertEqual(result, expected)

if __name__ == "__main__":
    unittest.main()
