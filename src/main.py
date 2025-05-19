from textnode import TextType, TextNode
from htmlnode import HTMLnode, LeafNode

def main():
    test = TextNode("test", TextType.LINK, "http://a.com")
    test2 = TextNode("test", TextType.LINK, "http://ba.com")
    # print(test)
    # print(test == test2)
    props = {"href": "https://test.com", "target": "_blank"}
    tag = None

    test3 = LeafNode(tag, "This is a paragraph of text.")
    # test4 = LeafNode("p", "This is a paragraph of text.").to_html()
    # test5 = LeafNode(tag, "This is a paragraph of text.").to_html()
    # print(test3)
    # print(test4)
    # print(test5)
    # test6 = HTMLnode("a", "http://test.com", "props", props=HTMLnode.props_to_html(props))
    # print(test6)
    # print(LeafNode.to_html(test3))
    node = LeafNode("a", "Click Here", {"href": "https://test.com", "target": "_blank"})
    print(node.to_html())
    print(node)

main()