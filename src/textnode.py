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

def split_nodes_delimiter(old_nodes, delimiter, text_type):
# Could be improve to handle nested delimiter

    accepted_text_type = ["italic", "bold", "code", "link", "image"]
    new_nodes = []

    for node in old_nodes:
        if node.text_type == "text":
            if delimiter in node.text:
                text_splitted = node.text.split(delimiter)
                
                if len(text_splitted) % 2 == 0:
                    raise ValueError("Invalid markdown, formatted section not closed")

                for index, value in enumerate(text_splitted):
                    if value: # Only append non-empty text_splitted
                    
                        if index % 2 == 0:
                        # Even indices is always the non delimited text
                            new_nodes.append(TextNode(value, "text", node.url))
                        else:
                        # Odd indices is always the delimited text
                            new_nodes.append(TextNode(value, text_type, node.url))

                    else:
                        continue
            else:
                new_nodes.append(node)

        elif node.text_type in accepted_text_type:
            # Append node if it's one of the accepted types
            new_nodes.append(node)

        else:
            raise Exception("Not the right node text type")

    return new_nodes





        

