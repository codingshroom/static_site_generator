from markdown_to_block import markdown_to_block
from blocktype import BlockType, block_to_blocktype
from htmlnode import HTMLNode, LeafNode, ParentNode
from text_to_textnodes import text_to_textnodes
from main import text_node_to_htmlnode



def markdown_to_html_node(markdown):
    master_node = ParentNode("html", [])
    blocks = markdown_to_block(markdown)
    for block in blocks:
        block_type = block_to_blocktype(block)
        block_node = ParentNode(block_type, [])
        if block_type == BlockType.CODE:
            block_node = LeafNode("code", block)
        else:
            textnodes = text_to_textnodes(block)
            for text_node in textnodes:
                html_node = text_node_to_htmlnode(text_node)
                block_node.children.append(html_node)
        master_node.children.append(block_node)
    return master_node



if __name__ == "__main__":
    pass
