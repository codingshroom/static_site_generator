import os
from pathlib import Path
import shutil
from markdown_to_html_node import markdown_to_html_node
from extract_title import extract_title



def copy_static(origin_path, target_path):
    origin_path = os.path.join("/Users/karl/coding/boot.dev/ssg", origin_path)
    target_path = os.path.join("/Users/karl/coding/boot.dev/ssg", target_path)
    if os.path.exists(target_path):
        shutil.rmtree(target_path)
    os.mkdir(target_path)
    for entry in os.listdir(origin_path):
        entry_path = os.path.join(origin_path, entry)
        if os.path.isfile(entry_path):
            shutil.copy(entry_path, target_path)
        else:
            sub_origin_path = os.path.join(origin_path, entry)
            sub_target_path = os.path.join(target_path, entry)
            copy_static(sub_origin_path, sub_target_path)    


def generate_page(from_path, template_path, dest_path):
#    print(f"generating page {from_path} to {dest_path} using {template_path}")
    root_dir = "/Users/karl/coding/boot.dev/ssg"
    from_path = os.path.join(root_dir, from_path)
    template_path = os.path.join(root_dir, template_path)
    dest_path = os.path.join(root_dir, dest_path)
    with open(from_path) as f:
        markdown = f.read()
    title = extract_title(markdown)
    html_string = markdown_to_html_node(markdown).to_html()
    with open(template_path, "r") as f:
        template = f.read()
        template = template.replace("{{ Title }}", title)
        template = template.replace("{{ Content }}", html_string)
    dest_dir_name = os.path.dirname(dest_path)
    create_dirs(dest_dir_name)
    with open(dest_path, "w") as new_file:
        new_file.write(template)


def create_dirs(path):
    if os.path.exists(path):
        return
    create_dirs(os.path.dirname(path))
    os.mkdir(path)


def generate_pages_recursively(from_path, template_path, dest_path):
    root_dir = "/Users/karl/coding/boot.dev/ssg"
    from_path = os.path.join(root_dir, from_path)
    template_path = os.path.join(root_dir, template_path)
    dest_path = os.path.join(root_dir, dest_path)
    Path(dest_path).mkdir(parents=True, exist_ok=True)
    dir_list = os.listdir(from_path)
    for entry in dir_list:
        entry_path = os.path.join(from_path, entry)
        if os.path.isfile(entry_path):
            file_path = os.path.join(dest_path, "index.html")
            generate_page(entry_path, template_path, file_path)  
            continue
        dest_entry_path = os.path.join(dest_path, entry)
        generate_pages_recursively(entry_path, template_path, dest_entry_path)



def main():
    copy_static("static", "public")
    generate_pages_recursively("content", "template.html", "public")

#    generate_page("index.md", "template.html", "index.html")
#    generate_page("contact/index.md", "template.html", "contact/index.html")
#    generate_page("blog/tom/index.md", "template.html", "blog/tom/index.html")
#    generate_page("blog/glorfindel/index.md", "template.html", "blog/glorfindel/index.html")
#    generate_page("blog/majesty/index.md", "template.html", "blog/majesty/index.html")





if __name__ == "__main__":
    main()
