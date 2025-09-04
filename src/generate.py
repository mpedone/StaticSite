import re
import os
from markdown_to_html_node import markdown_to_html_node
from htmlnode import HTMLnode, ParentNode, LeafNode


def extract_title(markdown):
    header = re.search(r"^# (.*)", markdown)
    if header is None:
        raise Exception("No H1 found.")
    title = header.group(1)
    return title

def generate_page(from_path, template_path, dest_path):
    print(f"Generating page from {from_path} to {dest_path} using {template_path}.")
    with open(from_path, "r") as f:
        markdown = f.read()
    with open(template_path, "r") as t:
        template = t.read()
    
    html_nodes = markdown_to_html_node(markdown)
    html_code = html_nodes.to_html()

    title = extract_title(markdown)

    titled_page = re.sub(r"{{ Title }}", title, template)
    full_page = re.sub(r"{{ Content }}", html_code, titled_page)

    if not os.path.exists(dest_path):
        os.makedirs(dest_path, exist_ok=True)

    dest_file_path = os.path.join(dest_path, "index.html")

    with open(dest_file_path, "w") as f:
        f.write(full_page)

# generate_page("./content/index.md", "./template.html", "./static")

"""
If 'from_path' is a directory, list contents
loop through contents
if file is a directory, add to 'from_path' and call function again

for files:
if file is a file, get the filename: 
    os.path.splitext(os.path.basename(filepath))[0]
append ".html" as the new filename.
"""