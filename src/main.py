from textnode import TextNode, split_nodes_delimiter
from htmlnode import HTMLNode, LeafNode

def main():
    test = TextNode("This is a text node", "bold", "https://www.boot.dev")
    test_2 = HTMLNode("sasa", "sasa", "sasasa", "sasasa")
    test_3 = LeafNode("a", "sample text", {"href": "https://www.google.com"})
    test_4 = [TextNode("This is *a text node*", "text")]
    print(split_nodes_delimiter(test_4, "*", "bold"))

if __name__ == "__main__":
    main()