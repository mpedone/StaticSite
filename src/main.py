from textnode import TextType, TextNode
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
    # node = test.to_html()   
    # print(node)

    try:
        child_node = LeafNode(None, None)
        # child_node = ["p", "childe"]
        parent_node = ParentNode("div", child_node)
        print(child_node.to_html())
        print(parent_node.to_html())


    except Exception as e:
        print(e)

main()
