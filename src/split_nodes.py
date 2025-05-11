import re
from textnode import TextNode,TextType

def split_nodes_delimiter(old_nodes,delimiter,text_type):
    
    new_nodes = []
    
    for node in old_nodes:
    
        if node.text_type == TextType.TEXT:
            splitted_node = node.text.split(delimiter)
            if len(splitted_node) % 2 == 0:
                raise SyntaxError("markdown delimiter is not closed properly")
            
            for i in range(len(splitted_node)):
                if i % 2 == 0:
                    new_nodes.append(TextNode(splitted_node[i],TextType.TEXT))
                else:
                    new_nodes.append(TextNode(splitted_node[i],text_type))
        else:
            new_nodes.append(node)
        
    return new_nodes
      
def split_nodes_image(old_nodes):
    new_nodes = []
    for node in old_nodes:
        if node.text_type != TextType.TEXT:
            new_nodes.append(node)
            continue
        images = extract_markdown_image(node.text)
        if images:
            text_parts = re.split(r'!\[[^\[\]]*\]\([^\(\)]*\)', node.text)
            for text in text_parts:
                    if text == "":
                        if images:
                            image = images.pop(0)
                            new_nodes.append(TextNode(image[0],TextType.IMAGE,image[1]))
                        continue
                    new_nodes.append(TextNode(text,TextType.TEXT))    
                    if images:
                        image = images.pop(0)
                        new_nodes.append(TextNode(image[0],TextType.IMAGE,image[1]))
        else:
            new_nodes.append(node)
    return new_nodes

def split_nodes_link(old_nodes):
    new_nodes = []
    for node in old_nodes:
        if node.text_type != TextType.TEXT:
                new_nodes.append(node)
                continue
        links = extract_markdown_link(node.text)
        if links:
            text_parts = re.split(r'\[[^\[\]]*\]\([^\(\)]*\)', node.text)
            for text in text_parts:
                    if text == "":
                        if links:
                            link = links.pop(0)   
                            new_nodes.append(TextNode(link[0],TextType.LINK,link[1]))
                        continue
                    new_nodes.append(TextNode(text,TextType.TEXT))
                    if links:
                        link = links.pop(0)   
                        new_nodes.append(TextNode(link[0],TextType.LINK,link[1]))
        else:
            new_nodes.append(node)
    return new_nodes

def extract_markdown_image(text):
    images = re.findall(r"!\[([^\[\]]*)\]\(([^\(\)]*)\)", text)
    return images

def extract_markdown_link(text):
    links = re.findall(r"(?<!!)\[([^\[\]]*)\]\(([^\(\)]*)\)", text)
    return links

def text_to_textnodes(text):
    node = TextNode(text,TextType.TEXT)
    text_nodes = split_nodes_delimiter([node],"**",TextType.BOLD)
    text_nodes = split_nodes_delimiter(text_nodes,"_",TextType.ITALIC)
    text_nodes = split_nodes_delimiter(text_nodes,"`",TextType.CODE)
    text_nodes = split_nodes_image(text_nodes)
    text_nodes = split_nodes_link(text_nodes)
    return text_nodes
    

