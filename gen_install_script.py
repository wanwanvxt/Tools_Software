def generate_install_script(markdown_file, output_script="install.ps1"):
    with open(markdown_file, 'r', encoding='utf-8') as file:
        lines = file.readlines()

    # Tìm bảng
    table_start = None
    for i, line in enumerate(lines):
        if '|' in line and '-' in line:
            table_start = i - 1 if i > 0 else i
            break

    if table_start is None:
        print("Table not found!")
        return

    header = lines[table_start].strip()
    table_lines = []

    for line in lines[table_start + 2:]:
        if line.strip() == '':
            break
        table_lines.append(line.strip())

    commands = []
    for row in table_lines:
        columns = [col.strip() for col in row.split('|')[1:-1]]  # Bỏ cột ngoài cùng do split `|...|`
        if not columns or len(columns) < 1:
            continue
        pkg = columns[0]
        params = columns[1] if len(columns) > 1 else ''
        install_args = columns[2] if len(columns) > 2 else ''

        cmd = f"choco install {pkg}"
        if params:
            cmd += f" --params \"'{params}'\""
        if install_args:
            cmd += f" --install-arguments \"'{install_args}'\""
        cmd += " -y"

        commands.append(cmd)

    with open(output_script, 'w', encoding='utf-8', newline='\n') as out:
        out.write("Set-ExecutionPolicy Bypass -Scope Process -Force\n")
        out.write("$ErrorActionPreference = 'Stop'\n\n")
        for cmd in commands:
            out.write(cmd + '\n')

    print("Generated install script.")

generate_install_script("./README.md")