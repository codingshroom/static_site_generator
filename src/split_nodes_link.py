from textnode import TextNode, TextType
from main import extract_markdown_links


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
