import unittest

from blocks import markdown_to_blocks, block_to_block_type, BlockType

class test_markdown_to_blocks(unittest.TestCase):

        def test_markdown_to_blocks(self):
            md = """
This is **bolded** paragraph

This is another paragraph with _italic_ text and `code` here
This is the same paragraph on a new line

- This is a list
- with items
"""
            blocks = markdown_to_blocks(md)
            self.assertEqual(
                blocks,
                [
                    "This is **bolded** paragraph",
                    "This is another paragraph with _italic_ text and `code` here\nThis is the same paragraph on a new line",
                    "- This is a list\n- with items",
                ],
            )
        
        def test_markdown_to_blocks_whitespace(self):
            md = """
  This is a **bolded** paragraph

    This is another paragraph with _italic_ text and `code` here
This is the same paragraph on a new line

- This is a list
- with items   
"""
            blocks = markdown_to_blocks(md)
            self.assertEqual(
                blocks,
                [
                    "This is a **bolded** paragraph",
                    "This is another paragraph with _italic_ text and `code` here\nThis is the same paragraph on a new line",
                    "- This is a list\n- with items",
                ],
            )

        def test_markdown_to_blocks_newlines(self):
            md = """
This is a **bolded** paragraph



This is another paragraph with _italic_ text and `code` here
This is the same paragraph on a new line



- This is a list
- with items


"""
            blocks = markdown_to_blocks(md)
            self.assertEqual(
                blocks,
                [
                    "This is a **bolded** paragraph",
                    "This is another paragraph with _italic_ text and `code` here\nThis is the same paragraph on a new line",
                    "- This is a list\n- with items",
                ],
            )

        def test_markdown_to_blocks_newlines_and_whitespace(self):
            md = """

   This is a **bolded** paragraph  



    This is another paragraph with _italic_ text and `code` here
This is the same paragraph on a new line



    - This is a list
- with items


"""
            blocks = markdown_to_blocks(md)
            self.assertEqual(
                blocks,
                [
                    "This is a **bolded** paragraph",
                    "This is another paragraph with _italic_ text and `code` here\nThis is the same paragraph on a new line",
                    "- This is a list\n- with items",
                ],
            )

        def test_block_to_block_type(self):
            block_types = []
            text = """# Header 1

Normal paragraph

## Header 2

Normal paragraph

- ordered list 1
- ordered list 2

Paragraph

```code block```

paragraph

```code block
with
multiple
lines```

Paragraph

## Heading 2

Paragraph

1. OL
2. OL
3. OL
4. OL
5. OL
6. OL

> quote

### Heading 3"""
            blocks = markdown_to_blocks(text)
            for block in blocks:
                 block_types.append(block_to_block_type(block).name)
            self.assertListEqual(block_types, ['HEADING', 'PARAGRAPH', 'HEADING', 'PARAGRAPH', 'UNORDERED_LIST', 'PARAGRAPH', 'CODE', 'PARAGRAPH', 'CODE', 'PARAGRAPH', 'HEADING', 'PARAGRAPH', 'ORDERED_LIST', 'QUOTE', 'HEADING'])

        def test_headers(self):
            block_types = []
            text = "# H1\n\n## H2\n\n### H3\n\n#### H4\n\n##### H5\n\n###### H6\n\n####### H7"
            blocks = markdown_to_blocks(text)
            for block in blocks:
                block_types.append(block_to_block_type(block).name)
            self.assertListEqual(block_types, ['HEADING', 'HEADING', 'HEADING', 'HEADING', 'HEADING','HEADING', 'PARAGRAPH'])
        
        def test_bad_code(self):
            text = "```blah"
            block_type = block_to_block_type(text)
            self.assertEqual(block_type, BlockType.PARAGRAPH)

        def test_bad_ul(self):
            block_types = []
            text = "* one\n* two\n*three\n\n- one\ntwo\n- three\n\n"
            blocks = markdown_to_blocks(text)
            for block in blocks:
                block_types.append(block_to_block_type(block).name)
            self.assertListEqual(block_types, ["PARAGRAPH", "PARAGRAPH"])

        def test_bad_ol(self):
            block_types = []
            text = "1. a\n3. b\n4. c\n\n2. a\n3. b\n4. c\n\n1. a\nb\nc\n\n1. a\n2. v\n1. 3"
            blocks = markdown_to_blocks(text)
            for block in blocks:
                block_types.append(block_to_block_type(block))
            self.assertListEqual(block_types, [BlockType["PARAGRAPH"]] * len(block_types))
        
        def test_block_quote(self):
            block = ">text\ntext\ntext"
            block_type = block_to_block_type(block)
            self.assertEqual(block_type, BlockType.QUOTE)
        
        def test_mixed(self):
            block_types = []
            text = """# This is a heading

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
            blocks = markdown_to_blocks(text)
            for block in blocks:
                block_types.append(block_to_block_type(block))
            actual = [
                    BlockType["HEADING"], 
                    BlockType["PARAGRAPH"], 
                    BlockType["HEADING"], 
                    BlockType["UNORDERED_LIST"], 
                    BlockType["CODE"], 
                    BlockType["HEADING"],
                    BlockType["PARAGRAPH"], 
                    BlockType["ORDERED_LIST"],
                    BlockType["QUOTE"],
                    BlockType["PARAGRAPH"],
                    BlockType["PARAGRAPH"], 
                    BlockType["PARAGRAPH"],
                    BlockType["PARAGRAPH"]
                ]
            self.assertListEqual(block_types, actual)


if __name__ == "__main__":
    unittest.main()