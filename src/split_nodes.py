from textnode import TextNode,TextType

def split_nodes_delimiter(old_nodes,delimiter,text_type):
    
    new_nodes = []
    
    for node in old_nodes:
    
        if node.text_type == TextType.TEXT:
            splitted_node = node.text.split(delimiter)
            print(len(splitted_node))
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