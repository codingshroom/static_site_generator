from textnode import TextNode, TextType
from split_delimiter import split_nodes_delimiter
from split_nodes_link import split_nodes_link
from split_nodes_image import split_nodes_image


def text_to_textnodes(text):
    if not text:
        return []
    node = TextNode(text, TextType.TEXT)
    nodes = split_nodes_delimiter([node], "**", TextType.BOLD)
    nodes = split_nodes_delimiter(nodes, "_", TextType.ITALIC)
    nodes = split_nodes_delimiter(nodes, "`", TextType.CODE)
    nodes = split_nodes_image(nodes)
    nodes = split_nodes_link(nodes)
    return nodes



if __name__ == "__main__":
    pass
