
import yaml
import os
import re

# Path to the input YAML file and output directory
# input_yaml_file = "input.yaml"
input_yaml_file = "/home/luanpham/projects/blog/codebase-edu.github.io/_data/sidebars/python_course_sidebar.yml"  # Path to the YAML file
output_directory = "markdown_files"

# Ensure the output directory exists
os.makedirs(output_directory, exist_ok=True)

# Load the YAML content from the file
with open(input_yaml_file, "r", encoding="utf-8") as file:
    data = yaml.safe_load(file)

# Recursive function to process the YAML structure
def process_yaml(data, chapter, file_list):
    if isinstance(data, dict):
        for key, value in data.items():
            if key == "url":
                # Extract the base name of the URL and replace .html with .md
                base_name = os.path.basename(value).replace(".html", ".md")
                file_list.append((base_name, data.get("title", ""), value))
            else:
                process_yaml(value, chapter, file_list)
    elif isinstance(data, list):
        for index, item in enumerate(data, start=1):
            process_yaml(item, f"{chapter}.{index}", file_list)

# List to store the filenames and their titles
file_entries = []

# Process the YAML data
for idx, folder in enumerate(data.get("entries", [])[0].get("folders", []), start=1):
    process_yaml(folder.get("folderitems", []), str(idx), file_entries)


def separate_number_and_text(input_string):
    # Regular expression to match the number and the text
    match = re.match(r"(\d+(\.\d+)?)\s+(.*)", input_string)
    if match:
        number = match.group(1)  # The number part (e.g., 5.3)
        text = match.group(3)    # The text part (e.g., Thuộc tính và phương thức (Attributes và Methods))
        return number, text
    else:
        return None, input_string  # Return None if no number is found

# Generate the .md files with the specified template
for lesson_num, (file_name, title, url) in enumerate(file_entries, start=1):
    lesson_number, lesson_title = separate_number_and_text(str(title))
    md_content = f"""---
    title: "Lập trình Python Cơ bản {lesson_number} - {lesson_title}"
    sidebar: python_course_sidebar
    permalink: {url}
    folder: python-basic-free
---
"""
    
    output_path = os.path.join(output_directory, file_name)
    with open(output_path, "w", encoding="utf-8") as md_file:
        md_file.write(md_content)

print(f"Generated {len(file_entries)} .md files in '{output_directory}'.")
