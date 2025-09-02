import os
import shutil

def copy_to_folder(source, destination):
    if not os.path.exists(destination):
        os.mkdir(destination)
    # elif os.path.isfile(destination):
    #     raise Exception("Please enter a folder as destination.")
    elif os.path.exists(destination):
        # shutil.rmtree(destination)
        files_list = os.listdir(destination)
        for file in files_list:
            filepath = os.path.join(destination, file)
            if os.path.isdir(filepath):
                shutil.rmtree(filepath)
            else:
                os.remove(filepath)
    
    files_to_copy = os.listdir(source)
    for file in files_to_copy:
        filepath = os.path.join(source, file)
        dest_path = os.path.join(destination, file)
        print(f" * {filepath} -> {dest_path}")
        if os.path.isfile(filepath):
            shutil.copy(filepath, dest_path)
        else:
            copy_to_folder(filepath, dest_path)
