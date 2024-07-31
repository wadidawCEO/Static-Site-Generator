import unittest

from textnode import TextNode, text_node_to_html_node


class TestTextNode(unittest.TestCase):
    def test_eq(self):
        node_1 = TextNode("This is a text node", "bold")
        node_2 = TextNode("This is a text node", "bold")
        self.assertEqual(node_1, node_2)

    def test_not_eq(self):
        node_1 = TextNode("This is a text node", "italic")
        node_2 = TextNode("This is a text node", "bold")
        self.assertNotEqual(node_1, node_2)

    def test_not_eq_url_none(self):
        node_1 = TextNode("This is a text node", "bold", "www.bootdev.com")
        node_2 = TextNode("This is a text node", "bold", None)
        self.assertNotEqual(node_1, node_2)
    
    def test_text_to_html(self):
        node = TextNode("sample text", "bold")
        html_node = text_node_to_html_node(node).to_html()
        expected_output = "<b>sample text</b>"
        self.assertEqual(html_node, expected_output)
    
    def test_text_to_html_link(self):
        node = TextNode("sample text", "link", "www.google.com")
        html_node = text_node_to_html_node(node).to_html()
        expected_output = '<a href="www.google.com">sample text</a>'
        self.assertEqual(html_node, expected_output)
    
    def test_test_to_html_image(self):
        node = TextNode("sample text", "image", "www.google.com")
        html_node = text_node_to_html_node(node).to_html()
        expected_output = '<img src="www.google.com" alt="sample text">'
        self.assertEqual(html_node, expected_output)
    
    def test_test_to_html_invalid(self):
        with self.assertRaises(Exception) as message:
            node = TextNode("sample text", "nothing", "www.google.com")
            text_node_to_html_node(node)
        self.assertTrue("Not the right text type" in str(message.exception))

if __name__ == "__main__":
    unittest.main()