import os
from bs4 import BeautifulSoup

# Define the folder containing HTML files
folder_path = "Documentation\\en\\ScriptReference"

# List all HTML files in the folder
html_files = [f for f in os.listdir(folder_path) if f.endswith(".html")]

# Iterate over the files
for file in html_files:
    file_path = os.path.join(folder_path, file)
    #print(f"Processing: {file_path}")

# Function to extract info from HTML
def extract_info_from_html(file_path):
    with open(file_path, "r", encoding="utf-8") as file:
        soup = BeautifulSoup(file, "html.parser")
    
    # Class Name
    class_name = soup.find("h1").text.strip() if soup.find("h1") else "No Class Name"

    # Description
    description = "No Description"
    description_h3 = soup.find("h3", string="Description")
    if description_h3:
        parent_div = description_h3.find_parent("div")
        if parent_div:
            description_tag = parent_div.find("p")
            if description_tag:
                description = description_tag.text.strip()

    # Declaration
    declaration = "No Declaration"
    declaration_h2 = soup.find("h2", string="Declaration")
    if declaration_h2:
        parent_div = declaration_h2.find_parent("div")  # Locate the containing div
        if parent_div:
            # Collect all text strings in the declaration
            declaration_parts = [
                element.text.strip() for element in parent_div.find_all(string=True) if element.strip()
            ]
            declaration = " ".join(declaration_parts)  # Combine the strings

    # Returns
    Returns = "No Returns"
    Returns_h3 = soup.find("h3", string = "Returns")
    if Returns_h3:
        parent_div = declaration_h2.find_parent("div")  # Locate the containing div
        if parent_div:
            Returns_tag = parent_div.find("p")
            if Returns_tag:
                Returns = description_tag.text.strip()

    # Parameters


    # URL
    url = file_path

    # Debug Outputs
    print(f"Class Name: {class_name}")
    print(f"Description: {description}")
    print(f"Declaration: {declaration}")
    print(f"Returns: {Returns}")
    print(f"Syntax: {syntax}")
    print(f"URL: {url}")

    return class_name, description, Returns, declaration, syntax, url



test = os.path.join(folder_path, html_files[1])
extract_info_from_html(test)
