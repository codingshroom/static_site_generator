from blocktype import markdown_to_block


def extract_title(markdown):
    blocks = markdown_to_block(markdown)
    header = None
    for block in blocks:
        if block.startswith("# "):
            header = block[2:].strip()
            break
    if not header:
        raise Exception("no h1 header found")
    return header 



if __name__ == "__main__":
    pass
