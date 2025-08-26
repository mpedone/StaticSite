import unittest

from blocks import markdown_to_blocks

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


if __name__ == "__main__":
    unittest.main()