from markdown_to_block import markdown_to_block
from blocktype import BlockType, block_to_blocktype
from htmlnode import HTMLNode, LeafNode, ParentNode
from text_to_textnodes import text_to_textnodes
from main import text_node_to_htmlnode



def markdown_to_html_node(markdown):
    blocks = markdown_to_block(markdown)
    block_node_list = []
    for block in blocks:
        blocktype = block_to_blocktype(block)
        children_nodes = text_to_textnodes(block)
        html_children = []
        for child in children_nodes:
            html_child = text_node_to_htmlnode(child)
            html_children.append(html_child)
        block_node = ParentNode(blocktype, html_children)
        block_node_list.append(block_node)
    super_node = ParentNode("html", block_node_list) # not sure about tag: html, body, something else?!?!
    return super_node

