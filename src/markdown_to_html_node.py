from blocks import markdown_to_blocks, block_to_block_type, BlockType
from htmlnode import HTMLnode

def markdown_to_html_node(markdown):
    blocks = markdown_to_blocks(markdown)
    for block in blocks:
        block_type = block_to_block_type(block)
        node = HTMLnode(block_type.value, block)
    return node

md = "test"
print(markdown_to_html_node(md))