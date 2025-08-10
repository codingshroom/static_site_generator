import unittest
from markdown_to_block import markdown_to_block



class TestMarkdownToBlock(unittest.TestCase):
    def test_markdown_to_blocks(self):
        md = """
This is **bolded** paragraph

This is another paragraph with _italic_ text and `code` here
This is the same paragraph on a new line

- This is a list
- with items
"""
        blocks = markdown_to_block(md)
        self.assertEqual(
            blocks,
            [
                "This is **bolded** paragraph",
                "This is another paragraph with _italic_ text and `code` here\nThis is the same paragraph on a new line",
                "- This is a list\n- with items",
            ],
        )


    def test_empty_string(self):
        blocks = markdown_to_block("")
        self.assertEqual(blocks, [])


    def test_one_block(self):
        blocks = markdown_to_block("hi, my fire")
        self.assertEqual(blocks, ["hi, my fire"])


    def test_empty_blocks_in_between(self):
        md = """
        


This is **bolded** paragraph

    

This is another paragraph with _italic_ text and `code` here
This is the same paragraph on a new line



"""
        blocks = markdown_to_block(md)
        self.assertEqual(
            blocks,
            [
                "This is **bolded** paragraph",
                "This is another paragraph with _italic_ text and `code` here\nThis is the same paragraph on a new line",
            ],
        )


    def test_whitespace(self):
        blocks = markdown_to_block("""


"""
        )
        self.assertEqual(blocks, [])
    

    def test_starting_newline(self):
        md = """
    lord of the rings
"""
        blocks = markdown_to_block(md)
        self.assertEqual(blocks, ["lord of the rings"])
        




if __name__ == "__main__":
    unittest.main()
