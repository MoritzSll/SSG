from textnode import TextNode
from htmlnode import HTMLNode,LeafNode


def main():
    node = LeafNode(None,"This is a paragraph of text.")
    print(node.to_html())


main()


