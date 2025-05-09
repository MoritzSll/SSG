import unittest
from htmlnode import HTMLNode,LeafNode

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

if __name__ == "__main__":
    unittest.main()