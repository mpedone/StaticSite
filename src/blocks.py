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

md = """# This is a heading

    This is a paragraph of text. It has some **bold** and _italic_ words inside of it.



- This is the first list item in a list block
- This is a list item
- This is another list item


"""

""" blocks = markdown_to_blocks(md)
i = 1
for block in blocks:
    print(f"Block {i} (len: {len(block)}):\n{block}\n")
    i += 1 """