import re

def sort_markdown_list(file_path):
    with open(file_path, 'r') as file:
        content = file.readlines()
    
    # Define a regex pattern to match list items starting with '*'
    list_pattern = re.compile(r'^\s*\*\s+(.+)')
    
    # Extract list items and their positions
    list_items = []
    for i, line in enumerate(content):
        match = list_pattern.match(line)
        if match:
            list_items.append((i, match.group(1)))  # Store index and content of list item
    
    # If no list items are found, return as is
    if not list_items:
        print("No list found!")
        return
    
    # Sort list items alphabetically (case-insensitive)
    sorted_items = sorted((item[1] for item in list_items), key=str.lower)
    
    # Replace the old list items in the content
    for i, item in zip([index for index, _ in list_items], sorted_items):
        content[i] = f"* {item}\n"
    
    # Save the updated content back to the file
    with open(file_path, 'w') as file:
        file.writelines(content)
    print(f"Sorted list saved in {file_path}.")

sort_markdown_list("./README.md")