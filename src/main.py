from textnode import TextNode
from htmlnode import HTMLNode
from htmlnode import LeafNode

def main():
    test = TextNode("This is a text node", "bold", "https://www.boot.dev")
    test_2 = HTMLNode("sasa", "sasa", "sasasa", "sasasa")
    test_3 = LeafNode("a", "sample text", {"href": "https://www.google.com"})
    print(test_3.to_html())

if __name__ == "__main__":
    main()