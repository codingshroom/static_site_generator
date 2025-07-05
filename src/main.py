from textnode import TextNode, TextType


def main():
    node = TextNode("hi", TextType.BOLD, "https://www.creatingevil.com")
    print(node)

if __name__ == "__main__":
    main()
