from enum import Enum
from htmlnode import LeafNode



class TextType(Enum):
    TEXT = "text"
    BOLD = "bold"
    ITALIC = "italic"
    CODE = "code"
    LINK = "link"
    IMAGE = "image"


class TextNode:
    def __init__(self, text, text_type, url=None):
        self.text = text
        self.text_type = text_type 
        self.url = url

    def __eq__(self, other_node):
        one = self.text == other_node.text
        two = self.text_type == other_node.text_type
        three = self.url == other_node.url
        return all([one, two, three])

    def __repr__(self):
        return f"TextNode({self.text}, {self.text_type.value}, {self.url})"


def text_node_to_htmlnode(text_node):
    tag = text_node.text_type
    content = text_node.text
    link = text_node.url
    if tag == TextType.TEXT:
        return LeafNode(None, content)
    elif tag == TextType.BOLD:
        return LeafNode("b", content)
    elif tag == TextType.ITALIC:
        return LeafNode("i", content)
    elif tag == TextType.CODE:
        return LeafNode("code", content)
    elif tag == TextType.LINK:
        return LeafNode("a", content, {"href": link})
    elif tag == TextType.IMAGE:
        return LeafNode("img", "", {"src": link, "alt": content})
    else:
        raise Exception("TextType not found")



if __name__ == "__main__":
    pass
