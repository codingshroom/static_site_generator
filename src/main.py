import re
from textnode import TextType
from htmlnode import LeafNode



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

def extract_markdown_images(text):
    return re.findall(r"!\[([^\[\]]*)\]\(([^\(\)]*)\)", text)

def extract_markdown_links(text):
    return re.findall(r"(?<!!)\[([^\[\]]*)\]\(([^\(\)]*)\)", text)



def main():
    print("nothing here yet")


if __name__ == "__main__":
    main()
