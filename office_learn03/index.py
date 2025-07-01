import openpyxl
from pathlib import Path,PurePath

src_path = './file/'

p = Path(src_path)

all_excel_file = [ file for file in p.iterdir() if PurePath(file).match('*.xlsx') ]

product_map = {}

for file in all_excel_file:
    wb = openpyxl.load_workbook(file)
    sheets = wb.worksheets
    for sheet in sheets:
        for row in sheet.iter_rows(min_row=2):
            if row[0].value in product_map:
                product_map[row[0].value] += row[3].value
            else:
                product_map[row[0].value] = row[3].value
    wb.close()

print(product_map)
