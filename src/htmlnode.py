class HTMLNode():
    def __init__(self,tag=None,value=None,children=None,props=None):
        self.tag = tag
        self.value = value
        self.children = children
        self.props = props
    def to_html(self):
        raise NotImplementedError
    
    def props_to_html(self):
        rstring = ''
        if self.props is not None:
            for key in self.props:
                rstring += f' {key}="{self.props[key]}"'
        return rstring
    
    def __eq__(self, other):
        if not isinstance(other, HTMLNode):
            return False
        return (self.tag == other.tag and
                self.value == other.value and
                self.children == other.children and
                self.props == other.props)
    
    def __repr__(self):
        return(f"{self.tag}, {self.value}, {self.children}, {self.props}")

class LeafNode(HTMLNode):
    def __init__(self, tag, value, props=None):
        super().__init__(tag, value, children=None, props=props)
    
    def to_html(self):
        if self.value is None:
            raise ValueError
        elif self.tag is None:
            return f"{self.value}"
        else:
            return f"<{self.tag}{self.props_to_html()}>{self.value}</{self.tag}>"
        
class ParentNode(HTMLNode):
    def __init__(self, tag, children, props=None):
        super().__init__(tag, value=None, children=children, props=props)

    def to_html(self):
        if self.tag is None:
            raise ValueError("No tag was given.")
        if self.children is None:
            raise ValueError("No children were given.")
        if not isinstance(self.children, list):
            raise TypeError("children is not of list type")
        rstring = f"<{self.tag}{self.props_to_html()}>"
        for child in self.children:
            rstring += child.to_html()
        return rstring + f"</{self.tag}>"

        
    