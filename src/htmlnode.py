class HTMLNode():
    def __init__(self, tag=None, value=None, children=None, props=None):
        self.tag = tag
        self.value = value
        self.children = children if children is not None else []
        self.props = props if props is not None else {}
        
    def to_html(self):
        raise NotImplementedError("Implemented in future")
    
    def props_to_html(self):
        return ''.join(f' {key}="{value}"' for key, value in self.props.items())
    
    def __repr__(self):
        return f"HTMLNode(tag={self.tag}, value={self.value}, children={self.children}, props={self.props})"
    
class LeafNode(HTMLNode):
    def __init__(self, tag, value, props=None):
        if value is None:
            raise ValueError("LeafNode must have a value")
        
        super().__init__(tag=tag, value=value, children=[], props=props if props else {})

    def to_html(self):
        if self.tag is None:
            return self.value

        self_closing_tags = {"img", "br", "hr", "input", "link", "meta", "source", "area", "col", "base"}
        
        props_html = self.props_to_html() if self.props else ''
        
        if self.tag in self_closing_tags:
            return f"<{self.tag}{props_html}>"
        
        return f"<{self.tag}{props_html}>{self.value}</{self.tag}>"

    def props_to_html(self):
        return "".join(f' {key}="{value}"' for key, value in self.props.items())
    
    def __repr__(self):
        return f"LeafNode(tag={self.tag}, value={self.value}, children={self.children}, props={self.props})"
    
class ParentNode(HTMLNode):
    def __init__(self, tag, children, props=None):
        if not tag:
            raise ValueError("ParentNode must have a tag")
        if not children:
            raise ValueError("ParentNode must have at least one child")
        
        super().__init__(tag=tag, value=None, children=children, props=props)

    def to_html(self):
        if not self.tag:
            raise ValueError("ParentNode must have a tag")
        if not self.children:
            raise ValueError("ParentNode must have at least one child")
        
        children_html = ''.join(child.to_html() for child in self.children)

        return f"<{self.tag}{self.props_to_html()}>{children_html}</{self.tag}>"
    
    def __repr__(self):
        return f"ParentNode(tag={self.tag}, value={self.value}, children={self.children}, props={self.props})"
