import unittest

from textnode import TextNode, text_node_to_html_node, split_nodes_delimiter, split_nodes_image, split_nodes_link, text_to_textnodes


class TestTextNode(unittest.TestCase):

###TextNode###
    def test_TextNode_eq(self):
        node_1 = TextNode("This is a text node", "bold")
        node_2 = TextNode("This is a text node", "bold")
        self.assertEqual(node_1, node_2)

    def test_TextNode_not_eq(self):
        node_1 = TextNode("This is a text node", "italic")
        node_2 = TextNode("This is a text node", "bold")
        self.assertNotEqual(node_1, node_2)

    def test_TextNode_not_eq_url_none(self):
        node_1 = TextNode("This is a text node", "bold", "www.bootdev.com")
        node_2 = TextNode("This is a text node", "bold", None)
        self.assertNotEqual(node_1, node_2)

###text_to_html###    
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

###split_nodes_delimiter###    
    def test_split_nodes_delimiter_bold(self):
        node = [TextNode("This is text with a **bolded phrase** word", "text")]
        result = split_nodes_delimiter(node, "**", "bold")
        expected_output = [
                TextNode("This is text with a ", "text"),
                TextNode("bolded phrase", "bold"),
                TextNode(" word", "text"),
            ]
        self.assertEqual(result, expected_output)
    
    def test_split_nodes_delimiter_no_delimiters(self):
        node = [TextNode("This is text without delimiters", "text")]
        result = split_nodes_delimiter(node, "**", "bold")
        expected_output = [
            TextNode("This is text without delimiters", "text"),
        ]
        self.assertEqual(result, expected_output)

    def test_split_nodes_delimiter_multiple(self):
        node = [TextNode("This **is** text with **multiple** delimiters", "text")]
        result = split_nodes_delimiter(node, "**", "bold")
        expected_output = [
            TextNode("This ", "text"),
            TextNode("is", "bold"),
            TextNode(" text with ", "text"),
            TextNode("multiple", "bold"),
            TextNode(" delimiters", "text"),
        ]
        self.assertEqual(result, expected_output)

    def test_split_nodes_delimiter_empty_text_node(self):
        node = [TextNode("", "text")]
        result = split_nodes_delimiter(node, "**", "bold")
        expected_output = [
            TextNode("", "text"),
        ]
        self.assertEqual(result, expected_output)

    def test_split_nodes_delimiter_at_start(self):
        node = [TextNode("**bolded start** of the text", "text")]
        result = split_nodes_delimiter(node, "**", "bold")
        expected_output = [
            TextNode("bolded start", "bold"),
            TextNode(" of the text", "text"),
        ]
        self.assertEqual(result, expected_output)

    def test_split_nodes_delimiter_at_end(self):
        node = [TextNode("End of the text with **bold**", "text")]
        result = split_nodes_delimiter(node, "**", "bold")
        expected_output = [
            TextNode("End of the text with ", "text"),
            TextNode("bold", "bold"),
        ]
        self.assertEqual(result, expected_output)

    def test_split_nodes_delimiter_invalid_text_type(self):
        with self.assertRaises(Exception) as message:
            node = [TextNode("This is text with a **bolded phrase** word", "wadidaw")]
            result = split_nodes_delimiter(node, "**", "bold")
        self.assertTrue("Not the right node text type" in str(message.exception))

    def test_split_nodes_delimiter_mixed_text_types(self):
        node = [
            TextNode("This is a ", "text"),
            TextNode("link", "link"),
            TextNode(" and *bolded* text", "text")
        ]
        result = split_nodes_delimiter(node, "*", "bold")
        expected_output = [
            TextNode("This is a ", "text"),
            TextNode("link", "link"),
            TextNode(" and ", "text"),
            TextNode("bolded", "bold"),
            TextNode(" text", "text")
        ]
        self.assertEqual(result, expected_output)

    def test_split_nodes_delimiter_invalid_markdown(self):
        with self.assertRaises(ValueError) as message:
            node = [TextNode("This is text with a **uneven bolded phrase word", "text")]
            result = split_nodes_delimiter(node, "**", "bold")
        self.assertTrue("Invalid markdown, formatted section not closed" in str(message.exception))

# split_nodes_image & link
    def test_to_html_image(self):
        node = [TextNode(
            "This is text with a image ![wadidaw](https://i.imgur.com/aKaOqIh.gif) and ![bajibah](https://i.imgur.com/fJRm4Vk.jpeg), hooray", 
            "text"
        )]
        split_node = split_nodes_image(node)
        expected_output = [
            TextNode("This is text with a image ", "text"),
            TextNode("wadidaw", "image", "https://i.imgur.com/aKaOqIh.gif"),
            TextNode(" and ", "text"),
            TextNode("bajibah", "image", "https://i.imgur.com/fJRm4Vk.jpeg"),
            TextNode(", hooray", "text"),
        ]
        self.assertEqual(split_node, expected_output)
    
    def test_to_html_image_multiple_nodes(self):
        node = [
            TextNode("This is text with a image ![wadidaw](https://i.imgur.com/aKaOqIh.gif) and ", "text"),
            TextNode("![bajibah](https://i.imgur.com/fJRm4Vk.jpeg), hooray", "text"),
            TextNode("", "text")
        ]
        split_node = split_nodes_image(node)
        expected_output = [
            TextNode("This is text with a image ", "text"),
            TextNode("wadidaw", "image", "https://i.imgur.com/aKaOqIh.gif"),
            TextNode(" and ", "text"),
            TextNode("bajibah", "image", "https://i.imgur.com/fJRm4Vk.jpeg"),
            TextNode(", hooray", "text"),
        ]
        self.assertEqual(split_node, expected_output)
    
    def test_to_html_link(self):
        node = [TextNode(
            "This is text with a link [to boot dev](https://www.boot.dev) and [to youtube](https://www.youtube.com/@bootdotdev)",
            "text",
        )]
        split_node = split_nodes_link(node)
        expected_output = [
            TextNode("This is text with a link ", "text"),
            TextNode("to boot dev", "link", "https://www.boot.dev"),
            TextNode(" and ", "text"),
            TextNode("to youtube", "link", "https://www.youtube.com/@bootdotdev"),
        ]  
        self.assertEqual(split_node, expected_output)

    def test_to_html_link_multiple_nodes(self):
        node = [
            TextNode("This is text with a link [to boot dev](https://www.boot.dev)", "text"), 
            TextNode(" and [to youtube](https://www.youtube.com/@bootdotdev)","text"),
            TextNode("", "text"),
            TextNode("", "text")
        ]
        split_node = split_nodes_link(node)
        expected_output = [
            TextNode("This is text with a link ", "text"),
            TextNode("to boot dev", "link", "https://www.boot.dev"),
            TextNode(" and ", "text"),
            TextNode("to youtube", "link", "https://www.youtube.com/@bootdotdev"),
        ]
        self.assertEqual(split_node, expected_output)

# text_to_textnodes
    def test_text_to_textnodes(self):
        string = "This is **text** with an *italic* word and a `code block` and an ![obi wan image](https://i.imgur.com/fJRm4Vk.jpeg) and a [link](https://boot.dev)"
        textnode = text_to_textnodes(string)
        expected_output = [
            TextNode("This is ", "text"),
            TextNode("text", "bold"),
            TextNode(" with an ", "text"),
            TextNode("italic", "italic"),
            TextNode(" word and a ", "text"),
            TextNode("code block", "code"),
            TextNode(" and an ", "text"),
            TextNode("obi wan image", "image", "https://i.imgur.com/fJRm4Vk.jpeg"),
            TextNode(" and a ", "text"),
            TextNode("link", "link", "https://boot.dev"),
        ]
        self.assertEqual(expected_output, textnode)

    def test_text_to_textnodes_single_bold(self):
        string = "This is **bold** text"
        textnode = text_to_textnodes(string)
        expected_output = [
            TextNode("This is ", "text"),
            TextNode("bold", "bold"),
            TextNode(" text", "text"),
        ]
        self.assertEqual(expected_output, textnode)
    
    def test_text_to_textnodes_plain_text(self):
        string = "Just plain text without special formatting."
        textnode = text_to_textnodes(string)
        expected_output = [
            TextNode("Just plain text without special formatting.", "text")
        ]
        self.assertEqual(expected_output, textnode)

    def test_text_to_textnodes_none(self):
        string = ""
        textnode = text_to_textnodes(string)
        expected_output = []
        self.assertEqual(expected_output, textnode)

if __name__ == "__main__":
    unittest.main()