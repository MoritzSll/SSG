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
        for key,value in self.props.items():
            str += f'{key}="{value}" '
        return str.strip()
    
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