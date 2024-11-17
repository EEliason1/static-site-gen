import unittest
from textnode import TextNode, TextType
from splitnodes import split_nodes_image, split_nodes_link

class TestSplitNodeImageAndLink(unittest.TestCase):

    def test_split_nodes_image_single(self):
        node = TextNode(
            "This is a simple text with an ![image](https://image.url) embedded.",
            TextType.NORMAL,
        )
        new_nodes = split_nodes_image([node])
        self.assertEqual(
            new_nodes,
            [
                TextNode("This is a simple text with an ", TextType.NORMAL),
                TextNode("image", TextType.IMAGE, "https://image.url"),
                TextNode(" embedded.", TextType.NORMAL),
            ]
        )

    def test_split_nodes_link_single(self):
        node = TextNode(
            "This is a simple text with a link [to boot dev](https://www.boot.dev).",
            TextType.NORMAL,
        )
        new_nodes = split_nodes_link([node])
        self.assertEqual(
            new_nodes,
            [
                TextNode("This is a simple text with a link ", TextType.NORMAL),
                TextNode("to boot dev", TextType.LINK, "https://www.boot.dev"),
                TextNode(".", TextType.NORMAL),
            ]
        )

    def test_split_nodes_image_multiple(self):
        node = TextNode(
            "This is an image ![image](https://image.url) and another ![pic](https://pic.url).",
            TextType.NORMAL,
        )
        new_nodes = split_nodes_image([node])
        self.assertEqual(
            new_nodes,
            [
                TextNode("This is an image ", TextType.NORMAL),
                TextNode("image", TextType.IMAGE, "https://image.url"),
                TextNode(" and another ", TextType.NORMAL),
                TextNode("pic", TextType.IMAGE, "https://pic.url"),
                TextNode(".", TextType.NORMAL),
            ]
        )

    def test_split_nodes_link_multiple(self):
        node = TextNode(
            "Visit the [Boot Dev](https://boot.dev) website or check out [YouTube](https://youtube.com).",
            TextType.NORMAL,
        )
        new_nodes = split_nodes_link([node])
        self.assertEqual(
            new_nodes,
            [
                TextNode("Visit the ", TextType.NORMAL),
                TextNode("Boot Dev", TextType.LINK, "https://boot.dev"),
                TextNode(" website or check out ", TextType.NORMAL),
                TextNode("YouTube", TextType.LINK, "https://youtube.com"),
                TextNode(".", TextType.NORMAL),
            ]
        )

    def test_split_nodes_image_and_text(self):
        node = TextNode(
            "Here is some text before an image ![image](https://image.url) and some text after.",
            TextType.NORMAL,
        )
        new_nodes = split_nodes_image([node])
        self.assertEqual(
            new_nodes,
            [
                TextNode("Here is some text before an image ", TextType.NORMAL),
                TextNode("image", TextType.IMAGE, "https://image.url"),
                TextNode(" and some text after.", TextType.NORMAL),
            ]
        )

    def test_split_nodes_link_and_text(self):
        node = TextNode(
            "Here is a link [BootDev](https://boot.dev) followed by more text.",
            TextType.NORMAL,
        )
        new_nodes = split_nodes_link([node])
        self.assertEqual(
            new_nodes,
            [
                TextNode("Here is a link ", TextType.NORMAL),
                TextNode("BootDev", TextType.LINK, "https://boot.dev"),
                TextNode(" followed by more text.", TextType.NORMAL),
            ]
        )

    def test_split_nodes_image_none(self):
        node = TextNode(
            "This text contains no images at all.",
            TextType.NORMAL,
        )
        new_nodes = split_nodes_image([node])
        self.assertEqual(new_nodes, [node])

    def test_split_nodes_link_none(self):
        node = TextNode(
            "This text contains no links.",
            TextType.NORMAL,
        )
        new_nodes = split_nodes_link([node])
        self.assertEqual(new_nodes, [node])

    def test_empty_text(self):
        node = TextNode(
            "",
            TextType.NORMAL,
        )
        new_nodes = split_nodes_image([node])
        self.assertEqual(new_nodes, [node])

    def test_split_nodes_image_and_link(self):
        node = TextNode(
            "Here is an image ![image](https://image.url) and a link [BootDev](https://boot.dev).",
            TextType.NORMAL,
        )
        new_nodes_image = split_nodes_image([node])
        new_nodes_link = split_nodes_link([node])

        self.assertEqual(
            new_nodes_image,
            [
                TextNode("Here is an image ", TextType.NORMAL),
                TextNode("image", TextType.IMAGE, "https://image.url"),
                TextNode(" and a link [BootDev](https://boot.dev).", TextType.NORMAL),
            ]
        )

        self.assertEqual(
            new_nodes_link,
            [
                TextNode("Here is an image ![image](https://image.url) and a link ", TextType.NORMAL),
                TextNode("BootDev", TextType.LINK, "https://boot.dev"),
                TextNode(".", TextType.NORMAL),
            ]
        )

    def test_split_nodes_consecutive_links(self):
        node = TextNode(
            "Links [first](https://first.com) and [second](https://second.com).",
            TextType.NORMAL,
        )
        new_nodes = split_nodes_link([node])
        self.assertEqual(
            new_nodes,
            [
                TextNode("Links ", TextType.NORMAL),
                TextNode("first", TextType.LINK, "https://first.com"),
                TextNode(" and ", TextType.NORMAL),
                TextNode("second", TextType.LINK, "https://second.com"),
                TextNode(".", TextType.NORMAL),
            ]
        )

    def test_split_nodes_image_and_link_middle(self):
        node = TextNode(
            "Text before link [Link](https://link.com) and after image ![Image](https://image.com).",
            TextType.NORMAL,
        )
        new_nodes = split_nodes_link([node])
        new_nodes_image = split_nodes_image([node])
        self.assertEqual(
            new_nodes,
            [
                TextNode("Text before link ", TextType.NORMAL),
                TextNode("Link", TextType.LINK, "https://link.com"),
                TextNode(" and after image ![Image](https://image.com).", TextType.NORMAL),
            ]
        )
        
        self.assertEqual(
            new_nodes_image,
            [
                TextNode("Text before link [Link](https://link.com) and after image ", TextType.NORMAL),
                TextNode("Image", TextType.IMAGE, "https://image.com"),
                TextNode(".", TextType.NORMAL),
            ]
        )

if __name__ == "__main__":
    unittest.main()
