import unittest

from textnode import TextNode, TextType

class TestTextNode(unittest.TestCase):
    def test_eq(self):
        node = TextNode("This is a text node", TextType.BOLD)
        node2 = TextNode("This is a text node", TextType.BOLD)
        self.assertEqual(node, node2)
    def test_eq_two(self):
        node = TextNode("This is my first written test",TextType.IMAGES,"https://www.saenigma.com")
        node2 = TextNode("This is my AAAfirst written test",TextType.IMAGES,"https://www.saenigma.com")
        self.assertNotEqual(node, node2)
    def test_eq_three(self):
        node = TextNode("This is my 2nd written test",TextType.IMAGES,None)
        node2 = TextNode("This is my 2nd written test",TextType.IMAGES,"https://www.saenigma.com")
        self.assertNotEqual(node, node2)
    def test_eq_four(self):
        node = TextNode("This is my 3rd written test",TextType.IMAGES,None)
        node2 = TextNode("This is my 3rd written test",TextType.IMAGES,None)
        self.assertEqual(node, node2)

if __name__ == "__main__":
    unittest.main()
