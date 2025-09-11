from copy_static import copy_to_folder
from generate import generate_page_recursively
import os
# import shutil

static_dir = "./static"
public_dir = "./public"

def main():

    try:
        copy_to_folder(static_dir, public_dir)

        from_path = "./content"
        template_path = "./template.html"
        dest_path = "./public"

        generate_page_recursively(from_path, template_path, dest_path)

    except Exception as e:
        print(e)

main()
