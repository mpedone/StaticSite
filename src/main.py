from copy_static import copy_to_folder
from generate import generate_page
import os
# import shutil

static_dir = "./static"
public_dir = "./public"

def main():

    try:
        # print("this is the main file")
        # if os.path.exists(public_dir):
        #     shutil.rmtree(public_dir)
        copy_to_folder(static_dir, public_dir)

        from_path = "./content"
        template_path = "./template.html"
        dest_path = "./public"
        
        # content/blog/glorfindel/index.md
        # content/blog/tom/index.md
        # content/blog/majesty/index.md
        # content/contact/index.md

        '''
        I think I want the function to loop over any folders that might be in the "from_path" folder and look for markdown files. Then, they would take the file name from that folder and create an html file with that name.
        
        So, the function needs to be recursive, and needs to save the current path to recreate (which I think it already does), and the name of the file being used.
        '''

        

        generate_page(from_path, template_path, dest_path)

    except Exception as e:
        print(e)

main()
