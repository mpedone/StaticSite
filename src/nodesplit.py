from textnode import TextType, TextNode
from extract_links import extract_markdown_images, extract_markdown_links
from enum import Enum

class DelimType(Enum):
    TEXT = "text"
    BOLD = "**"
    ITALIC = "_"
    CODE = "'"
    LINK = "!["
    IMAGE = "["

def split_nodes_delimiter(old_nodes, delimiter, text_type):
    new_nodes = []
    for node in old_nodes:
        if node.text_type != TextType.TEXT:
            new_nodes.append(node)
            continue
        split_nodes = []
        sections = node.text.split(delimiter)
        if len(sections) % 2 == 0:
            raise Exception("Invalid markdown, formatted section not closed")
        for i in range(len(sections)):
            if sections[i] == "":
                continue
            if i % 2 == 0:
                split_nodes.append(TextNode(sections[i], TextType.TEXT))
            else:
                split_nodes.append(TextNode(sections[i], text_type))
        new_nodes.extend(split_nodes)
        return new_nodes

def split_nodes_image(old_nodes):
    new_nodes = []
    for node in old_nodes:
        matches = extract_markdown_images(node.text)
        for match in matches:
            text_sections = node.text.split(f"![{match[0]}]({match[1]})", 1)
            new_nodes.append(TextNode(text_sections[0], TextType.TEXT))
            new_nodes.append(TextNode(match[0], TextType.IMAGE, match[1]))
            node = TextNode(text_sections[1], TextType.TEXT)
        if node.text != '':
            new_nodes.append(node)
    return new_nodes

def split_nodes_link(old_nodes):
    new_nodes = []
    for node in old_nodes:
        matches = extract_markdown_images(node.text)
        for match in matches:
            text_sections = node.text.split(f"[{match[0]}]({match[1]})", 1)
            new_nodes.append(TextNode(text_sections[0], TextType.TEXT))
            new_nodes.append(TextNode(match[0], TextType.LINK, match[1]))
            node = TextNode(text_sections[1], TextType.TEXT)
        if node.text != '':
            new_nodes.append(node)
    return new_nodes

node = TextNode(
    "This is text with a link (https://www.boot.dev) and [to youtube](https://www.youtube.com/@bootdotdev)",
    TextType.TEXT,
)

res = split_nodes_link([node])
for item in res:
    print(item)



