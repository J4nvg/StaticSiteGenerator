import unittest

from htmlnode import HTMLNode,LeafNode,ParentNode

class TestHtmlNode(unittest.TestCase):
    def testNode_eq(self):
        attr= {"href": "https://www.google.com", "target": "_blank"}
        node = HTMLNode("a","This is a link",None,attr)
        self.assertEqual(node.props_to_html(), ' href="https://www.google.com" target="_blank"')
    def testNodeTwo_eq(self):
        attr= {"href": "https://www.google.com", "target": "_blank"}
        node = HTMLNode("a","This is a link",None,None)
        self.assertNotEqual(node.props_to_html(), ' href="https://www.google.com" target="_blank"')
    def testNodeThree_eq(self):
        attr= {"href": "https://www.google.com", 
               "target": "_blank",
               "target": "_blanker",
               "target": "_blankerd",
               "target": "_blankerds",
               }
        node = HTMLNode("a","This is a link",None,attr)
        # print(node.props_to_html())
        self.assertNotEqual(node.props_to_html(), ' href="https://www.google.com" target="_blank" target="_blanker" target="_blankerd" target="_blankerds"')

    def testLeafNode(self):
        node1 = LeafNode("p", "This is a paragraph of text.")
        value = "<p>This is a paragraph of text.</p>"
        self.assertEqual(node1.to_html(),value)
        
    def testLeafNodeTwo(self):
        node1 = LeafNode("a", "Click me!", {"href": "https://www.google.com"})
        value = '<a href="https://www.google.com">Click me!</a>'
        self.assertEqual(node1.to_html(),value)
    def testLeafNodeNone(self):
        node1 = LeafNode("a", "Click me!", None)
        value = '<a href="https://www.google.com">Click me!</a>'
        self.assertNotEqual(node1.to_html(),value)
    def testLeafNodeNone2(self):
        node1 = LeafNode("None", "Click me!", None)
        value = '<a href="https://www.google.com">Click me!</a>'
        self.assertNotEqual(node1.to_html(),value)

    def test_parent_node_single_child(self):
        # Test a ParentNode with a single LeafNode child
        child = LeafNode("a", "Click me!", {"href": "https://www.google.com"})
        parent = ParentNode("div", [child])
        expected_html = '<div><a href="https://www.google.com">Click me!</a></div>'
        self.assertEqual(parent.to_html(), expected_html)

    def test_parent_node_multiple_children(self):
        # Test a ParentNode with multiple children
        child1 = LeafNode("a", "Click me!", {"href": "https://www.google.com"})
        child2 = LeafNode("span", "Some text")
        parent = ParentNode("div", [child1, child2])
        expected_html = '<div><a href="https://www.google.com">Click me!</a><span>Some text</span></div>'
        self.assertEqual(parent.to_html(), expected_html)

    def test_parent_node_with_props(self):
        # Test a ParentNode with properties
        child = LeafNode("a", "Click me!", {"href": "https://www.google.com"})
        parent = ParentNode("div", [child], {"class": "container"})
        expected_html = '<div class="container"><a href="https://www.google.com">Click me!</a></div>'
        self.assertEqual(parent.to_html(), expected_html)

    def test_parent_node_no_children_error(self):
        # Test that an error is raised when children is None
        with self.assertRaises(ValueError) as context:
            ParentNode("div", None).to_html()
        self.assertEqual(str(context.exception), "No children were given.")

    def test_parent_node_non_list_children_error(self):
        # Test that an error is raised when children is not a list
        child = LeafNode("a", "Click me!", {"href": "https://www.google.com"})
        with self.assertRaises(TypeError) as context:
            ParentNode("div", child).to_html()
        self.assertEqual(str(context.exception), "children is not of list type")

    def test_parent_node_no_tag_error(self):
        # Test that an error is raised when tag is None
        child = LeafNode("a", "Click me!", {"href": "https://www.google.com"})
        with self.assertRaises(ValueError) as context:
            ParentNode(None, [child]).to_html()
        self.assertEqual(str(context.exception), "No tag was given.")

if __name__ == "__main__":
    unittest.main()
