from enum import Enum


class BlockType(Enum):
    PARA = "paragraph"
    HEAD = "heading"
    CODE = "code"
    QUOT = "quote"
    ULST = "unordered_list"
    OLST = "ordered_list"


def markdown_to_block(markdown):
    markdown = markdown.strip("\n\t ")
    if not markdown:
        return []
    block_list = []
    blocks = markdown.split("\n\n")
    for block in blocks:
        block = block.strip("\n\t ")
        if not block:
            continue
        block_list.append(block)
    return block_list


def block_to_blocktype(block):
    lines = block.split("\n")
    if any(block.startswith('#' * (i + 1) + ' ') for i in range(6)) and len(lines) < 2:
        return BlockType.HEAD
    if block.startswith("```") and block.endswith("```"):
        return BlockType.CODE
    if all(line.startswith(">") for line in lines):
        return BlockType.QUOT
    if all(line.startswith("- ") for line in lines):
        return BlockType.ULST
    if all(lines[i].startswith(f"{i + 1}. ") for i in range(len(lines))):
        return BlockType.OLST
    else:
        return BlockType.PARA


def blocktype_to_tag(blocktype):
    if blocktype == BlockType.PARA:
        return "p"
    if blocktype == BlockType.HEAD:
        return "h"
    if blocktype == BlockType.CODE:
        return "code"
    if blocktype == BlockType.QUOT:
        return "quoteblock"
    if blocktype == BlockType.OLST:
        return "ol"
    if blocktype == BlockType.ULST:
        return "ul"



if __name__ == "__main__":
    pass
