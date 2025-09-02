from copy_static import copy_to_folder
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

    except Exception as e:
        print(e)


main()
