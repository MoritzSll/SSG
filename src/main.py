from textnode import TextNode,TextType,text_node_to_html_node
from htmlnode import HTMLNode,LeafNode,ParentNode
from split_nodes import split_nodes_delimiter,split_nodes_link,text_to_textnodes,split_nodes_image
from markdown_blocks import is_heading_block



def main():
    
   markdown = "###### Heading 6"

   print(is_heading_block(markdown))




main()


