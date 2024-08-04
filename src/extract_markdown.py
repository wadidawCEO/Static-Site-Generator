import re

def extract_markdown_images(text):
    match = re.findall(r"!\[(.*?)\]\((.*?)\)", text)
    return match

def extract_markdown_links(text):
    text_no_images = re.sub(r"!\[(.*?)\]\((.*?)\)", '', text)
    match = re.findall(r"\[(.*?)\]\((.*?)\)", text_no_images)
    return match