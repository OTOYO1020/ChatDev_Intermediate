import re
import csv

# 入力ファイルのパス
input_file = './data_ChatDev_format.sh'
# 出力ファイルのパス
output_file = './prompt.csv'

# 出力用リスト
prompts = []

# データを読み込んで --task 部分を抽出
with open(input_file, 'r') as file:
    for line in file:
        match = re.search(r"--task '(.*?)'", line)
        if match:
            task_content = match.group(1)
            prompts.append([task_content])

# CSV形式でファイルに書き込む
with open(output_file, 'w', newline='') as csv_file:
    writer = csv.writer(csv_file)
    writer.writerow(["prompt"])
    writer.writerows(prompts)

print(f"Extracted {len(prompts)} tasks and saved to {output_file}")
