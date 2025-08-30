from enum import Enum, auto
import re

class BlockType(Enum):
    HEADING = "h"
    CODE = "pre"
    QUOTE = "blockquote"
    UNORDERED_LIST = "ul"
    ORDERED_LIST = "ol"
    PARAGRAPH = "p"

def markdown_to_blocks(markdown):
    block = []
    sections = markdown.split("\n\n")
    for section in sections:
        if section != "" and section != "\n":
            block.append(section.strip("\n "))
        # if section != "":
        #     block.append(section.strip())
    return block

def block_to_block_type(block):
    if re.match(r"#{1,6} .*[^\n]$", block):
        return BlockType.HEADING
    
    if re.match(r"`{3}(.*\n*.*)*`{3}", block):
        return BlockType.CODE
    
    if re.match(r"^>", block):
        return BlockType.QUOTE

    unordered_list = re.findall(r"^- ", block, flags=re.M)
    block_length = len(block.split("\n"))
    if len(unordered_list) == block_length:
        return BlockType.UNORDERED_LIST
    
    list_items = block.split("\n")
    if len(re.findall(r"\d. ", block, flags=re.M)) == len(list_items):
        if list_items[0][0] != "1":
            return BlockType.PARAGRAPH
        for i in range(len(list_items)):
            if list_items[i][0] != str(i+1):
                return BlockType.PARAGRAPH
        return BlockType.ORDERED_LIST
    return BlockType.PARAGRAPH