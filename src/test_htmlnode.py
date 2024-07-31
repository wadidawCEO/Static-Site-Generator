import unittest

from htmlnode import HTMLNode, LeafNode, ParentNode

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
    
    def test_leaf_to_html(self):
        node = LeafNode("p", "sample text", None)
        to_html_output = node.to_html()
        expected_output = "<p>sample text</p>"
        self.assertEqual(to_html_output, expected_output)
    
    def test_leaf_to_html_props(self):
        node = LeafNode("a", "sample text", {"href": "https://www.google.com"})
        to_html_output = node.to_html()
        expected_output = '<a href="https://www.google.com">sample text</a>'
        self.assertEqual(to_html_output, expected_output)
    
    def test_parent_to_html(self):
        node = ParentNode(
            "p",
            [
                LeafNode("b", "Bold text"),
                LeafNode(None, "Normal text"),
                LeafNode("i", "italic text"),
                LeafNode(None, "Normal text"),
            ],
        )
        to_html_output = node.to_html()
        expected_output = "<p><b>Bold text</b>Normal text<i>italic text</i>Normal text</p>"
        self.assertEqual(to_html_output, expected_output)
    
    def test_parent_to_html_no_children(self):
        with self.assertRaises(Exception) as message:
            node = ParentNode("p")
            node.to_html()
        self.assertTrue("Need Children Argument" in str(message.exception))

    def test_parent_to_html_children_empty_list(self):
        with self.assertRaises(Exception) as message:
            node = ParentNode("p", [])
            node.to_html()
        self.assertTrue("Need Children Argument" in str(message.exception))

    def test_parent_to_html_children_single(self):
        node = ParentNode(
            "p",
            [
                LeafNode("b", "Bold text"),
            ],
        )
        to_html_output = node.to_html()
        expected_output = "<p><b>Bold text</b></p>"
        self.assertEqual(to_html_output, expected_output)
    
    def test_parent_to_html_parent_inside(self):
        node = ParentNode(
            "p",
            [
                ParentNode(
                    "p",
                    [
                        LeafNode("b", "Bold text"),
                        LeafNode(None, "Normal text"),
                    ]
                ),
                LeafNode("i", "italic text"),
                LeafNode(None, "Normal text"),
            ],
        )
        to_html_output = node.to_html()
        expected_output = "<p><p><b>Bold text</b>Normal text</p><i>italic text</i>Normal text</p>"
        self.assertEqual(to_html_output, expected_output)

    def test_parent_to_html_parent_inside_deep(self):
        node = ParentNode(
            "p",
            [
                ParentNode(
                    "p",
                    [
                        ParentNode(
                            "p",
                            [
                                LeafNode("b", "Bold text"),
                            ]
                        ),
                        LeafNode(None, "Normal text"),
                    ]
                ),
                LeafNode("i", "italic text"),
                LeafNode(None, "Normal text"),
            ],
        )
        to_html_output = node.to_html()
        expected_output = "<p><p><p><b>Bold text</b></p>Normal text</p><i>italic text</i>Normal text</p>"
        self.assertEqual(to_html_output, expected_output)
    
    def test_parent_to_html_no_tag(self):
        with self.assertRaises(Exception) as message:
            node = ParentNode(
                None, 
                [
                LeafNode("b", "Bold text"),
                LeafNode(None, "Normal text"),
                LeafNode("i", "italic text"),
                LeafNode(None, "Normal text"),
                ],
            )
            node.to_html()

        self.assertTrue("Need Tag" in str(message.exception))
    
if __name__ == "__main__":
    unittest.main()