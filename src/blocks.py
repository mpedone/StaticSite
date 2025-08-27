from enum import Enum, auto
import re

class BlockType(Enum):
    HEADING = auto()
    CODE = auto()
    QUOTE = auto()
    UNORDERED_LIST = auto()
    ORDERED_LIST = auto()
    PARAGRAPH = auto()

def markdown_to_blocks(markdown):
    block = []
    sections = markdown.split("\n\n")
    for section in sections:
        # print(f"section: {section}")
        # print(f"len(section): {len(section)}")
        if section != "" and section != "\n":
            block.append(section.strip("\n "))
    return block
    # return sections

def block_to_block_type(block):
    if re.match(r"#{1,6} .*[^\n]$", block):
        return BlockType.HEADING
    
    if re.match(r"`{3}.*\n*.*`{3}", block):
        return BlockType.CODE
    
    if re.match(r"^>", block):
        return BlockType.QUOTE

    unordered_list = re.findall(r"^- ", block, flags=re.M)
    block_length = len(block.split("\n"))
    if len(unordered_list) == block_length:
        return BlockType.UNORDERED_LIST
    
    list_items = block.split("\n")
    if len(re.findall(r"\d. ", block, flags=re.M)) == len(list_items):
        if list_items[0][0] != 1:
            return BlockType.PARAGRAPH
        for i in range(1, len(list_items) + 1):
            if list_items[i][0] != i:
                return BlockType.PARAGRAPH
        return BlockType.ORDERED_LIST
    
    return BlockType.PARAGRAPH

    

    """ tag = block[0]
    print(tag)
    match tag:
        case BlockType.HEADING.value:
            return(BlockType.HEADING)
        case BlockType.UNORDERED_LIST.value:
            return(BlockType.UNORDERED_LIST)
        case BlockType.CODE.value:
            return(BlockType.CODE)
        case _:
            return("Normal Paragraph") """

md = """# This is a heading

    This is a paragraph of text. It has some **bold** and _italic_ words inside of it.

## Heading 2


- This is the first list item in a list block
- This is a list item
- This is another list item

```This is a code block
with three lines
of code```

### Heading 3

- lk
sad

1. Numbered list item 1
2. numbered list item 2

> And a drop quote

1. bad ol
3. nbad ol

regulat

3. bad ol

Then the last line

"""

blocks = markdown_to_blocks(md)
i = 1
for block in blocks:
    # print(f"Block {i} (len: {len(block)}):\n{block}\n")
    # i += 1
    print(block_to_block_type(block))