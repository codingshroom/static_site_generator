import unittest
from textnode import TextNode, TextType
from splitters import split_nodes_link


class TestLinkSplit(unittest.TestCase):
    def test_split_nodes_link(self):
        node = TextNode(
            "This is text with a [link](https://i.imgur.com/zjjcJKZ.png) and another [second link](https://i.imgur.com/3elNhQu.png)",
            TextType.TEXT
        )
        new_nodes = split_nodes_link([node])
        self.assertListEqual(
            [
                TextNode("This is text with a ", TextType.TEXT),
                TextNode("link", TextType.LINK, "https://i.imgur.com/zjjcJKZ.png"),
                TextNode(" and another ", TextType.TEXT),
                TextNode(
                    "second link", TextType.LINK, "https://i.imgur.com/3elNhQu.png"
                )
            ],
            new_nodes,
        )

    def test_no_node(self):
        new_nodes = split_nodes_link([])
        self.assertListEqual([],new_nodes,)

    def test_one_link(self):
        node = TextNode(
            "This is text with a [link](https://i.imgur.com/zjjcJKZ.png)",
            TextType.TEXT
        )
        new_nodes = split_nodes_link([node])
        self.assertListEqual(
            [
                TextNode("This is text with a ", TextType.TEXT),
                TextNode("link", TextType.LINK, "https://i.imgur.com/zjjcJKZ.png")
            ],
            new_nodes,
        )
    
    def test_no_link(self):
        node = TextNode("hi, my fire", TextType.TEXT)
        new_nodes = split_nodes_link([node])
        self.assertListEqual([TextNode("hi, my fire", TextType.TEXT)], new_nodes)
    
    def test_two_nodes_two_links(self):
        node = TextNode(
            "This is text with a [link](https://i.imgur.com/zjjcJKZ.png) and another ",
            TextType.TEXT
        )
        node_2 = TextNode(
                    "second link", TextType.LINK, "https://i.imgur.com/3elNhQu.png"
                )
        new_nodes = split_nodes_link([node, node_2])
        self.assertListEqual(
            [
                TextNode("This is text with a ", TextType.TEXT),
                TextNode("link", TextType.LINK, "https://i.imgur.com/zjjcJKZ.png"),
                TextNode(" and another ", TextType.TEXT),
                TextNode(
                    "second link", TextType.LINK, "https://i.imgur.com/3elNhQu.png"
                )
            ],
            new_nodes,
        )
        
    def test_two_nodes_one_link(self):
        node = TextNode(
            "This is text with a [link](https://i.imgur.com/zjjcJKZ.png) and another ",
            TextType.TEXT
        )
        node_2 = TextNode("not", TextType.TEXT)
        new_nodes = split_nodes_link([node, node_2])
        self.assertListEqual(
            [
                TextNode("This is text with a ", TextType.TEXT),
                TextNode("link", TextType.LINK, "https://i.imgur.com/zjjcJKZ.png"),
                TextNode(" and another ", TextType.TEXT),
                TextNode("not", TextType.TEXT,)
            ],
            new_nodes,
        )

    def test_two_nodes_no_link(self):
        node = TextNode("nothing here",TextType.TEXT)
        node_2 = TextNode("my friend", TextType.TEXT)
        new_nodes = split_nodes_link([node, node_2])
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
        new_nodes = split_nodes_link([node, node_2])
        self.assertListEqual(
            [
                TextNode("image", TextType.IMAGE, "https://i.imgur.com/zjjcJKZ.png"),
                TextNode("link", TextType.LINK, "https://i.imgur.com/zjjcJKZ.png")
            ],
            new_nodes,
        )

    def test_only_link(self):
        node = TextNode(
            "[link](https://i.imgur.com/zjjcJKZ.png)",
            TextType.TEXT
        )
        new_nodes = split_nodes_link([node])
        self.assertListEqual(
            [
                TextNode("link", TextType.LINK, "https://i.imgur.com/zjjcJKZ.png")
            ],
            new_nodes,
        )


if __name__ == "__main__":
    unittest.main()
