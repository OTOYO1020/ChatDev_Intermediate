import json
import openai

# APIキーを設定
openai.api_key = "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"

# 入力ファイルと出力ファイルのパス
input_file_path = "prompt2.json"
output_file_path = "task2.json"

# JSONファイルの読み込み
def read_json(file_path):
    try:
        with open(file_path, "r", encoding="utf-8") as file:
            return json.load(file)
    except FileNotFoundError:
        print(f"ファイル {file_path} が見つかりません。")
        return []
    except json.JSONDecodeError:
        print(f"ファイル {file_path} は正しいJSON形式ではありません。")
        return []

# ChatGPTを使用してテキストを分割
def split_text_with_ai(prompt, num_chunks):
    try:
        response = openai.ChatCompletion.create(
            model="gpt-4",
            messages=[
                {"role": "system", "content": "You are an assistant that divides text into equal parts."},
                {"role": "user", "content": f"Please split the following text into {num_chunks} equal parts and format the output as: 'subtask1: ... subtask2: ... subtask3: ... subtask4: ... subtask5: ...': {prompt}"}
            ],
            max_tokens=1500,
            temperature=0.5
        )
        # AIからの応答を取得
        return response["choices"][0]["message"]["content"].split("\n")
    except Exception as e:
        print(f"AIによる分割処理中にエラーが発生しました: {e}")
        return []

# JSONデータを処理して出力ファイルに書き込む
def process_and_write_to_file(input_path, output_path):
    data = read_json(input_path)
    if not data:
        return

    output_data = []

    for entry in data:
        prompt = entry.get("prompt", "")
        if not prompt:
            continue

        # AIを使ってテキストを分割
        chunks = split_text_with_ai(prompt, 5)

        # 分割結果を新しいエントリとして保存
        output_entry = {
            "original_prompt": prompt,
            "formatted_chunks": "\n".join(chunks)
        }
        output_data.append(output_entry)

    # 分割されたデータをJSONファイルに書き込み
    with open(output_path, "w", encoding="utf-8") as file:
        json.dump(output_data, file, ensure_ascii=False, indent=4)

    print(f"分割されたデータが {output_path} に保存されました。")

# メイン処理
def main():
    process_and_write_to_file(input_file_path, output_file_path)

if __name__ == "__main__":
    main()
