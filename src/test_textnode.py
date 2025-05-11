import unittest

from textnode import *


class TestTextNode(unittest.TestCase):
    def test_eq(self):
        node = TextNode("This is a text node", TextType.BOLD)
        node2 = TextNode("This is a text node", TextType.BOLD)
        self.assertEqual(node, node2)

    def test_not_eq(self):
        node = TextNode("This is a text node", TextType.BOLD)
        node2 = TextNode("this is a text node",TextType.ITALIC)
        self.assertNotEqual(node,node2)

    def test_link_eq(self):
        node = TextNode("This is a text node", TextType.LINK, "https:/blablabla.com")
        node2 = TextNode("This is a text node", TextType.LINK, "https:/blablabla.com")
        self.assertEqual(node,node2)
    
    def test_text(self):
        node = TextNode("This is a text node", TextType.TEXT)
        html_node = text_node_to_html_node(node)
        self.assertEqual(html_node.tag, None)
        self.assertEqual(html_node.value, "This is a text node")
    
    def test_link(self):
        node = TextNode("link to",TextType.LINK,"https:/blablabla.com")
        html_node = text_node_to_html_node(node)
        self.assertEqual(html_node.tag,"a")
        self.assertEqual(html_node.value,"link to")
        self.assertEqual(html_node.props,{"href":"https:/blablabla.com"})
    
    def test_img(self):
        node = TextNode(None,TextType.IMAGE,"./src/img/chess")
        html_node = text_node_to_html_node(node)
        self.assertEqual(html_node.tag,"img")
        self.assertEqual(html_node.value,None)
        self.assertEqual(html_node.props,{"src":"./src/img/chess","alt":"error"})


if __name__ == "__main__":
    unittest.main()