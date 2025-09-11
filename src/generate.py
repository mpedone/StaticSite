import re
import os
from markdown_to_html_node import markdown_to_html_node
from htmlnode import HTMLnode, ParentNode, LeafNode
from pathlib import Path


def extract_title(markdown):
    header = re.search(r"^# (.*)", markdown)
    if header is None:
        raise Exception("No H1 found.")
    title = header.group(1)
    return title

def generate_page_recursively(from_path, template_path, dest_path, basepath):
    files_list = os.listdir(from_path)
    for file in files_list:
        new_from_path = os.path.join(from_path, file)
        new_dest_path = os.path.join(dest_path, file)
        if os.path.isfile(new_from_path):
            new_dest_path = Path(new_dest_path).with_suffix(".html")
            generate_page(new_from_path, template_path, new_dest_path, basepath)
        else:
            generate_page_recursively(new_from_path, template_path, new_dest_path, basepath)

def generate_page(from_path, template_path, dest_path, basepath):
    print(f"* {from_path} --> {dest_path} <-- {template_path}.")

    with open(from_path, "r") as f:
        markdown = f.read()
        # filename = file.replace(".md", ".html")
    with open(template_path, "r") as t:
        template = t.read()
    html_nodes = markdown_to_html_node(markdown)
    html_code = html_nodes.to_html()

    title = extract_title(markdown)

    titled_page = re.sub(r"{{ Title }}", title, template)
    content_page = re.sub(r"{{ Content }}", html_code, titled_page)

    html_content_page = content_page.replace('href="/', f'href="{basepath}')
    full_page = html_content_page.replace('src="/', f'src="{basepath}')

    dest_dir_path = os.path.dirname(dest_path)
    if not os.path.exists(dest_dir_path):
        os.makedirs(dest_dir_path, exist_ok=True)

    with open(dest_path, "w") as f:
        f.write(full_page)

# generate_page("./content/index.md", "./template.html", "./static")
