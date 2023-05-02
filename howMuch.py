import jsonlines
from pathlib import Path
from pprint import pprint as pp
import json


def read_json_file(file_path):
    with open(file_path, "r", encoding="utf-8") as file:
        data = json.load(file)
    return data


def count_tokens(data):
    total_tokens = 0
    for i in range(len(data["prompt"])):
        prompt_tokens = len(data["prompt"][i])
        completion_tokens = len(data["completion"][i])
        total_tokens += prompt_tokens + completion_tokens
    return total_tokens


# JSON Lines ファイルを開く
with jsonlines.open('data_prepared.jsonl') as reader:

    # prompt と completion を格納する空のリストを作成
    prompt_list = []
    completion_list = []

    # 各行のデータに対してループ処理を行う
    for data in reader:

        # prompt と completion を取得し、リストに追加する
        prompt_list.append(data["prompt"])
        completion_list.append(data["completion"])

    # 辞書にデータを格納する
    data_dict = {
        "prompt": prompt_list,
        "completion": completion_list
    }

    # トークン数を計算して出力します
    total_tokens = count_tokens(data_dict)
    print("Total tokens:", str(int(total_tokens/1000*0.0006*133.92*100)/100)+"円")