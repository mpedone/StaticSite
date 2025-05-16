import unittest
from htmlnode import HTMLnode

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
        self.assertEqual(test_html, "Tag: testTag\nValue: testValue\nchildren: ['testChild1', 'testChild2']\nProps: {'prop1': 'val1', 'prop2': 'val2'}")


if __name__ == "__main__":
    unittest.main()