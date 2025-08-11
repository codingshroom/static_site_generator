

class HTMLNode:
    def __init__(self, tag=None, value=None, children=None, props=None):
        self.tag = tag  # string
        self.value = value  # string
        self.children = children  # list of HTMLNode objects
        self.props = props  # dictionary with attributes in a given tag

    def __repr__(self):
        return f"HTMLNode({self.tag}, {self.value}, {self.children}, {self.props})"

    def to_html(self):
        raise NotImplementedError

    def props_to_html(self):
        if self.props:
            new_list = [" " + key + '="' + self.props[key] + '"' for key in self.props]
            return "".join(new_list)


class LeafNode(HTMLNode):
    def __init__(self, tag, value, props=None):
        super().__init__(tag, value, props)
        self.tag = tag  # string
        self.value = value  # string
        self.props = props  # dictionary with attributes in a given tag
    
    def to_html(self):
        if not self.value:
            raise ValueError("missing value")
        if not self.tag:
            return self.value
        else:
            formatted_props = ""
            if self.props:
                formatted_props = self.props_to_html()
            return f"<{self.tag}{formatted_props}>{self.value}</{self.tag}>"


class ParentNode(HTMLNode):
    def __init__(self, tag, children, props=None):
        super().__init__(tag, children, props)
        self.tag = tag
        self.children = children
        self.props = props

    def to_html(self):
        if not self.tag:
            raise ValueError("missing tag")
        if not self.children:
            raise ValueError("missing children")
        else:
            formatted_props = ""
            if self.props:
                formatted_props = self.props_to_html()
            super_concatenation = f"<{self.tag}{formatted_props}>"
            for child in self.children:
                child_html = child.to_html()
                super_concatenation += child_html
            return super_concatenation + f"</{self.tag}>"
        


if __name__ == "__main__":
    pass
