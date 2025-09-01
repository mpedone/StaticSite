from textnode import TextType, TextNode, text_node_to_html_node
from htmlnode import HTMLnode, LeafNode, ParentNode
from nodesplit import text_to_textnodes, DelimType
from blocks import markdown_to_blocks, block_to_block_type, BlockType
from enum import Enum
import os
import shutil

def folder_generation(source, destination):
    if not os.path.exists(destination):
        os.mkdir(destination)
    elif os.path.isfile(destination):
        raise Exception("Please enter a folder as destination.")
    elif os.path.exists(destination):
        files_list = os.listdir(destination)
        for file in files_list:
            new_path = os.path.join(destination, file)
            os.remove(new_path)
    
    # shutil.copytree(source, destination)
    files_to_copy = os.listdir(source)
    for file in files_to_copy:
        shutil.copyfile


def main():

    try:
        print("this is the main file")
        copy_to_folder("test")

    except Exception as e:
        print(e)


main()
