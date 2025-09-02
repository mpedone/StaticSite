from textnode import TextType, TextNode, text_node_to_html_node
from htmlnode import HTMLnode, LeafNode, ParentNode
from nodesplit import text_to_textnodes, DelimType
from blocks import markdown_to_blocks, block_to_block_type, BlockType
from enum import Enum
import os
import shutil

def copy_to_folder(source, destination):
    if not os.path.exists(destination):
        os.mkdir(destination)
    elif os.path.isfile(destination):
        raise Exception("Please enter a folder as destination.")
    elif os.path.exists(destination):
        # shutil.rmtree(destination)
        files_list = os.listdir(destination)
        for file in files_list:
            filepath = os.path.join(destination, file)
            if os.path.isdir(filepath):
                shutil.rmtree(filepath)
            else:
                new_path = os.path.join(destination, file)
                os.remove(new_path)
    
    files_to_copy = os.listdir(source)
    for file in files_to_copy:
        filepath = os.path.join(source, file)
        if os.path.isdir(filepath):
            new_destination = os.path.join(destination, file)
            copy_to_folder(filepath, new_destination)
        else:
            print(filepath)
            shutil.copy(filepath, destination)


def main():

    try:
        # print("this is the main file")
        copy_to_folder("static", "public")

    except Exception as e:
        print(e)


main()
