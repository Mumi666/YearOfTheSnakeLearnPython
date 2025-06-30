import pandas as pd
from collections import Counter

def find_duplicate_invoices(file_path, invoice_column_name='发票号'):
    """
    查找Excel文件中的重复发票号并创建新的sheet页

    参数:
    file_path: Excel文件路径
    invoice_column_name: 发票号列的名称
    """
    try:
        # 读取Excel文件
        df = pd.read_excel(file_path)

        # 检查发票号列是否存在
        if invoice_column_name not in df.columns:
            print(f"错误：未找到列 '{invoice_column_name}'")
            print(f"可用的列名: {list(df.columns)}")
            return

        # 查找重复的发票号
        invoice_counts = df[invoice_column_name].value_counts()
        duplicate_invoices = invoice_counts[invoice_counts > 1].index.tolist()

        if not duplicate_invoices:
            print("未发现重复的发票号")
            return

        # 筛选出所有重复发票号对应的行
        duplicate_rows = df[df[invoice_column_name].isin(duplicate_invoices)]

        # 按发票号排序，方便查看
        duplicate_rows = duplicate_rows.sort_values(by=invoice_column_name)

        # 创建ExcelWriter对象来写入多个sheet
        with pd.ExcelWriter(file_path, engine='openpyxl', mode='a', if_sheet_exists='replace') as writer:
            # 将重复的记录写入新的sheet页
            duplicate_rows.to_excel(writer, sheet_name='重复发票号', index=False)

        print(f"发现 {len(duplicate_invoices)} 个重复的发票号")
        print(f"重复的发票号: {duplicate_invoices}")
        print(f"总共 {len(duplicate_rows)} 条重复记录已写入 '重复发票号' sheet页")

        # 显示重复统计信息
        print("\n重复统计:")
        for invoice in duplicate_invoices:
            count = invoice_counts[invoice]
            print(f"发票号 '{invoice}': 出现 {count} 次")

    except FileNotFoundError:
        print(f"错误：文件 '{file_path}' 未找到")
    except Exception as e:
        print(f"处理过程中出现错误: {str(e)}")

def find_duplicates_advanced(file_path, invoice_column_name='发票号', sheet_name=None):
    """
    高级版本：可以指定特定的sheet页进行处理
    """
    try:
        # 如果指定了sheet名称，则读取特定sheet
        if sheet_name:
            df = pd.read_excel(file_path, sheet_name=sheet_name)
        else:
            df = pd.read_excel(file_path)

        # 检查发票号列是否存在
        if invoice_column_name not in df.columns:
            print(f"错误：未找到列 '{invoice_column_name}'")
            print(f"可用的列名: {list(df.columns)}")
            return

        # 移除空值
        df_clean = df.dropna(subset=[invoice_column_name])

        # 查找重复的发票号
        duplicate_mask = df_clean.duplicated(subset=[invoice_column_name], keep=False)
        duplicate_rows = df_clean[duplicate_mask]

        if duplicate_rows.empty:
            print("未发现重复的发票号")
            return

        # 按发票号排序
        duplicate_rows = duplicate_rows.sort_values(by=invoice_column_name)

        # 添加重复次数列
        invoice_counts = df_clean[invoice_column_name].value_counts()
        duplicate_rows = duplicate_rows.copy()
        duplicate_rows['重复次数'] = duplicate_rows[invoice_column_name].map(invoice_counts)

        # 保存到新的sheet页
        with pd.ExcelWriter(file_path, engine='openpyxl', mode='a', if_sheet_exists='replace') as writer:
            duplicate_rows.to_excel(writer, sheet_name='重复发票号详情', index=False)

        # 创建重复统计摘要
        summary_data = []
        unique_duplicates = duplicate_rows[invoice_column_name].unique()

        for invoice in unique_duplicates:
            count = invoice_counts[invoice]
            summary_data.append({
                '发票号': invoice,
                '重复次数': count,
                '首次出现行号': df_clean[df_clean[invoice_column_name] == invoice].index[0] + 2  # +2因为Excel从1开始且有表头
            })

        summary_df = pd.DataFrame(summary_data)

        # 保存重复摘要到另一个sheet页
        with pd.ExcelWriter(file_path, engine='openpyxl', mode='a', if_sheet_exists='replace') as writer:
            summary_df.to_excel(writer, sheet_name='重复摘要', index=False)

        print(f"处理完成！")
        print(f"发现 {len(unique_duplicates)} 个重复的发票号")
        print(f"总共 {len(duplicate_rows)} 条重复记录")
        print(f"详细信息已保存到 '重复发票号详情' sheet页")
        print(f"摘要信息已保存到 '重复摘要' sheet页")

    except Exception as e:
        print(f"处理过程中出现错误: {str(e)}")

# 使用示例
if __name__ == "__main__":
    # 请将 'your_file.xlsx' 替换为您的Excel文件路径
    file_path = '/Users/shihongjin/Downloads/发票报表数据导出1750210790586.xlsx'

    # 基础版本调用
    print("=== 基础查重处理 ===")
    find_duplicate_invoices(file_path, invoice_column_name='发票号码')

    # print("\n=== 高级查重处理 ===")
    # 高级版本调用（可指定sheet名称）
    # find_duplicates_advanced(file_path, invoice_column_name='发票号', sheet_name=None)
