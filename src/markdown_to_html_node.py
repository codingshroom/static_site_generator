from htmlnode import LeafNode, ParentNode
from textnode import text_node_to_htmlnode
from blocktype import BlockType, block_to_blocktype, blocktype_to_tag, markdown_to_block
from splitters import text_to_textnodes



def markdown_to_html_node(markdown):
    master_node = ParentNode("div", [])
    blocks = markdown_to_block(markdown)
    print(f"{blocks=}")
    for block in blocks:
        block_type = block_to_blocktype(block)
        tag = blocktype_to_tag(block_type)
        block_node = ParentNode(tag, [])
        if block_type == BlockType.CODE:
            inner_node = LeafNode("code", block)
            block_node = ParentNode("pre", [inner_node])
        else:
            textnodes = text_to_textnodes(block)
#            print(f"{textnodes=}")
            for text_node in textnodes:
                html_node = text_node_to_htmlnode(text_node)
                block_node.children.append(html_node)
        master_node.children.append(block_node)
    return master_node



if __name__ == "__main__":
    pass
