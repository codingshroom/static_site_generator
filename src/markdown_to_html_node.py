from htmlnode import LeafNode, ParentNode
from textnode import text_node_to_htmlnode
from blocktype import BlockType, block_to_blocktype, blocktype_to_tag, markdown_to_block
from splitters import text_to_textnodes
from text_preparation import strip_code_block, strip_quote_block, strip_ulst_block



def markdown_to_html_node(markdown):
    master_node = ParentNode("div", [])
    blocks = markdown_to_block(markdown)
    for block in blocks:
        block_type = block_to_blocktype(block)
        tag = blocktype_to_tag(block_type)
        block_node = ParentNode(tag, [])
        if block_type == BlockType.CODE:
            stripped_block = strip_code_block(block)
            inner_node = LeafNode("code", stripped_block)
            block_node = ParentNode("pre", [inner_node])
        elif block_type == BlockType.QUOT:
            stripped_block = strip_quote_block(block)
            children = text_to_textnodes(stripped_block)
            block_node = ParentNode("quoteblock", [])
            for child in children:
                html_child = text_node_to_htmlnode(child)
                block_node.children.append(html_child)
        elif block_type == BlockType.ULST:
            stripped_block = strip_ulst_block(block)
            children = text_to_textnodes(stripped_block)
            block_node = ParentNode("ul", [])
            for child in children:
                html_child = text_node_to_htmlnode(child)
                block_node.children.append(html_child)
        else:
            textnodes = text_to_textnodes(block)
            for text_node in textnodes:
                html_node = text_node_to_htmlnode(text_node)
                block_node.children.append(html_node)
        master_node.children.append(block_node)
    return master_node



if __name__ == "__main__":
    pass
