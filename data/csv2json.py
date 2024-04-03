import csv
import json

# 打开CSV文件
csv_file = "a.csv"  # 替换为你的UTF-8编码的CSV文件路径

# 打开JSON文件
json_file = "output.json"  # 替换为你要保存的JSON文件路径

# 定义用于保存JSON数据的列表
json_data = []

# 打开CSV文件并读取数据
with open(csv_file, "r", encoding="utf-8") as csvfile:
    csv_reader = csv.DictReader(csvfile)
    for row in csv_reader:
        json_data.append(row)

# 将数据保存为JSON文件
with open(json_file, "w", encoding="utf-8") as jsonfile:
    json.dump(json_data, jsonfile, ensure_ascii=False, indent=4)

print(f"UTF-8编码的CSV文件 '{csv_file}' 已成功转换为JSON文件 '{json_file}'")

