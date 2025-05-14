import sys

from textnode import TextNode, TextType


def main():
    x = TextNode("ciao", TextType.NORMAL)
    print(x)


if __name__ == "__main__":
    sys.exit(main())
