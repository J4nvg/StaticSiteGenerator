from textnode import TextType,TextNode
from htmlnode import HTMLNode,LeafNode,ParentNode

def text_node_to_html_node(text_node):
    match(TextType(text_node.text_type)):
        case TextType.NORMAL:
            return LeafNode(None,text_node.text)
        case TextType.BOLD:
            return LeafNode("b",text_node.text)
        case TextType.ITALIC:
            return LeafNode("i",text_node.text)
        case TextType.CODE:
            return LeafNode("code",text_node.text)
        case TextType.LINKS:
            if text_node.url is None:
                raise Exception("no Url was given")
            return LeafNode("a",text_node.text,{"href":text_node.url})
        case TextType.IMAGES:
            if text_node.url is None:
                raise Exception("no Url was given")
            return LeafNode("img",None,{"src":text_node.url,"alt":text_node.text})
        case _:
            raise Exception("text node of invalid type")