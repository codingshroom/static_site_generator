from enum import Enum

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

