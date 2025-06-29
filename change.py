import re


def process_script_line(line):
    # subtaskの内容を抽出（--subtask1 〜 --subtask10）
    subtask_pattern = r'--subtask\d+ "([^"]+)"'
    subtasks = re.findall(subtask_pattern, line)

    # 全subtaskの内容を順に結合（コピペの要領）
    task_string = ' '.join(subtasks)

    # --task を末尾に追加
    new_line = line.strip() + f' --task "{task_string}"'
    return new_line

def main():
    input_file = "Cn_100.sh"
    output_file = "Cn_1002.sh"

    with open(input_file, "r", encoding="utf-8") as f:
        lines = f.readlines()

    # 変換処理（python3 run.py で始まる行のみ対象）
    modified_lines = [process_script_line(line) for line in lines if line.strip().startswith("python3 run.py")]

    with open(output_file, "w", encoding="utf-8") as f:
        for line in modified_lines:
            f.write(line + "\n")

    print(f"変換完了：{output_file} に保存しました。")

if __name__ == "__main__":
    main()
