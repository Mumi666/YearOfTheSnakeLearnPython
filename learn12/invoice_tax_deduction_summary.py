import pandas as pd
import numpy as np

def summarize_invoice_tax_deduction(file_path, invoice_column='发票号', tax_column='进项税抵扣金额', sheet_name=None):
    """
    汇总同一发票号的进项税抵扣金额
    
    参数:
    file_path: Excel文件路径
    invoice_column: 发票号列名
    tax_column: 进项税抵扣金额列名
    sheet_name: 要处理的sheet名称，如果为None则处理第一个sheet
    """
    try:
        # 读取Excel文件
        if sheet_name:
            df = pd.read_excel(file_path, sheet_name=sheet_name)
            print(f"正在处理sheet: {sheet_name}")
        else:
            df = pd.read_excel(file_path)
            print("正在处理默认sheet")
        
        # 检查必要的列是否存在
        if invoice_column not in df.columns:
            print(f"错误：未找到发票号列 '{invoice_column}'")
            print(f"可用的列名: {list(df.columns)}")
            return
        
        if tax_column not in df.columns:
            print(f"错误：未找到进项税抵扣金额列 '{tax_column}'")
            print(f"可用的列名: {list(df.columns)}")
            return
        
        # 清理数据：移除发票号为空的行
        df_clean = df.dropna(subset=[invoice_column]).copy()
        
        # 处理进项税抵扣金额列：转换为数值类型
        df_clean[tax_column] = pd.to_numeric(df_clean[tax_column], errors='coerce')
        
        # 移除进项税抵扣金额为空或无效的行
        df_clean = df_clean.dropna(subset=[tax_column])
        
        print(f"清理后的数据行数: {len(df_clean)}")
        
        # 按发票号分组汇总
        summary_agg = df_clean.groupby(invoice_column).agg({
            tax_column: ['sum', 'count', 'mean', 'max', 'min']
        }).round(2)
        
        # 简化列名
        summary_agg.columns = ['抵扣金额汇总', '记录数量', '平均金额', '最大金额', '最小金额']
        summary_agg = summary_agg.reset_index()
        
        # 添加是否有重复记录的标识
        summary_agg['是否重复'] = summary_agg['记录数量'] > 1
        
        # 按汇总金额降序排列
        summary_agg = summary_agg.sort_values('抵扣金额汇总', ascending=False)
        
        # 创建详细汇总表（包含原始数据的其他列）
        detailed_summary = create_detailed_summary(df_clean, invoice_column, tax_column)
        
        # 保存结果到新的sheet页
        with pd.ExcelWriter(file_path, engine='openpyxl', mode='a', if_sheet_exists='replace') as writer:
            # 保存汇总统计
            summary_agg.to_excel(writer, sheet_name='进项税汇总统计', index=False)
            
            # 保存详细汇总
            detailed_summary.to_excel(writer, sheet_name='进项税详细汇总', index=False)
        
        # 输出统计信息
        print(f"\n=== 汇总统计结果 ===")
        print(f"总发票数量: {len(summary_agg)}")
        print(f"有重复记录的发票数: {sum(summary_agg['是否重复'])}")
        print(f"进项税抵扣金额总计: {summary_agg['抵扣金额汇总'].sum():,.2f}")
        print(f"平均每张发票抵扣金额: {summary_agg['抵扣金额汇总'].mean():,.2f}")
        
        # 显示前10大抵扣金额
        print(f"\n=== 前10大抵扣金额发票 ===")
        top_10 = summary_agg.head(10)
        for idx, row in top_10.iterrows():
            print(f"发票号: {row[invoice_column]}, 抵扣金额: {row['抵扣金额汇总']:,.2f}, 记录数: {row['记录数量']}")
        
        # 显示有重复记录的发票
        duplicates = summary_agg[summary_agg['是否重复']]
        if not duplicates.empty:
            print(f"\n=== 有重复记录的发票（共{len(duplicates)}张）===")
            for idx, row in duplicates.iterrows():
                print(f"发票号: {row[invoice_column]}, 汇总金额: {row['抵扣金额汇总']:,.2f}, 记录数: {row['记录数量']}")
        
        return summary_agg, detailed_summary
        
    except Exception as e:
        print(f"处理过程中出现错误: {str(e)}")
        return None, None

def create_detailed_summary(df, invoice_column, tax_column):
    """
    创建详细的汇总表，包含每个发票号的所有相关信息
    """
    # 为每个发票号创建汇总记录
    detailed_records = []
    
    for invoice_no in df[invoice_column].unique():
        invoice_data = df[df[invoice_column] == invoice_no]
        
        # 基础汇总信息
        summary_record = {
            invoice_column: invoice_no,
            '原始记录数': len(invoice_data),
            f'{tax_column}_汇总': invoice_data[tax_column].sum(),
            f'{tax_column}_平均': invoice_data[tax_column].mean(),
            f'{tax_column}_最大': invoice_data[tax_column].max(),
            f'{tax_column}_最小': invoice_data[tax_column].min(),
        }
        
        # 添加其他重要列的信息（如果存在）
        important_columns = ['供应商名称', '开票日期', '税率', '不含税金额', '税额']
        for col in important_columns:
            if col in df.columns:
                if invoice_data[col].nunique() == 1:
                    # 如果该列所有值都相同，则直接使用该值
                    summary_record[col] = invoice_data[col].iloc[0]
                else:
                    # 如果有不同值，则标记为"多值"
                    summary_record[col] = f"多值({invoice_data[col].nunique()}种)"
        
        detailed_records.append(summary_record)
    
    detailed_df = pd.DataFrame(detailed_records)
    detailed_df = detailed_df.sort_values(f'{tax_column}_汇总', ascending=False)
    
    return detailed_df

def analyze_tax_deduction_patterns(file_path, invoice_column='发票号', tax_column='进项税抵扣金额'):
    """
    分析进项税抵扣的模式和异常情况
    """
    try:
        df = pd.read_excel(file_path)
        df_clean = df.dropna(subset=[invoice_column, tax_column]).copy()
        df_clean[tax_column] = pd.to_numeric(df_clean[tax_column], errors='coerce')
        df_clean = df_clean.dropna(subset=[tax_column])
        
        # 分析异常情况
        analysis_results = {
            '零抵扣发票': df_clean[df_clean[tax_column] == 0],
            '负数抵扣发票': df_clean[df_clean[tax_column] < 0],
            '大额抵扣发票': df_clean[df_clean[tax_column] > df_clean[tax_column].quantile(0.95)],
        }
        
        print("=== 进项税抵扣异常分析 ===")
        for category, data in analysis_results.items():
            print(f"{category}: {len(data)} 张发票")
            if len(data) > 0:
                print(f"  金额范围: {data[tax_column].min():,.2f} ~ {data[tax_column].max():,.2f}")
        
        # 保存异常分析结果
        with pd.ExcelWriter(file_path, engine='openpyxl', mode='a', if_sheet_exists='replace') as writer:
            for category, data in analysis_results.items():
                if not data.empty:
                    data.to_excel(writer, sheet_name=f'{category}分析', index=False)
        
        return analysis_results
        
    except Exception as e:
        print(f"异常分析出错: {str(e)}")
        return None

# 主函数
def main():
    # 请将文件路径替换为您的实际文件路径
    file_path = '/Users/shihongjin/Downloads/发票报表数据导出1750210790586.xlsx'
    
    print("=== 开始进项税抵扣金额汇总 ===")
    
    # 执行汇总
    summary, detailed = summarize_invoice_tax_deduction(
        file_path=file_path,
        invoice_column='发票号码',
        tax_column='进项税抵扣金额',
        sheet_name=None  # 如果要处理特定sheet，请指定名称
    )
    
    if summary is not None:
        print("\n汇总完成！结果已保存到以下sheet页:")
        print("- 进项税汇总统计")
        print("- 进项税详细汇总")
        
        # 执行异常分析
        print("\n=== 开始异常情况分析 ===")
        analyze_tax_deduction_patterns(file_path)
        print("异常分析完成！")

if __name__ == "__main__":
    main()
