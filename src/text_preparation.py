
def strip_code_block(block):
    new_block = block.strip("```")
    if new_block.startswith("\n"):
        new_block = new_block.replace("\n", "", 1)
    return new_block


def strip_quote_block(block):
    lines = block.split("\n")
    new_lines = []
    for line in lines:
        new_lines.append(line.replace(">", ""))
    new_block = "\n".join(new_lines)
    return new_block


def strip_ulst_block(block):
    lines = block.split("\n")
    new_lines = []
    for line in lines:
        new_lines.append(line.replace("- ", ""))
    new_block = "\n".join(new_lines)
    return new_block


def strip_ordered_list(block):
    lines = block.split("\n")
    for i in range(len(lines)):
        lines[i].replace(f"{i + 1}. ", "")
    new_block = "\n".join(lines)
    return new_block


    


