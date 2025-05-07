import csv

def generate_install_script(csv_file, output_script="install.ps1"):
  with open(csv_file, 'r', encoding='utf-8') as file:
    reader = csv.reader(file)
    rows = list(reader)

  if not rows or len(rows[0]) < 1:
    print("Invalid CSV format or empty file.")
    return

  header = rows[0]
  data_rows = rows[1:]

  commands = []
  for row in data_rows:
    if not row or len(row) < 1:
      continue
    pkg = row[0].strip()
    params = row[1].strip() if len(row) > 1 else ''
    install_args = row[2].strip() if len(row) > 2 else ''
    addn_params = row[3].strip() if len(row) > 3 else ''

    cmd = f"choco install {pkg}"
    if params:
      cmd += f" --params \"'{params}'\""
    if install_args:
      cmd += f" --install-arguments \"'{install_args}'\""
    cmd += f" -y {addn_params}"

    commands.append(cmd)

  with open(output_script, 'w', encoding='utf-8', newline='\n') as out:
    out.write("Set-ExecutionPolicy Bypass -Scope Process -Force\n")
    out.write("$ErrorActionPreference = 'Stop'\n\n")
    for cmd in commands:
      out.write(cmd + '\n')

  print("Generated install script.")

generate_install_script("./pkg.csv")