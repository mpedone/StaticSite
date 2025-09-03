from copy_static import copy_to_folder
from generate import generate_page
import os
import shutil

static_dir = "./static"
public_dir = "./public"

def main():

    try:
        # print("this is the main file")
        # if os.path.exists(public_dir):
        #     shutil.rmtree(public_dir)
        copy_to_folder(static_dir, public_dir)

        from_path = "./content/index.md"
        template_path = "./template.html"
        dest_path = "./public"
        generate_page(from_path, template_path, dest_path)


    except Exception as e:
        print(e)


main()
