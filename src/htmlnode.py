class HTMLnode:
    def __init__(self, tag=None, value=None, children=None, props=None):
        self.tag = tag
        self.value = value
        self.children = children
        self.props = props

    def to_html(self):
        raise NotImplementedError("not yet implemented")
    
    def props_to_html(self):
        if self == None:
            return ""
        res = ''.join(list(map(lambda key, value: f' {key}="{value}"', self.keys(), self.values())))
        return res
    
    def __repr__(self):
        return f"HTMLNode({self.tag}, {self.value}, {self.children}, {self.props})"
    
class LeafNode(HTMLnode):
    def __init__(self, tag, value, props=None):
        super().__init__(tag, value, children=None, props=props)

    def __repr__(self):
        return f"Value: {self.value}; Tag: {self.tag}; Props: {self.props}"

    def to_html(self):
        if self.value == None:
            raise ValueError("leaf node must have a value")
        if self.props == None:
            if self.tag == None:
                return f"{self.value}"
            # else: 
                # return f"<{self.tag}>{self.value}</{self.tag}>"
        return f"<{self.tag}{HTMLnode.props_to_html(self.props)}>{self.value}</{self.tag}>"
        