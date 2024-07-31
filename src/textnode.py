from htmlnode import LeafNode

class TextNode:
    def __init__(self, text, text_type, url = None):
        self.text = text
        self.text_type = text_type
        self.url = url
    
    def __eq__(self, other):
        if (
            self.text == other.text 
            and self.text_type == other.text_type 
            and self.url == other.url
        ):
            return True
        return False

    def __repr__(self):
        return f"TextNode({self.text}, {self.text_type}, {self.url})"

def text_node_to_html_node(text_node):
    dic_text_type = {"text": "", "bold": "b", "italic": "i", "code": "code", "link": "a", "image": "img"}

    if text_node.text_type not in dic_text_type:
        raise Exception("Not the right text type")
    
    tag = dic_text_type[text_node.text_type]
    props = None
    text = text_node.text

    if text_node.text_type == "image":
        text = ""
        props = {"src": text_node.url, "alt": text_node.text}

    elif text_node.text_type == "link":
        props = {"href": text_node.url}

    return LeafNode(tag, text, props)
        

