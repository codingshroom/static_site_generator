import re
from textnode import TextNode, TextType



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


def split_nodes_delimiter(old_nodes, delimiter, text_type):
    new_nodes = []
    for node in old_nodes:
        if node.text_type != TextType.TEXT:
            new_nodes.append(node)
            continue
        parts_of_node = node.text.split(delimiter)
        if len(parts_of_node) % 2 == 0:
            raise Exception("invalid Markdown Syntax")
        for i in range(len(parts_of_node)):        
            if i % 2 == 0:
                new_node = TextNode(parts_of_node[i], TextType.TEXT)
            else:
                new_node = TextNode(parts_of_node[i], text_type)
            if new_node.text != "":
                new_nodes.append(new_node)
    return new_nodes


def split_nodes_link(old_nodes):
    new_nodes = []
    for node in old_nodes:
        if node.text_type != TextType.TEXT:
            new_nodes.append(node)
            continue
        extracted_links = extract_markdown_links(node.text)
        if not extracted_links:
            new_nodes.append(node)
            continue
        text_to_process = node.text
        for link_node in extracted_links:
            link_alt = link_node[0]
            link_link = link_node[1]
            sections = text_to_process.split(f"[{link_alt}]({link_link})", 1)
            if sections[0]:
                new_node = TextNode(sections[0], TextType.TEXT) 
                new_nodes.append(new_node)
            new_link_node = TextNode(link_alt, TextType.LINK, link_link)
            new_nodes.append(new_link_node)
            text_to_process = sections[1]
        if text_to_process:
            last_node = TextNode(text_to_process, TextType.TEXT)
            new_nodes.append(last_node)
    return new_nodes


def split_nodes_image(old_nodes):
    new_nodes = []
    for node in old_nodes:
        if node.text_type != TextType.TEXT:
            new_nodes.append(node)
            continue
        extracted_images = extract_markdown_images(node.text)
        if not extracted_images:
            new_nodes.append(node)
            continue
        text_to_process = node.text
        for image_node in extracted_images:
            image_alt = image_node[0]
            image_link = image_node[1]
            sections = text_to_process.split(f"![{image_alt}]({image_link})", 1)
            if sections[0]:
                new_node = TextNode(sections[0], TextType.TEXT) 
                new_nodes.append(new_node)
            new_image_node = TextNode(image_alt, TextType.IMAGE, image_link)
            new_nodes.append(new_image_node)
            text_to_process = sections[1]
        if text_to_process:
            last_node = TextNode(text_to_process, TextType.TEXT)
            new_nodes.append(last_node)
    return new_nodes


def extract_markdown_images(text):
    return re.findall(r"!\[([^\[\]]*)\]\(([^\(\)]*)\)", text)

def extract_markdown_links(text):
    return re.findall(r"(?<!!)\[([^\[\]]*)\]\(([^\(\)]*)\)", text)



if __name__ == "__main__":
    pass
