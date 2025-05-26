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
        super().__init__(tag, value, None, props)

    def __repr__(self):
        return f"LeafNode({self.tag}, {self.value}, {self.props})"

    def to_html(self):
        if self.value is None:
            raise ValueError("node must have a value")
        if self.tag is None:
            return f"{self.value}"
        return f"<{self.tag}{HTMLnode.props_to_html(self.props)}>{self.value}</{self.tag}>"


class ParentNode(HTMLnode):
    def __init__(self, tag, children, props=None):
        super().__init__(tag, None, children, props)
        self.children = [children]
    
    def to_html(self):
        if self.tag is None:
            raise ValueError("tag required")
        if self.children is None:
            raise ValueError("node must have a value")
        return f"<{self.tag}{HTMLnode.props_to_html(self.props)}>{ParentNode.children_format(self.children)}</{self.tag}>"
    
    # My original method, doesn't take nested lists into account       
    # def children_format(self):
    #     formatted_code = ""
    #     if len(self) == 0:
    #         return formatted_code
    #     formatted_code += self[0].to_html()
    #     return formatted_code + ParentNode.children_format(self[1:])

    # '''
    # My attempt at taking nested lists into account (doesn't seem to work)

    def children_format(self):
        formatted_code = ""
        for node in self:
            if isinstance(node, list):
                formatted_code += ParentNode.children_format(node)
            else:
                formatted_code += node.to_html()
        return formatted_code
    
    def __repr__(self):
        return f"ParentNode({self.tag}, {self.children}, {self.props})"