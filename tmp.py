import re

# ファイルパスを指定
file_path = 'C_agile_100.sh'

# --nameの後に続く数字を格納するリスト
numbers = []

# ファイルを開いて読み込む
with open(file_path, 'r', encoding='utf-8') as file:
    for line in file:
        match = re.search(r'--name\s+"[A-Za-z]+_(\d+)"', line)
        if match:
            numbers.append(int(match.group(1)))

# 数字をソートして出力
for number in sorted(numbers):
    print(number)

