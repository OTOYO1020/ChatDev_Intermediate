import difflib
import os


def create_diff_file(dir1, dir2, filename, base_output_dir):
    """
    指定されたファイル名について2つのディレクトリ間の差分を計算し、
    体系的なディレクトリ構造でファイルを保存する関数。
    """
    file1_path = os.path.join(dir1, filename)
    file2_path = os.path.join(dir2, filename)

    # 比較対象のファイルが両方のディレクトリに存在するかチェック
    if not os.path.exists(file1_path):
        print(f"  - ⚠️  スキップ: {file1_path} が見つかりません。")
        return
    if not os.path.exists(file2_path):
        print(f"  - ⚠️  スキップ: {file2_path} が見つかりません。")
        return

    # 出力先ディレクトリを決定 (例: ./diff/main/)
    filename_without_ext = os.path.splitext(filename)[0]
    file_specific_output_dir = os.path.join(base_output_dir, filename_without_ext)
    os.makedirs(file_specific_output_dir, exist_ok=True)

    # 出力ファイルパスを決定 (例: ./diff/main/diff_subtask1_vs_subtask2.diff)
    diff_filename = f"diff_{dir1}_vs_{dir2}.diff"
    output_filepath = os.path.join(file_specific_output_dir, diff_filename)

    try:
        # ファイルを読み込み
        with open(file1_path, "r", encoding="utf-8") as f1:
            file1_lines = f1.readlines()
        with open(file2_path, "r", encoding="utf-8") as f2:
            file2_lines = f2.readlines()

        # 差分を生成
        diff_generator = difflib.unified_diff(
            file1_lines,
            file2_lines,
            fromfile=file1_path,
            tofile=file2_path,
        )
        diff_lines = list(diff_generator)

        if diff_lines:
            with open(output_filepath, "w", encoding="utf-8") as f:
                f.writelines(diff_lines)
            print(f"  - ✅ {filename}: 差分を保存しました -> {output_filepath}")
        else:
            print(f"  - ℹ️  {filename}: 差分はありませんでした。")

    except Exception as e:
        print(f"  - ❌ {filename}: エラーが発生しました: {e}")


def main():
    """
    メイン処理
    """
    print("処理を開始します...")

    # 'subtask'で始まるディレクトリを数字順にソートして取得
    try:
        all_subtask_dirs = sorted(
            [
                d
                for d in os.listdir(".")
                if d.startswith("subtask") and os.path.isdir(d)
            ],
            key=lambda d: int(d.replace("subtask", "")),
        )
    except ValueError:
        print("❌ エラー: 'subtask'に続く文字を数値に変換できませんでした。")
        print(
            "   ディレクトリ名が 'subtask[数字]' の形式になっているか確認してください。"
        )
        return

    if len(all_subtask_dirs) < 2:
        print("比較対象のディレクトリが2つ未満のため、処理を終了します。")
        return

    print(f"検出したディレクトリ: {all_subtask_dirs}")

    # --- 基準となるファイルリストを最初のディレクトリから取得 ---
    reference_dir = all_subtask_dirs[0]
    # .pyで終わるファイルのみを対象とする
    files_to_compare = [
        f
        for f in os.listdir(reference_dir)
        if f.endswith(".py") and os.path.isfile(os.path.join(reference_dir, f))
    ]

    if not files_to_compare:
        print(
            f"基準ディレクトリ '{reference_dir}' 内に比較対象のPythonファイル(.py)が見つかりませんでした。"
        )
        return

    print(f"比較対象のファイルリスト (from {reference_dir}): {files_to_compare}")

    base_output_dir = "./diff"

    # 連続するディレクトリのペアで比較を実行
    for i in range(len(all_subtask_dirs) - 1):
        dir1 = all_subtask_dirs[i]
        dir2 = all_subtask_dirs[i + 1]

        print(f"\n--- 比較中: {dir1} vs {dir2} ---")

        # 見つかったファイルリストを元に、一つずつ比較を実行
        for filename in files_to_compare:
            create_diff_file(dir1, dir2, filename, base_output_dir)

    print("\nすべての処理が完了しました。")


if __name__ == "__main__":
    main()
