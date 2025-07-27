import unittest
from split_delimiter import split_nodes_delimiter
from textnode import TextNode, TextType


class TestSplitDelimiter(unittest.TestCase):
    def test_code(self):
        node = TextNode("hi`return`friend", TextType.TEXT)
        lst = split_nodes_delimiter([node], "`", TextType.CODE)
        self.assertEqual(str(lst), "[TextNode(hi, text, None), TextNode(return, code, None), TextNode(friend, text, None)]")
        
    def test_bold_italic(self):
        node = TextNode("a **big** word", TextType.TEXT)
        node_2 = TextNode("_great_ stuff", TextType.TEXT)
        first = split_nodes_delimiter([node, node_2], "**", TextType.BOLD)
        lst = split_nodes_delimiter(first, "_", TextType.ITALIC)
        self.assertEqual(str(lst), "[TextNode(a , text, None), TextNode(big, bold, None), TextNode( word, text, None), TextNode(great, italic, None), TextNode( stuff, text, None)]")
    
    def test_one_word(self):
        node = TextNode("**ass**", TextType.TEXT)
        lst = split_nodes_delimiter([node], "**", TextType.BOLD)
        self.assertEqual(str(lst), "[TextNode(ass, bold, None)]")

    def test_comma(self):
        node = TextNode("what _are_ we, today?", TextType.TEXT)
        lst = split_nodes_delimiter([node], "_", TextType.ITALIC)
        self.assertEqual(str(lst), "[TextNode(what , text, None), TextNode(are, italic, None), TextNode( we, today?, text, None)]")

    def test_given_code(self):
        node = TextNode("return _True_", TextType.CODE)
        node_2 = TextNode("lorem", TextType.TEXT)
        node_3 = TextNode("giving _in_", TextType.TEXT)
        lst = split_nodes_delimiter([node, node_2, node_3], "_", TextType.ITALIC)
        self.assertEqual(str(lst), "[TextNode(return _True_, code, None), TextNode(lorem, text, None), TextNode(giving , text, None), TextNode(in, italic, None)]")
        
    def test_given_bold(self):
        node = TextNode("return **True**", TextType.BOLD)
        node_2 = TextNode("lorem", TextType.TEXT)
        lst = split_nodes_delimiter([node, node_2], "**", TextType.BOLD)
        self.assertEqual(str(lst), "[TextNode(return **True**, bold, None), TextNode(lorem, text, None)]")

    def test_given_italic(self):
        node = TextNode("return _True_", TextType.ITALIC)
        node_2 = TextNode("lorem", TextType.TEXT)
        lst = split_nodes_delimiter([node, node_2], "_", TextType.BOLD)
        self.assertEqual(str(lst), "[TextNode(return _True_, italic, None), TextNode(lorem, text, None)]")

    def test_empty_string(self):
        node = TextNode("", TextType.TEXT)
        lst = split_nodes_delimiter([node], "**", TextType.BOLD)
        self.assertEqual(str(lst), "[]")
    
    def test_unbalance_delimiters(self):
        node = TextNode("_wrong", TextType.TEXT)
        with self.assertRaises(Exception) as cm:
            split_nodes_delimiter([node], "_", TextType.ITALIC)
        self.assertEqual(str(cm.exception), "invalid Markdown Syntax")
    
    def test_no_delimiter(self):
        node = TextNode("plain text", TextType.TEXT)
        lst = split_nodes_delimiter([node], "**", TextType.BOLD)
        self.assertEqual(str(lst), "[TextNode(plain text, text, None)]")



if __name__ == "__main__":
    unittest.main()
