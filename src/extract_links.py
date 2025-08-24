import re

def extract_markdown_images(text):
    matches = re.findall(r"!\[([^\[\]]*)\]\(([^\(\)]*)\)", text)
    # matches = re.findall(r"((?<=\[).*?)\]\((http.*?(?=\)))", text)
    # matches = re.findall(r"((?<=\[).*?(?=\]))\]\(((?<=\()http.*?(?=\)))", text)
    return matches

def extract_markdown_links(text):
    matches = re.findall(r"\[([^\[\]]*)\]\(([^\(\)]*)\)", text)
    return matches
