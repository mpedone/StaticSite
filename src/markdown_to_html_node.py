from blocks import markdown_to_blocks, block_to_block_type, BlockType
from htmlnode import HTMLnode, ParentNode
from nodesplit import text_to_textnodes
from textnode import text_node_to_html_node, TextNode, TextType
import re

def markdown_to_html_node(markdown):
    blocks = markdown_to_blocks(markdown)
    nodes = []
    for item in blocks:
        block_type = block_to_block_type(item)

        if block_type.value == "h":
            level = item.split(" ", 1)[0].count("#")
            tag = "h" + str(level)
        else:
            tag = block_type.value

        if block_type == BlockType.CODE:
            block = re.sub(r"`{3}", "", item)
            code_block = TextNode(block, TextType.CODE)
            html_node = text_node_to_html_node(code_block)
            parent = ParentNode(tag, [html_node])
            nodes.append(parent)
            continue
        else:
            block = block_to_html(item, block_type)
        
        children_nodes = text_to_children(block)
        node = ParentNode(tag, children_nodes)
        nodes.append(node)
    output = ParentNode("div", nodes)
    return output

def text_to_children(text):
    new_text = text_to_textnodes(text)
    new_nodes = []
    for x in new_text:
        new_nodes.append(text_node_to_html_node(x))
    # print(new_nodes)
    return new_nodes

def block_to_html(block, block_type):
    match block_type.value:
        case "h":
            return re.sub(r"#{1,6} ", "", block)
        case "ul":
            return re.sub(r"- (.*)", r"<li>\1</li>", block)
        case "ol":
            return re.sub(r"\d. (.*)", r"<li>\1</li>", block)
        case "blockquote":
            return re.sub(r"> ", "", block)
        case _:
            return block


# md = "# test\n\nHere's some **bold** text\n\n1. item\n2. itme\n3. ietm\n\n```code\nblock```"
md = """
This is **bolded** paragraph
text in a p

> tag here

This is another paragraph with _italic_ text and `code` here

"""

node = markdown_to_html_node(md)
# print(node.to_html())
