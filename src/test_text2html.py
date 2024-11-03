import unittest

from textnode import TextNode, TextType
from htmlnode import HTMLNode,LeafNode,ParentNode
from text2html import text_node_to_html_node

class TestTextNodeEdgeCases(unittest.TestCase):
    def test_normal_text_node(self):
        node = TextNode("Normal text", TextType.NORMAL)
        expected = LeafNode(None, "Normal text")
        self.assertEqual(text_node_to_html_node(node), expected)

    def test_links_text_node_with_url(self):
        node = TextNode("Click here", TextType.LINKS, url="http://example.com")
        expected = LeafNode("a", "Click here", {"href": "http://example.com"})
        self.assertEqual(text_node_to_html_node(node), expected)

    def test_links_text_node_without_url(self):
        node = TextNode("Click here", TextType.LINKS)
        with self.assertRaises(Exception) as context:
            text_node_to_html_node(node)
        self.assertTrue('no Url was given' in str(context.exception))

    def test_images_text_node_with_url_and_text(self):
        node = TextNode("An image", TextType.IMAGES, url="http://example.com/image.png")
        expected = LeafNode("img", None, {"src": "http://example.com/image.png", "alt": "An image"})
        self.assertEqual(text_node_to_html_node(node), expected)

    def test_images_text_node_without_url(self):
        node = TextNode("An image", TextType.IMAGES)
        with self.assertRaises(Exception) as context:
            text_node_to_html_node(node)
        self.assertTrue('no Url was given' in str(context.exception))

    def test_text_node_with_none_text(self):
        node = TextNode(None, TextType.NORMAL)
        expected = LeafNode(None, None)
        self.assertEqual(text_node_to_html_node(node), expected)

    def test_code_text_node(self):
        node = TextNode("print('Hello, world!')", TextType.CODE)
        expected = LeafNode("code", "print('Hello, world!')")
        self.assertEqual(text_node_to_html_node(node), expected)

    def test_italic_text_node(self):
        node = TextNode("Italic text", TextType.ITALIC)
        expected = LeafNode("i", "Italic text")
        self.assertEqual(text_node_to_html_node(node), expected)


if __name__ == "__main__":
    unittest.main()
