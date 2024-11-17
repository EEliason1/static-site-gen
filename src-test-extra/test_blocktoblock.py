import unittest
from blocktoblock import block_to_block_type

class TestBlockToBlockType(unittest.TestCase):

    def test_heading(self):
        markdown = "# This is a heading"
        expected = 'heading'
        self.assertEqual(block_to_block_type(markdown), expected)
    
    def test_code_block(self):
        markdown = """```
def hello():
    return "Hello, world!"
```"""
        expected = 'code'
        self.assertEqual(block_to_block_type(markdown), expected)

    def test_quote_block(self):
        markdown = """> This is a quote
> with multiple lines"""
        expected = 'quote'
        self.assertEqual(block_to_block_type(markdown), expected)

    def test_unordered_list(self):
        markdown = """* List item 1
* List item 2"""
        expected = 'unordered_list'
        self.assertEqual(block_to_block_type(markdown), expected)

    def test_ordered_list(self):
        markdown = """1. First item
2. Second item"""
        expected = 'ordered_list'
        self.assertEqual(block_to_block_type(markdown), expected)

    def test_paragraph(self):
        markdown = "This is a normal paragraph."
        expected = 'paragraph'
        self.assertEqual(block_to_block_type(markdown), expected)

    def test_empty_string(self):
        markdown = ""
        expected = 'paragraph'
        self.assertEqual(block_to_block_type(markdown), expected)

    def test_unordered_list_with_dash(self):
        markdown = """- List item 1
- List item 2"""
        expected = 'unordered_list'
        self.assertEqual(block_to_block_type(markdown), expected)

    def test_ordered_list_with_more_than_10_items(self):
        markdown = """1. First item
2. Second item
3. Third item"""
        expected = 'ordered_list'
        self.assertEqual(block_to_block_type(markdown), expected)

    def test_mixed_paragraph_and_list(self):
        markdown = """This is a paragraph

* List item 1
* List item 2"""
        expected = 'unordered_list'
        self.assertEqual(block_to_block_type(markdown.splitlines()[-2]), expected)

if __name__ == '__main__':
    unittest.main()
