import unittest
from textnode import TextNode, TextType, text_node_to_htmlnode



class TestTextNode(unittest.TestCase):
    def test_eq(self):
        node = TextNode("This is a text node", TextType.BOLD)
        node2 = TextNode("This is a text node", TextType.BOLD)
        self.assertEqual(node, node2)
    
    def test_eq_2(self):
        node = TextNode("", TextType.LINK, "https://www.wikipedia.org")
        node2 = TextNode("", TextType.LINK, "https://www.wikipedia.org")
        self.assertEqual(node, node2)
    
    def test_eq_3(self):
        node = TextNode("experiment", TextType.IMAGE, None)
        node2 = TextNode("experiment", TextType.IMAGE)
        self.assertEqual(node, node2)

    def test_uneq(self):
        node = TextNode("Hi", TextType.BOLD)
        node2 = TextNode("Hi", TextType.ITALIC)
        self.assertNotEqual(node, node2)
    
    def test_uneq_2(self):
        node = TextNode("x", TextType.TEXT)
        node2 = TextNode("x", TextType.TEXT, "https://www.boot.dev")
        self.assertNotEqual(node, node2)

    def test_uneq_3(self):
        node = TextNode("Hello my friend!", TextType.TEXT, "https://www.boot.dev")
        node2 = TextNode("Hello my fiend!", TextType.TEXT, "https://www.boot.dev")
        self.assertNotEqual(node, node2)

    def test_text(self):
        node = TextNode("This is a text node", TextType.TEXT)
        html_node = text_node_to_htmlnode(node)
        self.assertEqual(html_node.tag, None)
        self.assertEqual(html_node.value, "This is a text node")



if __name__ == "__main__":
    unittest.main()
