import unittest

from extract_markdown import extract_markdown_images, extract_markdown_links

class TestTextNode(unittest.TestCase):

    def test_extract_markdown_images(self):
        text = "This is text with a ![rick roll](https://i.imgur.com/aKaOqIh.gif) and ![obi wan](https://i.imgur.com/fJRm4Vk.jpeg)"
        links = extract_markdown_images(text)
        expected_output =  [("rick roll", "https://i.imgur.com/aKaOqIh.gif"), ("obi wan", "https://i.imgur.com/fJRm4Vk.jpeg")]
        self.assertEqual(links, expected_output)

    def test_extract_markdown_links(self):
        text = "This is text with a link [to boot dev](https://www.boot.dev) and [to youtube](https://www.youtube.com/@bootdotdev)"
        links = extract_markdown_links(text)
        expected_output =  [("to boot dev", "https://www.boot.dev"), ("to youtube", "https://www.youtube.com/@bootdotdev")]
        self.assertEqual(links, expected_output)
    
    def test_extract_markdown_no_images(self):
        text = "This text has no images."
        links = extract_markdown_images(text)
        expected_output = []
        self.assertEqual(links, expected_output)

    def test_extract_markdown_no_links(self):
        text = "This text has no links."
        links = extract_markdown_links(text)
        expected_output = []
        self.assertEqual(links, expected_output)

    def test_mixed_content(self):
        text = "This is text with a ![image](https://i.imgur.com/image.jpg) and a [link](https://www.example.com)"
        image_links = extract_markdown_images(text)
        expected_images = [("image", "https://i.imgur.com/image.jpg")]
        self.assertEqual(image_links, expected_images)
        
        regular_links = extract_markdown_links(text)
        expected_links = [("link", "https://www.example.com")]
        self.assertEqual(regular_links, expected_links)
    
    def test_malformed_syntax(self):
        text = "This text has [malformed ![image](https://i.imgur.com/image.jpg) and link(https://www.example.com)"
        image_links = extract_markdown_images(text)
        expected_images = [("image", "https://i.imgur.com/image.jpg")]
        self.assertEqual(image_links, expected_images)
        
        regular_links = extract_markdown_links(text)
        expected_links = []
        self.assertEqual(regular_links, expected_links)
    

if __name__ == "__main__":
    unittest.main()