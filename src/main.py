from textnode import TextType, TextNode, text_node_to_html_node
from htmlnode import HTMLnode, LeafNode, ParentNode
from nodesplit import text_to_textnodes, DelimType
from blocks import markdown_to_blocks, block_to_block_type, BlockType
from enum import Enum


def main():
    test = "```This is a paragraph with a bold word and an italic word.```"

    try:
        block_type = block_to_block_type(test)
        code_block = TextNode(test, TextType.CODE)
        # html_node = text_node_to_html_node(code_block)
        # parent = ParentNode(block_type.value, [html_node])
        if block_type != BlockType.CODE:
            sub_blocks = text_to_textnodes(test)
            leaf_blocks = []
            for sub in sub_blocks:
                leaf_blocks.append(text_node_to_html_node(sub))
            html_node = ParentNode(block_type.value, leaf_blocks)
        node = text_node_to_html_node(code_block)
        html_node = ParentNode(block_type.value, [node])

        print(block_type.value)
        # print(parent.to_html())


    except Exception as e:
        print(e)


main()
