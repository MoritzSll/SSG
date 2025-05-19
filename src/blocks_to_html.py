from markdown_blocks import markdown_to_blocks,block_to_block_type,BlockType
from htmlnode import *
from split_nodes import text_to_textnodes
from textnode import text_node_to_html_node

def markdown_to_html_node(markdown):
    blocks = markdown_to_blocks(markdown)
    parentNode = ParentNode("div",[],None)
    
    for block in blocks:
        blocktype = block_to_block_type(block)

        match blocktype:
            case BlockType.PARAGRAPH:
                parentNode.children.append(create_node(block,"p"))
            case BlockType.QUOTE:
                block = clean_quote_block_from_markdown(block)
                parentNode.children.append(create_node(block,"blockquote"))
            case BlockType.UNORDERED_LIST:
                block = clean_ul_block_from_markdown(block)
                parentNode.children.append(create_node(block,"ul"))
            case BlockType.ORDERED_LIST:
                block = clean_ol_block_from_markdown(block)
                parentNode.children.append(create_node(block,"ol"))
            case BlockType.CODE:
                parentNode.children.append(create_code_node(block))
            case BlockType.HEADING:
                heading_type = type_of_heading(block)
                block = clean_heading_block_from_markdown(block,heading_type)
                parentNode.children.append(create_node(block,f"h{heading_type}"))

    return parentNode   


def create_paragraph_node(markdown):
    parent_node = ParentNode("p",None,None)
    parent_node.children = text_to_children(markdown)
    return parent_node

def create_quote_node(markdown):
    parent_node = ParentNode("blockquote",None,None)
    parent_node.children = text_to_children(markdown)
    return parent_node

def create_node(markdown,tag):
    parentNode = ParentNode(tag,None,None)
    parentNode.children = text_to_children(markdown)
    return parentNode

def create_code_node(markdown):
    code_node = ParentNode("code",[],None)
    parentNode = ParentNode("pre",[code_node],None)
    cleaned_markdown = markdown.strip("```")
    code_node.children.append(LeafNode(None,cleaned_markdown,None))
    return parentNode

def text_to_children(text):
    nodes = text_to_textnodes(text)
    html_nodes = []
    for node in nodes:
        html_nodes.append(text_node_to_html_node(node))
    return html_nodes

def clean_quote_block_from_markdown(block):
    lines = block.split("\n")
    cleand_lines = [line[1:].strip() if line.startswith(">") else line for line in lines]
    block = "\n".join(cleand_lines)
    return block

def clean_ul_block_from_markdown(block):
    cleaned_lines = [line[1:].strip() if line.startswith("-") else line for line in block.split("\n")]
    cleaned_lines = ["<li>"+line+"</li>" for line in cleaned_lines]
    block = "\n".join(cleaned_lines)
    return block

def clean_ol_block_from_markdown(block):
    cleaned_lines = [line.lstrip(f"{i+1}. ").strip() for i,line in enumerate(block.split("\n"))]
    cleaned_lines = ["<li>"+line+"</li>" for line in cleaned_lines]
    block = "\n".join(cleaned_lines)
    return block

def type_of_heading(block):
    for i,char in enumerate(block):
        if char == "#":
            continue
        else:
            return i
        
def clean_heading_block_from_markdown(block,heading_type):
    return block[heading_type + 1:]
