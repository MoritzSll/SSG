import unittest
from split_nodes import split_nodes_delimiter
from textnode import TextNode,TextType


class test_split_nodes(unittest.TestCase):

    def test_split_delimiter_code(self):
        node = TextNode("This is text with a `code block` word", TextType.TEXT)
        new_nodes = split_nodes_delimiter([node], "`", TextType.CODE)
        self.assertEqual(new_nodes,[
    TextNode("This is text with a ", TextType.TEXT),
    TextNode("code block", TextType.CODE),
    TextNode(" word", TextType.TEXT),
])
    def test_split_delimiter_bold(self):
        node = TextNode("This is text with a **bold block** word",TextType.TEXT)
        new_nodes = split_nodes_delimiter([node],"**",TextType.BOLD)
        self.assertEqual(new_nodes,[
    TextNode("This is text with a ", TextType.TEXT),
    TextNode("bold block", TextType.BOLD),
    TextNode(" word", TextType.TEXT),
])
    def test_split_delimiter_italic(self):
        node = TextNode("This is text with a _italic block_ word",TextType.TEXT)
        new_nodes = split_nodes_delimiter([node],"_",TextType.ITALIC)
        self.assertEqual(new_nodes,[
    TextNode("This is text with a ", TextType.TEXT),
    TextNode("italic block", TextType.ITALIC),
    TextNode(" word", TextType.TEXT),
])    
    def test_split_delimiter_error(self):
        
        node = TextNode("This is_ text with a _italic block_ word",TextType.TEXT)
        with self.assertRaises(SyntaxError) as context:
            split_nodes_delimiter([node],"_",TextType.ITALIC)
        
        self.assertEqual(str(context.exception), "markdown delimiter is not closed properly")






        

if __name__ == "__main__":
    unittest.main()