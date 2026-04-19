from html_node import HTMLNode

class ParentNode(HTMLNode):
    def __init__(self, tag, children, props = None):
        super(ParentNode, self).__init__(tag, None, children, props)
    
    def to_html(self):
        if self.children == None:
            raise ValueError
        if self.tag == None:
            raise ValueError
        
        child_html = "".join(child.to_html() for child in self.children)

        return f"<{self.tag}{self.props_to_html()}>{child_html}</{self.tag}>"
    
    def __repr__(self):
        return  f"{self.tag}, {self.props}, {self.children}"
    


