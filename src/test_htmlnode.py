import unittest
from htmlnode import HTMLnode, LeafNode

class TestHTMLNode(unittest.TestCase):
    def test_default(self):
        node = HTMLnode()
        self.assertIsNone(node.tag)
        self.assertIsNone(node.value)
        self.assertIsNone(node.children)
        self.assertIsNone(node.props)

    def test_props_to_html(self):
        test_props = {"href": "https://test.com", "target": "_blank",}
        html_target = ' href="https://test.com" target="_blank"'
        node = HTMLnode(props = test_props)
        test_html = HTMLnode.props_to_html(node.props)
        self.assertEqual(test_html, html_target)
    
    def test_repr(self):
        tag = "testTag"
        value = "testValue"
        children = ["testChild1", "testChild2"]
        props = {"prop1": "val1", "prop2": "val2"}
        node = HTMLnode(tag, value, children, props)
        test_html = HTMLnode.__repr__(node)
        # self.assertEqual(str(test_output).split("\n")[0], f"Tag: {tag}")
        self.assertEqual(test_html, "HTMLNode(testTag, testValue, ['testChild1', 'testChild2'], {'prop1': 'val1', 'prop2': 'val2'})")
    
    def test_leaf_to_html_p(self):
        node = LeafNode("p", "Hello, world!")
        self.assertEqual(node.to_html(), "<p>Hello, world!</p>")
    
    def test_leaf_to_html_a(self):
        node = LeafNode("a", "Click Here", {"href": "https://test.com", "target": "_blank"})
        self.assertEqual(node.to_html(), '<a href="https://test.com" target="_blank">Click Here</a>')
    
    def test_leaf_to_html_no_tag(self):
        node = LeafNode(None, "this is a paragraph")
        self.assertEqual(node.to_html(), "this is a paragraph")


if __name__ == "__main__":
    unittest.main()