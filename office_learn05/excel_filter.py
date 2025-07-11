import pandas as pd

src_excel_path = './file/CUX_科目发生额查询报表-中药资源-20250206-原始.xlsx'
df = pd.read_excel(src_excel_path, header=2)

# 过滤条件：科目说明 包含"旅客运输"
filtered_df = df[df['科目说明'].str.contains('旅客运输', na=False)]

# 创建ExcelWriter对象
with pd.ExcelWriter(src_excel_path , engine='openpyxl', mode='a', if_sheet_exists= 'replace') as writer:
    # 保存过滤后的数据到另一个sheet
    filtered_df.to_excel(writer, sheet_name='核对表2-旅客运输', index=False)



