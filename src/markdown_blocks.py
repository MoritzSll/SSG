import re
from enum import Enum


class BlockType(Enum):
    PARAGRAPH = "paragraph"
    HEADING = "heading"
    CODE = "code"
    QUOTE = "quote"
    UNORDERED_LIST = "unordered_list"
    ORDERED_LIST = "ordered_list"


def markdown_to_blocks(markdown):
    blocks = re.split(r"\n\s*\n", markdown)
    filtered_blocks = []
    for block in blocks:
        if block == "":
            continue
        block = block.strip()
        filtered_blocks.append(block)
    return filtered_blocks

def block_to_block_type(markdown):
    if is_heading_block(markdown):
        return BlockType.HEADING
    elif is_code_block(markdown):
        return BlockType.CODE
    elif is_quote_block(markdown):
        return BlockType.QUOTE
    elif is_unordered_list_block(markdown):
        return BlockType.UNORDERED_LIST
    elif is_ordered_list_block(markdown):
        return BlockType.ORDERED_LIST
    else:
        return BlockType.PARAGRAPH  


def is_heading_block(markdown):
    if markdown[0] == "#":
        for i,char in enumerate(markdown):
            if i < 6 and char == "#":
                continue
            if i < 7 and char == " ":
                return True
            else:
                return False
    return 

def is_code_block(markdown):
    return markdown.startswith("```") and markdown.endswith("```")

def is_quote_block(markdown):
    return all(line.startswith(">") for line in markdown.split("\n"))

def is_unordered_list_block(markdown):
    return all(line.startswith("-") for line in markdown.split("\n"))

def is_ordered_list_block(markdown):
    return all(line.startswith(f"{i+1}. ") for i,line in enumerate(markdown.split("\n")))


