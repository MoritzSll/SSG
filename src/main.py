from textnode import TextNode,TextType
from htmlnode import HTMLNode,LeafNode,ParentNode
from split_nodes import split_nodes_delimiter,split_nodes_link,split_nodes_image


def main():
    
    node = TextNode(
            "This is text with an ![image](https://i.imgur.com/zjjcJKZ.png)![second image](https://i.imgur.com/3elNhQu.png)",
            TextType.TEXT,
        )
    print(split_nodes_image([node]))




main()


