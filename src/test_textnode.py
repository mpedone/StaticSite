import unittest
import main

from textnode import TextNode, TextType, text_node_to_html_node


class TestTextNode(unittest.TestCase):
    # pass
    def test_eq(self):
        node = TextNode("This is a text node", TextType.BOLD)
        node2 = TextNode("This is a text node", TextType.BOLD)
        self.assertEqual(node, node2)
    
    def test_text_not_eq(self):
        node = TextNode("This is a text node", TextType.BOLD)
        node2 = TextNode("This is another text node", TextType.BOLD)
        self.assertNotEqual(node, node2)

    def test_text_type_not_eq(self):
        node = TextNode("This is a text node", TextType.BOLD)
        node2 = TextNode("This is a text node", TextType.LINK)
        self.assertNotEqual(node, node2)

    def test_url_not_eq(self):
        node = TextNode("This is a text node", TextType.BOLD, "a.com")
        node2 = TextNode("This is a text node", TextType.BOLD, "b.com")
        self.assertNotEqual(node, node2)
    
    def test_url_default(self):
        node = TextNode("This is a text node", TextType.BOLD)
        self.assertIsNone(node.url)

    def test_url(self):
        node = TextNode("This is a text node", TextType.BOLD, "http://boot.dev")
        self.assertIsNotNone(node.url)
    
    def test_eq_method(self):
        node = TextNode("This is a text node", TextType.BOLD)
        node2 = TextNode("This is a text node", TextType.BOLD)
        equality = node == node2
        self.assertTrue(equality)

    def test_eq_false_method(self):
        node = TextNode("This is a text node", TextType.BOLD)
        node2 = TextNode("This is another text node", TextType.BOLD)
        equality = node == node2
        self.assertFalse(equality)

    def test_text(self):
        node = TextNode("This is a text node", TextType.TEXT)
        html_node = text_node_to_html_node(node)
        self.assertEqual(html_node.tag, None)
        self.assertEqual(html_node.value, "This is a text node")
    
    def test_text_bold(self):
        node = TextNode("This is a bold node", TextType.BOLD)
        html_node = text_node_to_html_node(node)
        self.assertEqual(html_node.tag, "b")
        self.assertEqual(html_node.value, "This is a bold node")

    def test_text_italic(self):
        node = TextNode("This is an italic node", TextType.ITALIC)
        html_node = text_node_to_html_node(node)
        self.assertEqual(html_node.tag, "i")
        self.assertEqual(html_node.value, "This is an italic node")

    def test_text_code(self):
        node = TextNode("This is a code node", TextType.CODE)
        html_node = text_node_to_html_node(node)
        self.assertEqual(html_node.tag, "code")
        self.assertEqual(html_node.value, "This is a code node")
    
    def test_text_link(self):
        node = TextNode("This is a link node", TextType.LINK, "https://test.com")
        html_node = text_node_to_html_node(node)
        self.assertEqual(html_node.tag, "a")
        self.assertEqual(html_node.value, "This is a link node")
        self.assertEqual(html_node.props, {"href": "https://test.com"})
        self.assertEqual(html_node.to_html(), '<a href="https://test.com">This is a link node</a>')
    
    def test_text_img(self):
        node = TextNode("This is an image node", TextType.IMAGE, "./images/image.png")
        html_node = text_node_to_html_node(node)
        self.assertEqual(html_node.tag, "img")
        self.assertEqual(html_node.value, "")
        self.assertEqual(html_node.props, {"src": "./images/image.png", "alt": "This is an image node"})
        self.assertEqual(html_node.to_html(), '<img src="./images/image.png" alt="This is an image node">')


if __name__ == "__main__":
    unittest.main()