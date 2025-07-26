from textnode import TextNode, TextType
from main import extract_markdown_images, extract_markdown_links


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
