import unittest
from textnode import TextNode, TextType
from splitnodes import split_nodes_delimiter

class TestSplitNodesDelimiter(unittest.TestCase):

    def test_split_code(self):
        node = TextNode("This is text with a `code block` word", TextType.NORMAL)
        new_nodes = split_nodes_delimiter([node], "`", TextType.CODE)
        
        self.assertEqual([node.text for node in new_nodes], 
                         ["This is text with a ", "code block", " word"])
        self.assertEqual([node.text_type for node in new_nodes], 
                         [TextType.NORMAL, TextType.CODE, TextType.NORMAL])

    def test_split_bold(self):
        node = TextNode("This is some **bold text**", TextType.NORMAL)
    
        new_nodes = split_nodes_delimiter([node], "**", TextType.BOLD)
    
        expected_texts = ["This is some ", "bold text"]
        expected_types = [TextType.NORMAL, TextType.BOLD]

        self.assertEqual([node.text for node in new_nodes], expected_texts)
        self.assertEqual([node.text_type for node in new_nodes], expected_types)

    def test_split_italic(self):
        node = TextNode("This is *italic text* in the sentence", TextType.NORMAL)
        new_nodes = split_nodes_delimiter([node], "*", TextType.ITALIC)
        
        self.assertEqual([node.text for node in new_nodes], 
                         ["This is ", "italic text", " in the sentence"])
        self.assertEqual([node.text_type for node in new_nodes], 
                         [TextType.NORMAL, TextType.ITALIC, TextType.NORMAL])

    def test_split_multiple_delimiters(self):
        node = TextNode("This is *italic* and `code`", TextType.NORMAL)
    
        new_nodes = split_nodes_delimiter([node], "*", TextType.ITALIC)
    
        new_nodes = split_nodes_delimiter(new_nodes, "`", TextType.CODE)
    
        expected_texts = ["This is ", "italic", " and ", "code"]
        expected_types = [TextType.NORMAL, TextType.ITALIC, TextType.NORMAL, TextType.CODE]
    
        self.assertEqual([node.text for node in new_nodes], expected_texts)
        self.assertEqual([node.text_type for node in new_nodes], expected_types)

    def test_split_empty_text(self):
        node = TextNode("", TextType.NORMAL)
        new_nodes = split_nodes_delimiter([node], "*", TextType.ITALIC)
    
        self.assertEqual([node.text for node in new_nodes], [''])
        self.assertEqual([node.text_type for node in new_nodes], [TextType.NORMAL])

    def test_split_text_with_multiple_delimiters(self):
        node = TextNode("Text *italic* and `code`", TextType.NORMAL)
    
        new_nodes = split_nodes_delimiter([node], "*", TextType.ITALIC)
    
        new_nodes = split_nodes_delimiter(new_nodes, "`", TextType.CODE)
    
        expected_texts = ['Text ', 'italic', ' and ', 'code']
        expected_types = [TextType.NORMAL, TextType.ITALIC, TextType.NORMAL, TextType.CODE]

        self.assertEqual([node.text for node in new_nodes], expected_texts)
        self.assertEqual([node.text_type for node in new_nodes], expected_types)


if __name__ == "__main__":
    unittest.main()
