import unittest

from extract_links import extract_markdown_images, extract_markdown_links
from nodesplit import split_nodes_link, split_nodes_image, text_to_textnodes
from textnode import TextNode, TextType
""" 
class test_extract_funcs(unittest.TestCase):
    def test_one(self):
        matches = extract_markdown_images("This is text with a ![rick roll](https://i.imgur.com/aKaOqIh.gif) and ![obi wan](https://i.imgur.com/fJRm4Vk.jpeg)")
        self.assertEqual([("rick roll", "https://i.imgur.com/aKaOqIh.gif"), ("obi wan", "https://i.imgur.com/fJRm4Vk.jpeg")], matches)
    
    def test_extract_markdown_images(self):
        matches = extract_markdown_images(
            "This is text with an ![image](https://i.imgur.com/zjjcJKZ.png)"
        )
        self.assertListEqual([("image", "https://i.imgur.com/zjjcJKZ.png")], matches)

    def test_extract_links(self):
        matches = extract_markdown_links("This is text with a link [to boot dev](https://www.boot.dev) and [to youtube](https://www.youtube.com/@bootdotdev)")
        self.assertListEqual([("to boot dev", "https://www.boot.dev"), ("to youtube", "https://www.youtube.com/@bootdotdev")], matches)
    
    def test_no_alt_text(self):
        matches = extract_markdown_images("This is bad markdown, just look at how grumpy grumpy cat is: (https://notarealcat.gif)")
        self.assertEqual([], matches)
    
    def test_no_image(self):
        matches = extract_markdown_images("Blah blah blah ![blah]")
        self.assertEqual([], matches)
    
    def test_http(self):
        matches = extract_markdown_images("This is text with a ![rick roll](http://i.imgur.com/aKaOqIh.gif) and ![obi wan](http://i.imgur.com/fJRm4Vk.jpeg)")
        self.assertEqual([("rick roll", "http://i.imgur.com/aKaOqIh.gif"), ("obi wan", "http://i.imgur.com/fJRm4Vk.jpeg")], matches)

    def test_http_link(self):
        matches = extract_markdown_links("This is a non-secure [website](http://gimme.com)")
        self.assertEqual([("website", "http://gimme.com")], matches)
    
    def test_non_standard(self):
        matches = extract_markdown_links("[file transfer](ftp://hereyougo.com) and [just the domain](sketchy.com)")
        self.assertEqual([("file transfer", "ftp://hereyougo.com"), ("just the domain", "sketchy.com")], matches)

class test_split_links(unittest.TestCase):
    def test_split_images(self):
        node = TextNode(
            "This is text with an ![image](https://i.imgur.com/zjjcJKZ.png) and another ![second image](https://i.imgur.com/3elNhQu.png)",
            TextType.TEXT,
        )
        new_nodes = split_nodes_image([node])
        self.assertListEqual(
            [
                TextNode("This is text with an ", TextType.TEXT),
                TextNode("image", TextType.IMAGE, "https://i.imgur.com/zjjcJKZ.png"),
                TextNode(" and another ", TextType.TEXT),
                TextNode(
                    "second image", TextType.IMAGE, "https://i.imgur.com/3elNhQu.png"
                ),
            ],
            new_nodes,
        )

    def test_split_images_2(self):
        node = TextNode(
            "This is text with an ![image](https://i.imgur.com/zjjcJKZ.png) and another ![second image](https://i.imgur.com/3elNhQu.png), but nothing else.",
            TextType.TEXT,
        )
        new_nodes = split_nodes_image([node])
        self.assertListEqual(
            [
                TextNode("This is text with an ", TextType.TEXT),
                TextNode("image", TextType.IMAGE, "https://i.imgur.com/zjjcJKZ.png"),
                TextNode(" and another ", TextType.TEXT),
                TextNode(
                    "second image", TextType.IMAGE, "https://i.imgur.com/3elNhQu.png"
                ),
                TextNode(", but nothing else.", TextType.TEXT),
            ],
            new_nodes,
        )

    def test_split_links(self):
        node = TextNode(
            "This is text with a link [to boot dev](https://www.boot.dev) and [to youtube](https://www.youtube.com/@bootdotdev)",
            TextType.TEXT,
        )
        new_nodes = split_nodes_link([node])
        self.assertListEqual(
            [
                TextNode("This is text with a link ", TextType.TEXT),
                TextNode("to boot dev", TextType.LINK, "https://www.boot.dev"),
                TextNode(" and ", TextType.TEXT),
                TextNode(
                    "to youtube", TextType.LINK, "https://www.youtube.com/@bootdotdev"
                ),
            ],
            new_nodes,
        )

    def test_split_links_2(self):
        node = TextNode(
            "This is text with a link [to boot dev](https://www.boot.dev) and [to youtube](https://www.youtube.com/@bootdotdev), but nothing else.",
            TextType.TEXT,
        )
        new_nodes = split_nodes_link([node])
        self.assertListEqual(
            [
                TextNode("This is text with a link ", TextType.TEXT),
                TextNode("to boot dev", TextType.LINK, "https://www.boot.dev"),
                TextNode(" and ", TextType.TEXT),
                TextNode(
                    "to youtube", TextType.LINK, "https://www.youtube.com/@bootdotdev"
                ),
                TextNode(", but nothing else.", TextType.TEXT),
            ],
            new_nodes,
        )
    
    def test_no_images(self):
        node = TextNode("Nothing to see here!", TextType.TEXT)
        new_nodes = split_nodes_image([node])
        self.assertListEqual([TextNode("Nothing to see here!", TextType.TEXT)], new_nodes)

    def test_no_links(self):
        node = TextNode("Nowhere to go!", TextType.TEXT)
        new_nodes = split_nodes_link([node])
        self.assertListEqual([TextNode("Nowhere to go!", TextType.TEXT)], new_nodes)
    
    def test_image_first(self):
        node = TextNode("![DropCapImage](https://i.imgur.com/zjjcJKZ.png)This line starts with an image.", TextType.TEXT)
        new_nodes = split_nodes_image([node])
        self.assertListEqual([
            TextNode("DropCapImage", TextType.IMAGE, "https://i.imgur.com/zjjcJKZ.png"),
            TextNode("This line starts with an image.", TextType.TEXT)
        ], new_nodes)

    def test_link_first(self):
        node = TextNode("[Click here](http://somelink.com) before reading the rest of this sentence.", TextType.TEXT)
        new_nodes = split_nodes_link([node])
        self.assertListEqual([
            TextNode("Click here", TextType.LINK, "http://somelink.com"),
            TextNode(" before reading the rest of this sentence.", TextType.TEXT)
        ], new_nodes)
 """
class test_split_node(unittest.TestCase):
    def test_one(self):
        text = "This is **text** with an _italic_ word and a `code block` and an ![obi wan image](https://i.imgur.com/fJRm4Vk.jpeg) and a [link](https://boot.dev)"
        new_nodes = text_to_textnodes(text)
        self.assertListEqual([
            TextNode("This is ", TextType.TEXT),
            TextNode("text", TextType.BOLD),
            TextNode(" with an ", TextType.TEXT),
            TextNode("italic", TextType.ITALIC),
            TextNode(" word and a ", TextType.TEXT),
            TextNode("code block", TextType.CODE),
            TextNode(" and an ", TextType.TEXT),
            TextNode("obi wan image", TextType.IMAGE, "https://i.imgur.com/fJRm4Vk.jpeg"),
            TextNode(" and a ", TextType.TEXT),
            TextNode("link", TextType.LINK, "https://boot.dev"),
        ], new_nodes)


if __name__ == "__main__":
    unittest.main()