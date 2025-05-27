from textnode import TextType, TextNode, text_node_to_html_node
from htmlnode import HTMLnode, LeafNode, ParentNode

def main():
    test = ParentNode(
        "p",
            [
                LeafNode("b", "Bold text"),
                LeafNode(None, "Normal text"),
                LeafNode("i", "italic text"),
                LeafNode(None, "Normal text"),
            ],
    )

    try:
        node = TextNode("test text", TextType.IMAGE, "https://test.com")
        print(node.url)
        print(text_node_to_html_node(node))
        leaf_node = text_node_to_html_node(node)
        print(leaf_node.to_html())


    except Exception as e:
        print(e)

            
main()
