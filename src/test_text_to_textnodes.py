import unittest
from textnode import TextNode, TextType
from splitters import text_to_textnodes


class TestTextToTextNodes(unittest.TestCase):
    def test_all(self):
        text = "This is **text** with an _italic_ word and a `code block` and an ![obi wan image](https://i.imgur.com/fJRm4Vk.jpeg) and a [link](https://boot.dev)"
        self.assertListEqual(
            [
    TextNode("This is ", TextType.TEXT),
    TextNode("text", TextType.BOLD),
    TextNode(" with an ", TextType.TEXT),
    TextNode("italic", TextType.ITALIC),
    TextNode(" word and a ", TextType.TEXT),
    TextNode("code block", TextType.CODE),
    TextNode(" and an ", TextType.TEXT),
    TextNode("obi wan image", TextType.IMAGE, "https://i.imgur.com/fJRm4Vk.jpeg"),
    TextNode(" and a ", TextType.TEXT),
    TextNode("link", TextType.LINK, "https://boot.dev"),
], 
text_to_textnodes(text)
)


    def test_text_only(self):
        text = "This is"
        self.assertListEqual([TextNode("This is", TextType.TEXT)], text_to_textnodes(text))


    def test_no_text(self):
        text = "**text**_italic_`code block`![obi wan image](https://i.imgur.com/fJRm4Vk.jpeg)[link](https://boot.dev)"
        self.assertListEqual(
            [
    TextNode("text", TextType.BOLD),
    TextNode("italic", TextType.ITALIC),
    TextNode("code block", TextType.CODE),
    TextNode("obi wan image", TextType.IMAGE, "https://i.imgur.com/fJRm4Vk.jpeg"),
    TextNode("link", TextType.LINK, "https://boot.dev"),
], 
text_to_textnodes(text)
)


    def test_all(self):
        text = ""
        self.assertListEqual([], text_to_textnodes(text))



if __name__ == "__main__":
    unittest.main()

