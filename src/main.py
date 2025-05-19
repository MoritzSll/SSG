from textnode import TextNode,TextType,text_node_to_html_node
from htmlnode import HTMLNode,LeafNode,ParentNode
from split_nodes import split_nodes_delimiter,split_nodes_link,text_to_textnodes,split_nodes_image
from markdown_blocks import is_heading_block
from blocks_to_html import markdown_to_html_node,create_paragraph_node,text_to_children



def main():
    
   md = """This is **bolded** paragraph
text in a p
tag here

This is another paragraph with _italic_ text and `code` here"""

   node = markdown_to_html_node(md)
   print(node.to_html())
   




main()


