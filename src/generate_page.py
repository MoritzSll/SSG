import os 
from blocks_to_html import markdown_to_html_node,extract_title

def generate_page(from_path,template_path,dest_path):
    print(f"generating page from {from_path} to {dest_path} using {template_path}...")

    with open(from_path, 'r', encoding = "utf-8") as f:
        md = f.read()
    
    with open(template_path, 'r', encoding = "utf-8") as f:
        template_html = f.read()

    html_node = markdown_to_html_node(md)
    content = html_node.to_html()
    title = extract_title(md)
    template_html = template_html.replace("{{ Title }}", title).replace("{{ Content }}", content)
    os.makedirs(os.path.dirname(dest_path), exist_ok=True)

    with open(dest_path, 'w', encoding='utf-8') as f:
        f.write(template_html)

def load_content(path):

    if os.path.isfile(path):
        dest_path = path.replace("content","public").replace("md","html")
        generate_page(path,"template.html",dest_path)
    
    if os.path.isdir(path):
        for entry in os.listdir(path):
            load_content(os.path.join(path,entry))
