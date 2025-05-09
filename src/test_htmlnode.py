import unittest
from htmlnode import HTMLNode,ParentNode,LeafNode

class test_htmlnode(unittest.TestCase):

    def test_prop_to_html(self):
        node = HTMLNode("p","moin",None,{"key":"value","key2":"value2"})

        self.assertEqual(node.props_to_html(),'key="value" key2="value2"')
    
    def test_prop_to_html_2(self):
        node = HTMLNode("p","moin",None,{"href": "https://www.google.com", "target": "_blank"})

        self.assertEqual(node.props_to_html(),'href="https://www.google.com" target="_blank"')
                    
    def test_repr_(self):
        node = HTMLNode("p", "moin", None, {"href": "https://www.google.com", "target": "_blank"})
        expected_repr = 'tag: p, value: moin, props: href="https://www.google.com" target="_blank"'
        
        self.assertEqual(repr(node), expected_repr)

    def test_leaf_to_html_p(self):
        node = LeafNode("p", "Hello, world!")
        self.assertEqual(node.to_html(), "<p>Hello, world!</p>")

    def test_leaf_to_html_link(self):
        node = LeafNode("a", "Click me!", {"href": "https://www.google.com"})
        self.assertEqual(node.to_html(),'<a href="https://www.google.com">Click me!</a>')
    
    def test_to_html_with_children(self):
        child_node = LeafNode("span", "child")
        parent_node = ParentNode("div", [child_node])
        self.assertEqual(parent_node.to_html(), "<div><span>child</span></div>")

    def test_to_html_with_grandchildren(self):
        grandchild_node = LeafNode("b", "grandchild")
        child_node = ParentNode("span", [grandchild_node])
        parent_node = ParentNode("div", [child_node])
        self.assertEqual(
            parent_node.to_html(),
            "<div><span><b>grandchild</b></span></div>")
        
    def test_to_html_empty_children(self):
        node = ParentNode("div", [], {"class": "test"})
        with self.assertRaises(ValueError) as context:
            node.to_html()
        self.assertEqual(str(context.exception), "ParentNode needs to have children")

    def test_to_html_with_props(self):
        child = LeafNode("p", "Hello", None)
        node = ParentNode("div", [child], {"class": "test", "id": "1"})
        expected_html = '<div class="test" id="1"><p>Hello</p></div>'
        self.assertEqual(node.to_html(), expected_html)

        

if __name__ == "__main__":
    unittest.main()