import unittest
from textnode import TextNode, TextType
from splitters import split_nodes_image


class TestImageSplit(unittest.TestCase):
    def test_split_nodes_images(self):
        node = TextNode(
            "This is text with an ![image](https://i.imgur.com/zjjcJKZ.png) and another ![second image](https://i.imgur.com/3elNhQu.png)",
            TextType.TEXT
        )
        new_nodes = split_nodes_image([node])
        self.assertListEqual(
            [
                TextNode("This is text with an ", TextType.TEXT),
                TextNode("image", TextType.IMAGE, "https://i.imgur.com/zjjcJKZ.png"),
                TextNode(" and another ", TextType.TEXT),
                TextNode(
                    "second image", TextType.IMAGE, "https://i.imgur.com/3elNhQu.png"
                )
            ],
            new_nodes,
        )

    def test_no_node(self):
        new_nodes = split_nodes_image([])
        self.assertListEqual([], new_nodes)

    def test_one_image(self):
        node = TextNode(
            "This is text with an ![image](https://i.imgur.com/zjjcJKZ.png)",
            TextType.TEXT
        )
        new_nodes = split_nodes_image([node])
        self.assertListEqual(
            [
                TextNode("This is text with an ", TextType.TEXT),
                TextNode("image", TextType.IMAGE, "https://i.imgur.com/zjjcJKZ.png")
            ],
            new_nodes,
        )

    def test_no_image(self):
        node = TextNode("hi, my fire", TextType.TEXT)
        new_nodes = split_nodes_image([node])
        self.assertListEqual([TextNode("hi, my fire", TextType.TEXT)], new_nodes)
    
    def test_two_nodes_two_images(self):
        node = TextNode(
            "This is text with an ![image](https://i.imgur.com/zjjcJKZ.png) and another ",
            TextType.TEXT
        )
        node_2 = TextNode(
                    "second image", TextType.IMAGE, "https://i.imgur.com/3elNhQu.png"
                )
        new_nodes = split_nodes_image([node, node_2])
        self.assertListEqual(
            [
                TextNode("This is text with an ", TextType.TEXT),
                TextNode("image", TextType.IMAGE, "https://i.imgur.com/zjjcJKZ.png"),
                TextNode(" and another ", TextType.TEXT),
                TextNode(
                    "second image", TextType.IMAGE, "https://i.imgur.com/3elNhQu.png"
                )
            ],
            new_nodes,
        )
        
    def test_two_nodes_one_image(self):
        node = TextNode(
            "This is text with an ![image](https://i.imgur.com/zjjcJKZ.png) and another ",
            TextType.TEXT
        )
        node_2 = TextNode("not", TextType.TEXT)
        new_nodes = split_nodes_image([node, node_2])
        self.assertListEqual(
            [
                TextNode("This is text with an ", TextType.TEXT),
                TextNode("image", TextType.IMAGE, "https://i.imgur.com/zjjcJKZ.png"),
                TextNode(" and another ", TextType.TEXT),
                TextNode("not", TextType.TEXT)
            ],
            new_nodes,
        )

    def test_two_nodes_no_image(self):
        node = TextNode("nothing here",TextType.TEXT)
        node_2 = TextNode("my friend", TextType.TEXT)
        new_nodes = split_nodes_image([node, node_2])
        self.assertListEqual(
            [
                TextNode("nothing here", TextType.TEXT),
                TextNode("my friend", TextType.TEXT)
            ],
            new_nodes,
        )

    def test_image_and_link_input_nodes(self):
        node = TextNode("image", TextType.IMAGE, "https://i.imgur.com/zjjcJKZ.png")
        node_2 = TextNode("link", TextType.LINK, "https://i.imgur.com/zjjcJKZ.png")
        new_nodes = split_nodes_image([node, node_2])
        self.assertListEqual(
            [
                TextNode("image", TextType.IMAGE, "https://i.imgur.com/zjjcJKZ.png"),
                TextNode("link", TextType.LINK, "https://i.imgur.com/zjjcJKZ.png")
            ],
            new_nodes,
        )

    def test_only_image(self):
        node = TextNode(
            "![image](https://i.imgur.com/zjjcJKZ.png)",
            TextType.TEXT
        )
        new_nodes = split_nodes_image([node])
        self.assertListEqual(
            [
                TextNode("image", TextType.IMAGE, "https://i.imgur.com/zjjcJKZ.png")
            ],
            new_nodes,
        )


if __name__ == "__main__":
    unittest.main()
