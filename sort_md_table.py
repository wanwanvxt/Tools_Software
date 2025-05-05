def sort_markdown_table(file_path):
    with open(file_path, 'r', encoding='utf-8') as file:
        lines = file.readlines()

    table_start = None
    for i, line in enumerate(lines):
        if '|' in line and '-' in line:
            table_start = i - 1 if i > 0 else i
            break

    if table_start is None or table_start + 1 >= len(lines):
        print("Table not found!")
        return

    header = lines[table_start].rstrip('\n')
    separator = lines[table_start + 1].rstrip('\n')

    table_rows = []
    for line in lines[table_start + 2:]:
        if line.strip() == '':
            break
        table_rows.append(line.rstrip('\n'))

    sorted_rows = sorted(
        table_rows,
        key=lambda row: row.split('|')[1].strip().lower()
    )

    new_lines = lines[:table_start] + [header + '\n', separator + '\n']
    new_lines += [row + '\n' for row in sorted_rows]
    new_lines += lines[table_start + 2 + len(table_rows):]

    with open(file_path, 'w', encoding='utf-8', newline="\n") as file:
        file.writelines(new_lines)

    print("Sorted.")

sort_markdown_table("./README.md")