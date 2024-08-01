class HTMLNode:
    def __init__(self, tag = None, value = None, children = None, props = None):
        self.tag = tag
        self.value = value
        self.children = children
        self.props = props

    def to_html(self):
        raise NotImplementedError

    def props_to_html(self):
        # Return props in strings by iterating the whole props using dict.items()
        props_string = ""
        if self.props == None:
            return ""
        for k,v in self.props.items():
            props_string += f' {k}="{v}"'
        return props_string

    def __repr__(self):
        # Print HTMLNode object
        return f"tag = {self.tag}, value = {self.value}, children = {self.children}, props = {self.props}"

class LeafNode(HTMLNode):
    def __init__(self, tag = None, value = None, props = None):
        super().__init__(tag, value, None, props)
        if self.value == None:
            raise ValueError("Need Value")
    
    def to_html(self):
        if self.value == None:
            raise ValueError("Need Value")
        if self.tag == None:
            return self.value
        # Return props in strings by iterating the whole props using dict.items() if theres is self.props    
        props_string = ""
        if self.props:
            for k,v in self.props.items():
                props_string += f' {k}="{v}"'
        
        if self.tag == "img":
            return f"<{self.tag}{props_string}>"

        return f"<{self.tag}{props_string}>{self.value}</{self.tag}>"

class ParentNode(HTMLNode):
    def __init__(self, tag = None, children = None, props = None):
        super().__init__(tag, None, children, props)
        if children == None:
            raise Exception("Need Children Argument")

    def to_html(self):
        if self.tag == None:
            raise ValueError("Need Tag")
        if not self.children:
            raise ValueError("Need Children Argument")
        result = ""
        # Iterate all self.children and running to_html method
        for child in self.children:
            result += child.to_html()
        return f"<{self.tag}>{result}</{self.tag}>"

