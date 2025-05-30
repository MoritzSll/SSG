class HTMLNode():
    def __init__(self,tag,value,children,props):
        self.tag = tag
        self.value = value
        self.children = children
        self.props = props

    def to_html(self):
        raise NotImplementedError
    
    def props_to_html(self):
        str = ""
        if self.props:
            for key,value in self.props.items():
                str += f'{key}="{value}" '
            return str.strip()
        else:
            return None
    
    def __repr__(self):
        return f"tag: {self.tag}, value: {self.value}, props: {self.props_to_html()}"

class LeafNode(HTMLNode):

    def __init__(self,tag,value,props = None):
        super().__init__(tag,value,None,props)
    
    def to_html(self):
        if self.value == None:
            raise ValueError("all LeafNodes must have a value")
        
        if self.tag == None:
            return self.value
        elif self.props == None:
            return f"<{self.tag}>{self.value}</{self.tag}>"
        else:
            return f"<{self.tag} {self.props_to_html()}>{self.value}</{self.tag}>"
        
class ParentNode(HTMLNode):
    def __init__(self,tag,children,props= None):
        super().__init__(tag,None,children,props)

    def to_html(self):
        
        if not self.tag:
            raise ValueError("ParentNode needs to have a tag")
        
        if not self.children:
            raise ValueError("ParentNode needs to have children")
        
        html = ""
        if self.props:
            html += f"<{self.tag} {self.props_to_html()}>"
        else:
            html += f"<{self.tag}>"
        for child in self.children:
            html += child.to_html() 
        html += f"</{self.tag}>"
        return html