from textnode import TextNode, TextType


def split_nodes_delimiter(old_nodes, delimiter, text_type):
    new_nodes = []
    for node in old_nodes:
        if node.text_type != TextType.TEXT:
            new_nodes.append(node)
            continue
        parts_of_node = node.text.split(delimiter)
        if len(parts_of_node) % 2 == 0:
            print(parts_of_node)
            raise Exception("invalid Markdown Syntax")
        for i in range(len(parts_of_node)):        
            if i % 2 == 0:
                new_node = TextNode(parts_of_node[i], TextType.TEXT)
            else:
                new_node = TextNode(parts_of_node[i], text_type)
            if new_node.text != "":
                new_nodes.append(new_node)
    return new_nodes
            


if __name__ == "__main__":
    pass
