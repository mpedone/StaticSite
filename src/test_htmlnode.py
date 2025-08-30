import unittest
from htmlnode import HTMLnode, LeafNode, ParentNode

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
    
    def test_leaf_to_html_no_value(self):
        node = LeafNode(None, None)
        with self.assertRaises(ValueError):
            node.to_html()

    def test_to_html_with_children(self):
        child_node = LeafNode("span", "child")
        parent_node = ParentNode("div", [child_node])
        self.assertEqual(parent_node.to_html(), "<div><span>child</span></div>")

    def test_to_html_with_grandchildren(self):
        grandchild_node = LeafNode("b", "grandchild")
        child_node = ParentNode("span", [grandchild_node])
        parent_node = ParentNode("div", [child_node])
        self.assertEqual(
            parent_node.to_html(),
            "<div><span><b>grandchild</b></span></div>",
        )
    
    def test_to_html_child_with_props(self):
        child_node = LeafNode("span", "Child", {"href": "https://test.com", "target": "_blank"})
        parent_node = ParentNode("div", [child_node])
        self.assertEqual(
            parent_node.to_html(),
            '<div><span href="https://test.com" target="_blank">Child</span></div>')
    
    def test_to_html_lots_of_props(self):
        grandchild_node_1 = LeafNode("span", "grandchild-1", {"class": "tech"})
        grandchild_node_2 = LeafNode("a", "grandchild-2", {"href": "https://yeah.no"})
        grandchild_node_3 = LeafNode("span", "grandchild-3", {"class": "hover"})
        grandchild_node_4 = LeafNode("span", "grandchild-4", {"style": "color:blue;text-align:center;"})
        grandchildren = [grandchild_node_1, grandchild_node_2, grandchild_node_3, grandchild_node_4]
        child_node = ParentNode("b", grandchildren)
        parent_node = ParentNode("div", [child_node])
        self.assertEqual(
            parent_node.to_html(),
            '<div><b><span class="tech">grandchild-1</span><a href="https://yeah.no">grandchild-2</a><span class="hover">grandchild-3</span><span style="color:blue;text-align:center;">grandchild-4</span></b></div>')

    def test_to_html_list_argument(self):
        child_node1 = [LeafNode("span", "Child", {"href": "https://test.com", "target": "_blank"})]
        parent_node1 = ParentNode("div", [child_node1])
        parent_node2 = ParentNode("div", child_node1)
        self.assertEqual(parent_node1.to_html(), parent_node2.to_html())

    def test_to_html_list_argument2(self):
        child_node1 = [LeafNode("span", "Child", {"href": "https://test.com", "target": "_blank"})]
        child_node2 = LeafNode("span", "Child", {"href": "https://test.com", "target": "_blank"})
        parent_node1 = ParentNode("div", [child_node1])
        parent_node2 = ParentNode("div", [child_node2])
        self.assertEqual(parent_node1.to_html(), parent_node2.to_html())

    def test_to_html_nest_list(self):
        grandchild_node_1 = LeafNode("span", "grandchild-1", {"class": "tech"})
        grandchild_node_2 = LeafNode("a", "grandchild-2", {"href": "https://yeah.no"})
        grandchild_node_3 = LeafNode("span", "grandchild-3", {"class": "hover"})
        grandchild_node_4 = LeafNode("span", "grandchild-4", {"style": "color:blue;text-align:center;"})
        grandchildren = [grandchild_node_1, grandchild_node_2, grandchild_node_3]
        child_node = ParentNode("p", [grandchildren, grandchild_node_4])
        parent_node = ParentNode("div", [child_node])
        self.assertEqual(
            parent_node.to_html(),
            '<div><p><span class="tech">grandchild-1</span><a href="https://yeah.no">grandchild-2</a><span class="hover">grandchild-3</span><span style="color:blue;text-align:center;">grandchild-4</span></p></div>'
            )

    def test_to_html_lots_of_nesting(self):
        descendant = LeafNode("b", "Bold text")
        descendant_wrapper = LeafNode(None, " before plain text.")
        greatgrandchild_1 = ParentNode("p", [descendant, descendant_wrapper])
        greatgrandchild_2 = LeafNode("p", "Another paragraph")
        grandchild_3 = ParentNode("h1", [greatgrandchild_1, greatgrandchild_2])
        child_2 = ParentNode("div", [grandchild_3], {"class": "main"})
        grandchild_1 = LeafNode("h1", "title")
        grandchild_2 = LeafNode("h2", "subtitle")
        child_1 = ParentNode("header", [grandchild_1, grandchild_2])
        parent = ParentNode("body", [child_1, child_2])
        self.assertEqual(
            parent.to_html(),
            '<body><header><h1>title</h1><h2>subtitle</h2></header><div class="main"><h1><p><b>Bold text</b> before plain text.</p><p>Another paragraph</p></h1></div></body>'
        )

    def test_to_html_value_error(self):
        child_node = LeafNode(None, None)
        parent_node = ParentNode("div", [child_node])
        with self.assertRaises(ValueError):
            parent_node.to_html()

if __name__ == "__main__":
    unittest.main()