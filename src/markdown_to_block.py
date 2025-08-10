
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



if __name__ == "__main__":
    pass
