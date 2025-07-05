import unittest
from htmlnode import HTMLNode, LeafNode, ParentNode


class TestHMTLNode(unittest.TestCase):

    # equal standard node tests
    def test_eq(self):
        test_dict = {"href": "https://www.google.com", "target": "_blank",}
        node = HTMLNode("<a>", "hi genius", props=test_dict)
        wanted = ' href="https://www.google.com" target="_blank"'
        self.assertEqual(node.props_to_html(), wanted)

    def test_eq_2(self):
        node = HTMLNode("<a>", "hi genius")
        wanted = None
        self.assertEqual(node.props_to_html(), wanted)
    
    def test_eq_3(self):
        test_dict = {"href": "https://www.boot.dev", "target": "wisdom", "clarity": "0"}
        node = HTMLNode(props=test_dict)
        wanted = ' href="https://www.boot.dev" target="wisdom" clarity="0"'
        self.assertEqual(node.props_to_html(), wanted)
    
    # unequal standard node tests
    def test_uneq(self):
        test_dict = {"href": "https://www.google.com", "target": "_blank", "x": "zet"}
        node = HTMLNode("<a>", "hi genius", props=test_dict)
        wanted = ' href="https://www.google.com" target="_blank"'
        self.assertNotEqual(node.props_to_html(), wanted)
    
    def test_uneq_2(self):
        node = HTMLNode("<a>", "hi genius")
        wanted = "None"
        self.assertNotEqual(node.props_to_html(), wanted)

    def test_uneq_3(self):
        test_dict = {"href": "https://www.boot.dev", "target": "wisdom", "clarity": "0"}
        node = HTMLNode(props=test_dict)
        wanted = 'href="https://www.boot.dev" target="wisdom" clarity="0"'
        self.assertNotEqual(node.props_to_html(), wanted)

    # equal leaf node tests
    def test_leaf_eq(self):
        node = LeafNode("p", "Hello, world!")
        self.assertEqual(node.to_html(), "<p>Hello, world!</p>")
    
    def test_leaf_eq_2(self):
        test_dict = {"href": "https://www.google.com", "target": "_blank",}
        node = LeafNode("p", "Hello, world!", props=test_dict)
        self.assertEqual(node.to_html(), '<p href="https://www.google.com" target="_blank">Hello, world!</p>')

    # unequal leaf node tests
    def test_leaf_uneq(self):
        node = LeafNode("head", "Hello, world!")
        self.assertNotEqual(node.to_html(), "<a>Hello, world!</a>")

    def test_leaf_uneq_2(self):
        test_dict = {"href": "https://www.google.com", "target": "_blank",}
        node = LeafNode("p", "Hello, world!", props=test_dict)
        self.assertNotEqual(node.to_html(), '<p href="https://www.google.com" target="_blank">Hello, world!</a>')

    # equal parent node tests
    def test_to_html_with_children(self):
        child_node = LeafNode("span", "child")
        parent_node = ParentNode("div", [child_node])
        self.assertEqual(parent_node.to_html(), "<div><span>child</span></div>")

    def test_to_html_with_grandchildren(self):
        grandchild_node = LeafNode("b", "grandchild")
        child_node = ParentNode("span", [grandchild_node])
        parent_node = ParentNode("div", [child_node])
        self.assertEqual(parent_node.to_html(), "<div><span><b>grandchild</b></span></div>",)
    
    def test_to_html_multiple_children(self):
        child_1 = LeafNode("b", "change")
        child_2 = LeafNode("i", "must")
        child_3 = LeafNode("u", "happen")
        child_4 = LeafNode("h1", "now")
        parent_1 = ParentNode("body", [child_1, child_2, child_3, child_4])
        self.assertEqual(parent_1.to_html(), "<body><b>change</b><i>must</i><u>happen</u><h1>now</h1></body>")
    
    def test_to_html_multi_children_multi_parents(self):
        child_1 = LeafNode("b", "change")
        child_2 = LeafNode("i", "must")
        child_3 = LeafNode("u", "happen")
        child_4 = LeafNode("h1", "now")
        parent_1 = ParentNode("body", [child_1, child_2])
        parent_2 = ParentNode("head", [child_3, child_4])
        grandparent = ParentNode("html", [parent_1, parent_2])
        self.assertEqual(grandparent.to_html(), "<html><body><b>change</b><i>must</i></body><head><u>happen</u><h1>now</h1></head></html>")

    # unequal parent node tests
    def test_to_html_with_children(self):
        grandchild_node = LeafNode("b", "child")
        child_node = LeafNode("span", [grandchild_node])
        parent_node = ParentNode("div", [child_node])
        self.assertNotEqual(parent_node.to_html(), "<div><span>child</span></div>")

    def test_to_html_with_grandchildren(self):
        grandchild_node = LeafNode("b", "grandchild")
        child_node = ParentNode("div", [grandchild_node])
        parent_node = ParentNode("span", [child_node])
        self.assertNotEqual(parent_node.to_html(), "<div><span><b>grandchild</b></span></div>",)



if __name__ == "__main__":
    unittest.main()
