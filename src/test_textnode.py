import unittest

from textnode import TextNode


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
    


if __name__ == "__main__":
    unittest.main()