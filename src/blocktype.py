from enum import Enum


class BlockType(Enum):
    PARA = "paragraph"
    HEAD = "heading"
    CODE = "code"
    QUOT = "quote"
    ULST = "unordered_list"
    OLST = "ordered_list"


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
    
    