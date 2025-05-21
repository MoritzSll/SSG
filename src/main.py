from textnode import TextNode,TextType,text_node_to_html_node
from htmlnode import HTMLNode,LeafNode,ParentNode
from split_nodes import split_nodes_delimiter,split_nodes_link,text_to_textnodes,split_nodes_image
from markdown_blocks import is_heading_block
from blocks_to_html import markdown_to_html_node,create_paragraph_node,text_to_children
from copy_static import copy_static_into_public


def main():
   
   copy_static_into_public("static")

main()


