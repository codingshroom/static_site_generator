import unittest
from blocktype import BlockType, block_to_blocktype


class TestBlockToBlockType(unittest.TestCase):
    def test_no_content(self):
        block_enum = block_to_blocktype("")
        self.assertEqual(BlockType.PARA, block_enum)


    def test_multi_line_content(self):
        block_enum = block_to_blocktype("normal text\nheight\nelement")
        self.assertEqual(BlockType.PARA, block_enum)


    def test_headings(self):
        block_enum = block_to_blocktype("### wireframe\ngoodness gracious")
        self.assertEqual(BlockType.PARA, block_enum)


    def test_hashtags(self):
        for i in range(1, 7):
            block_enum = block_to_blocktype("#" * i + " element of crime")
            self.assertEqual(BlockType.HEAD, block_enum)


    def test_multi_headings(self):
        block_enum = block_to_blocktype("## genius\n# wants\n##### food")
        self.assertEqual(BlockType.PARA, block_enum)
        

    def test_seven_hashtags(self):
        block_enum = block_to_blocktype("####### element of crime")
        self.assertEqual(BlockType.PARA, block_enum)


    def test_hashtags_no_space(self):
        for i in range(1, 7):
            block_enum = block_to_blocktype("#" * i + "element of crime")
            self.assertEqual(BlockType.PARA, block_enum)


    def test_correct_backticks(self):
        block_enum = block_to_blocktype("```if genius:\n stop work```")
        self.assertEqual(BlockType.CODE, block_enum)


    def test_correct_backticks_own_line(self):
        block_enum = block_to_blocktype("```\nif genius:\n stop work\nelse:\nhustle\n```")
        self.assertEqual(BlockType.CODE, block_enum)


    def test_incorrect_backticks(self):
        block_enum = block_to_blocktype("```if genius: stop work``")
        self.assertEqual(BlockType.PARA, block_enum)


    def test_incorrect_backticks_two(self):
        block_enum = block_to_blocktype("`if genius: stop work```")
        self.assertEqual(BlockType.PARA, block_enum)


    def test_incorrect_backticks_three(self):
        block_enum = block_to_blocktype("``genius: stop work``")
        self.assertEqual(BlockType.PARA, block_enum)


    def test_quote(self):
        block_enum = block_to_blocktype("> quote")
        self.assertEqual(BlockType.QUOT, block_enum)


    def test_quotes(self):
        block_enum = block_to_blocktype("> hi\n> friend\n> we are good")
        self.assertEqual(BlockType.QUOT, block_enum)


    def test_quotes_two(self):
        block_enum = block_to_blocktype("> hi\n friend\n> we are good")
        self.assertEqual(BlockType.PARA, block_enum)


    def test_unordered_list(self):
        block_enum = block_to_blocktype("- hi\n- friend\n- we are good")
        self.assertEqual(BlockType.ULST, block_enum)


    def test_unordered_list_two(self):
        block_enum = block_to_blocktype("- hi\n-friend\n- we are good")
        self.assertEqual(BlockType.PARA, block_enum)


    def test_ordered_list(self):
        block_enum = block_to_blocktype("1. hi\n2. friend\n3. we are good")
        self.assertEqual(BlockType.OLST, block_enum)


    def test_ordered_list_two(self):
        block_enum = block_to_blocktype("2. hi\n1. friend\n3. we are good")
        self.assertEqual(BlockType.PARA, block_enum)


    def test_ordered_list_three(self):
        block_enum = block_to_blocktype("1. friend\n3. we are good")
        self.assertEqual(BlockType.PARA, block_enum)


    def test_ordered_list_four(self):
        block_enum = block_to_blocktype("1. hi\n2.friend\n3. we are good")
        self.assertEqual(BlockType.PARA, block_enum)

 
    def test_ordered_list_five(self):
        block_enum = block_to_blocktype("1. hi\n2 friend\n3. we are good")
        self.assertEqual(BlockType.PARA, block_enum)


    def test_unordered_list_item(self):
        block_enum = block_to_blocktype("- hi")
        self.assertEqual(BlockType.ULST, block_enum)


    def test_ordered_list_item(self):
        block_enum = block_to_blocktype("1. scenius")
        self.assertEqual(BlockType.OLST, block_enum)


    def test_ordered_list_wrong_start(self):
        block_enum = block_to_blocktype("2. scenius\n3. scene\n4. genius")
        self.assertEqual(BlockType.PARA, block_enum)


    def test_unordered_list_space_break(self):
        block_enum = block_to_blocktype("- hi\n - avater\n- aang")
        self.assertEqual(BlockType.PARA, block_enum)


    def test_ordered_list_empty_line(self):
        block_enum = block_to_blocktype("1. scenius\n2. scene\n\n3. genius")
        self.assertEqual(BlockType.PARA, block_enum)


    def test_unordered_list_empty_line(self):
        block_enum = block_to_blocktype("- hi\n\n- aang")
        self.assertEqual(BlockType.PARA, block_enum)



if __name__ == "__main__":
    unittest.main()
