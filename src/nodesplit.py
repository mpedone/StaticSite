from textnode import TextType, TextNode
from extract_links import extract_markdown_images, extract_markdown_links
from enum import Enum

class DelimType(Enum):
    TEXT = "text"
    BOLD = "**"
    ITALIC = "_"
    CODE = "`"
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
            if len(text_sections) != 2:
                raise ValueError("invalid markdown, image section not closed")
            if text_sections[0] != '':
                new_nodes.append(TextNode(text_sections[0], TextType.TEXT))
            new_nodes.append(TextNode(match[0], TextType.IMAGE, match[1]))
            node = TextNode(text_sections[1], TextType.TEXT)
        if node.text != '':
            new_nodes.append(node)
    return new_nodes

def split_nodes_link(old_nodes):
    new_nodes = []
    for node in old_nodes:
        matches = extract_markdown_links(node.text)
        for match in matches:
            text_sections = node.text.split(f"[{match[0]}]({match[1]})", 1)
            if len(text_sections) != 2:
                raise ValueError("invalid markdown, link section not closed")
            if text_sections[0] != '':
                new_nodes.append(TextNode(text_sections[0], TextType.TEXT))
            new_nodes.append(TextNode(match[0], TextType.LINK, match[1]))
            node = TextNode(text_sections[1], TextType.TEXT)
        if node.text != '':
            new_nodes.append(node)
    return new_nodes

def text_to_textnodes(text):
    node = TextNode(text, TextType.TEXT)
    
    res = split_nodes_delimiter([node], "**", TextType.BOLD)
    node = res.pop()
    res2 = split_nodes_delimiter([node], "_", TextType.ITALIC)
    node = res2.pop()
    res3 = split_nodes_delimiter([node], "`", TextType.CODE)
    node = res3.pop()
    res4 = split_nodes_image([node])
    node = res4.pop()
    res5 = split_nodes_link([node])

    res.extend(res2)
    res.extend(res3)
    res.extend(res4)
    res.extend(res5)

    return res

""" text = "This is **text** with an _italic_ word and a `code block` and an ![obi wan image](https://i.imgur.com/fJRm4Vk.jpeg) and a [link](https://boot.dev)"
# node = TextNode(text, TextType.TEXT)
new_nodes = text_to_textnodes(text)
# new_nodes = split_nodes_link([node])
for node in new_nodes:
    print(node) """

