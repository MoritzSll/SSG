from textnode import TextNode
from htmlnode import HTMLNode,LeafNode,ParentNode


def main():
    node = ParentNode(
    "p",
    [
        LeafNode("b", "Bold text"),
        LeafNode(None, "Normal text"),
        ParentNode("i",[LeafNode("p", "Normal text"),LeafNode("b", "Bold text")]),
        LeafNode(None, "Normal text"),
    ],
)
    print(node.to_html())




main()


