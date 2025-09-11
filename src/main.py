from copy_static import copy_to_folder
from generate import generate_page_recursively
import sys

static_dir = "./static"
public_dir = "./docs"

def main():

    try:
        basepath = "/"
        if len(sys.argv) > 1:
            basepath = sys.argv[1]

        print("Deleting docs directory...")
        print("Copying static files to docs directory...")
        copy_to_folder(static_dir, public_dir)

        from_path = "./content"
        template_path = "./template.html"
        dest_path = "./docs"

        print("Generating content...")
        generate_page_recursively(from_path, template_path, dest_path, basepath)

    except Exception as e:
        print(e)

main()
