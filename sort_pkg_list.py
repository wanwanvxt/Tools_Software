import csv

def sort_csv_file(file_path):
  with open(file_path, 'r', encoding='utf-8') as file:
    reader = list(csv.reader(file))
    if not reader:
      print("File is empty!")
      return

    header = reader[0]
    rows = reader[1:]

    sorted_rows = sorted(rows, key=lambda row: row[0].strip().lower() if len(row) > 1 else "")

  with open(file_path, 'w', encoding='utf-8', newline='') as file:
    writer = csv.writer(file)
    writer.writerow(header)
    writer.writerows(sorted_rows)

  print("CSV sorted")

sort_csv_file("./pkg.csv")