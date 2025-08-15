
def strip_code_block(block):
    new_block = block.strip("```")
    while new_block.startswith(("\n", "\t", " ")):
        if new_block.startswith("\n"):
            new_block = new_block.replace("\n", "", 1)
        if new_block.startswith("\t"):
            new_block = new_block.replace("\t", "", 1)
        if new_block.startswith(" "):
            new_block = new_block.replace(" ", "", 1)
    return new_block


def strip_quote_block(block):
    lines = block.split("\n")
    new_lines = []
    for line in lines:
        new_lines.append(line[2:])
    new_block = "\n".join(new_lines)
    return new_block


def strip_list_block(block, start_index):
    lines = block.split("\n")
    new_lines = []
    for line in lines:
        new_lines.append(line[start_index:])
    return new_lines


def strip_header_block(block):
    num_hashtags = 0 
    while block.startswith("#"):
        block = block[1:]
        num_hashtags += 1
    new_block = block[1:]
    return new_block, num_hashtags



if __name__ == "__main__":
    pass
