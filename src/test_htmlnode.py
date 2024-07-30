import unittest

from htmlnode import HTMLNode

class TestHTMLNode(unittest.TestCase):
    def test_props_to_html_with_props(self):
        node = HTMLNode(props={"href": "https://www.google.com", "target": "_blank"})
        expected_output = ' href="https://www.google.com" target="_blank"'
        self.assertEqual(node.props_to_html(), expected_output)

    def test_props_to_html_without_props(self):
        node = HTMLNode()
        expected_output = ""
        self.assertEqual(node.props_to_html(), expected_output)
    
    def test_repr(self):
        node = HTMLNode("h1", "sample text", ["children 1", "children 2"], {"href": "https://www.google.com", "target": "_blank"})
        repr_output = node.__repr__()
        expected_output = "tag = h1, value = sample text, children = ['children 1', 'children 2'], props = {'href': 'https://www.google.com', 'target': '_blank'}"
        self.assertEqual(repr_output, expected_output)

if __name__ == "__main__":
    unittest.main()