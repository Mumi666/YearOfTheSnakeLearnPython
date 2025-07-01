from collections import defaultdict, Counter
from pathlib import Path

import openpyxl

src_file = './file/'

all_excel_file = [file for file in Path(src_file).glob('*.xlsx')]

total_map = defaultdict(int)

for file in all_excel_file:
    wb = openpyxl.load_workbook(file)
    sheets = wb.worksheets
    for sheet in sheets:
        for row in sheet.iter_rows(min_row=2):
            total_map[row[0].value] += row[3].value
    sort_total = Counter(total_map)
    total_map = defaultdict(int)
    print(file.stem + ':')
    print(sort_total.most_common(3))
    wb.close()
