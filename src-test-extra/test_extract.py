import unittest
from extract import extract_markdown_images, extract_markdown_links

class TestMarkdownExtraction(unittest.TestCase):

    def test_extract_markdown_images(self):
        text = "This is text with a ![rick roll](https://i.imgur.com/aKaOqIh.gif) and ![obi wan](https://i.imgur.com/fJRm4Vk.jpeg)"
        result = extract_markdown_images(text)
        self.assertEqual(result, [("rick roll", "https://i.imgur.com/aKaOqIh.gif"), 
                                  ("obi wan", "https://i.imgur.com/fJRm4Vk.jpeg")])

    def test_extract_markdown_links(self):
        text = "This is text with a link [to boot dev](https://www.boot.dev) and [to youtube](https://www.youtube.com/@bootdotdev)"
        result = extract_markdown_links(text)
        self.assertEqual(result, [("to boot dev", "https://www.boot.dev"), 
                                  ("to youtube", "https://www.youtube.com/@bootdotdev")])

    def test_no_images(self):
        text = "This is a text with no images!"
        result = extract_markdown_images(text)
        self.assertEqual(result, [])

    def test_no_links(self):
        text = "This is a text with no links!"
        result = extract_markdown_links(text)
        self.assertEqual(result, [])

    def test_mixed_content(self):
        text = "Here is some text with a ![image](https://image.url) and a [link](https://link.url)."
        result_images = extract_markdown_images(text)
        result_links = extract_markdown_links(text)

        self.assertEqual(result_images, [("image", "https://image.url")])

        self.assertEqual(result_links, [("link", "https://link.url")])

    def test_multiple_images(self):
        text = "Some text with ![first image](https://first.url) and ![second image](https://second.url)."
        result = extract_markdown_images(text)
        self.assertEqual(result, [("first image", "https://first.url"), 
                                  ("second image", "https://second.url")])

    def test_multiple_links(self):
        text = "Text with [first link](https://first.link) and [second link](https://second.link)."
        result = extract_markdown_links(text)
        self.assertEqual(result, [("first link", "https://first.link"), 
                                  ("second link", "https://second.link")])

# Run the tests
if __name__ == "__main__":
    unittest.main()