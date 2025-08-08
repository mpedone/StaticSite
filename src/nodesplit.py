from textnode import TextType, TextNode
from enum import Enum

class DelimType(Enum):
    TEXT = "text"
    BOLD = "**"
    ITALIC = "_"
    CODE = "'"
    LINK = "!["
    IMAGE = "["

def split_nodes_delimiter(old_nodes, delimiter, text_type):
    new_nodes = []
    new_string = ""
    delim_found = False


    for node in old_nodes:
        if delim_found == True:
            raise Exception("Invalid Markdown")
        if node.text_type != TextType.TEXT:
            new_nodes.append(node)
        else:
            if delimiter == "**":
                node.text = node.text.replace("**", "*")
                delimiter = "*"
                end_delimiter = "*"
            if delimiter == "_":
                end_delimiter = "_"
            if delimiter == "`":
                end_delimiter = "`"
            
            for char in node.text:
                if char == delimiter: 
                    if not delim_found and new_string != "":
                        new_nodes.append(TextNode(new_string, node.text_type))
                        new_string = ""
                        delim_found = True
                        delimiter = end_delimiter
                    elif not delim_found and new_string == "":
                        delim_found = True
                        new_string += char
                        delimiter = end_delimiter
                    elif delim_found:
                        new_nodes.append(TextNode(new_string, text_type))
                        new_string = ""
                        delim_found = False
                else:
                    new_string += char
            
            if delim_found:
                raise Exception("Invalid Markdown")
            
            new_nodes.append(TextNode(new_string, node.text_type))
            new_string = ""

            # if delimiter == "]":
    
    return new_nodes  
    
""" def main():

    node1 = TextNode("_This_ is _italic_, this is also _italic_ and this is **bold**", TextType.TEXT)
    node2 = TextNode("This is another _italic_ term.", TextType.TEXT)
    node_list = [node1, node2]
    try:
        # new_node = split_nodes_delimiter([node1], "*", TextType.BOLD)
        print(split_nodes_delimiter(split_nodes_delimiter([node1], "**", TextType.BOLD), "_", TextType.ITALIC))
    except Exception as e:
        print(e)


main()
     """