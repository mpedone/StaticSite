from textnode import TextType, TextNode
from htmlnode import HTMLnode

def main():
    test = TextNode("test", TextType.LINK, "http://a.com")
    test2 = TextNode("test", TextType.LINK, "http://ba.com")
    print(test)
    print(test == test2)

main()