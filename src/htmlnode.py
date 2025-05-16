class HTMLnode:
    def __init__(self, tag=None, value=None, children=None, props=None):
        self.tag = tag
        self.value = value
        self.children = children
        self.props = props

    def to_html(self):
        raise NotImplementedError("not yet implemented")
    
    def props_to_html(self):
        res = ''.join(list(map(lambda key, value: f' {key}="{value}"', self.keys(), self.values())))
        return res
    
    def __repr__(self):
        return f"Tag: {self.tag}\nValue: {self.value}\nchildren: {self.children}\nProps: {self.props}"