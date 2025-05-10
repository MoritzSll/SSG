from textnode import TextNode,TextType
from htmlnode import HTMLNode,LeafNode,ParentNode
from split_nodes import split_nodes_delimiter


def main():
    
    node = TextNode("This text with a _code block_ word", TextType.TEXT)
    print(split_nodes_delimiter([node], "_", TextType.ITALIC))




main()


