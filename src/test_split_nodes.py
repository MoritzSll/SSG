import unittest
from split_nodes import split_nodes_delimiter,extract_markdown_image,split_nodes_image,extract_markdown_link,split_nodes_link
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
    
    def test_extract_markdown_images(self):
        matches = extract_markdown_image(
            "This is text with an ![image](https://i.imgur.com/zjjcJKZ.png)"
        )
        self.assertListEqual([("image", "https://i.imgur.com/zjjcJKZ.png")], matches)

    def test_extract_markdown_links(self):
        matches = extract_markdown_link(
            "This is text with an [link](https://blablabla.com)"
        )
        self.assertListEqual([("link", "https://blablabla.com")], matches)
    
    def test_split_images(self):
        node = TextNode(
            "This is text with an ![image](https://i.imgur.com/zjjcJKZ.png) and another ![second image](https://i.imgur.com/3elNhQu.png)",
            TextType.TEXT,
        )
        new_nodes = split_nodes_image([node])
        self.assertListEqual(
            [
                TextNode("This is text with an ", TextType.TEXT),
                TextNode("image", TextType.IMAGE, "https://i.imgur.com/zjjcJKZ.png"),
                TextNode(" and another ", TextType.TEXT),
                TextNode(
                    "second image", TextType.IMAGE, "https://i.imgur.com/3elNhQu.png"
                ),
            ],
            new_nodes,
    )
    
    def test_split_links(self):
        node = TextNode(
            "This is text with an [link](https://blablabla.com) and another [second link](https://blublublu.com)",
            TextType.TEXT,
        )
        new_nodes = split_nodes_link([node])
        self.assertListEqual(
            [
                TextNode("This is text with an ", TextType.TEXT),
                TextNode("link", TextType.LINK, "https://blablabla.com"),
                TextNode(" and another ", TextType.TEXT),
                TextNode(
                    "second link", TextType.LINK, "https://blublublu.com"
                ),
            ],
            new_nodes,
    )
    
    def test_split_images_no_text_between(self):
        node = TextNode(
            "This is text with an ![image](https://i.imgur.com/zjjcJKZ.png) ![second image](https://i.imgur.com/3elNhQu.png)",
            TextType.TEXT,
        )
        new_nodes = split_nodes_image([node])
        self.assertListEqual(
            [
                TextNode("This is text with an ", TextType.TEXT),
                TextNode("image", TextType.IMAGE, "https://i.imgur.com/zjjcJKZ.png"),
                TextNode(" ",TextType.TEXT),
                TextNode(
                    "second image", TextType.IMAGE, "https://i.imgur.com/3elNhQu.png"
                ),
            ],
            new_nodes,
    )
    
    def test_split_images_no_space(self):
        node = TextNode(
            "This is text with an ![image](https://i.imgur.com/zjjcJKZ.png)![second image](https://i.imgur.com/3elNhQu.png)",
            TextType.TEXT,
        )
        new_nodes = split_nodes_image([node])
        self.assertListEqual(
            [
                TextNode("This is text with an ", TextType.TEXT),
                TextNode("image", TextType.IMAGE, "https://i.imgur.com/zjjcJKZ.png"),
                TextNode(
                    "second image", TextType.IMAGE, "https://i.imgur.com/3elNhQu.png"
                ),
            ],
            new_nodes,
    )
    
    def test_split_image_single(self):
        node = TextNode(
            "![image](https://www.example.COM/IMAGE.PNG)",
            TextType.TEXT,
        )
        new_nodes = split_nodes_image([node])
        self.assertListEqual(
            [
                TextNode("image", TextType.IMAGE, "https://www.example.COM/IMAGE.PNG"),
            ],
            new_nodes,
        )



        

        





        

if __name__ == "__main__":
    unittest.main()