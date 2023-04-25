from pprint import pprint as pp
import json


def is_valid_time_string(s):
    """
    文字列sが数字、数字、":"、数字、数字の形式かどうかを判定する関数。
    """
    s = s[:5]

    for i in range(len(s)):
        if i == 2:  # ":"の位置であれば次の文字をチェック
            continue
        if not s[i].isdigit():  # 数字でなければFalseを返す
            return False

    if s[2] != ":":  # ":"の位置になければFalseを返す
        return False

    return True


messages = []
forChat = []
with open("friend.txt") as f,open("data.json", "w") as e:
# with open("kose.txt") as f,open("data.json", "w") as e:
    p = False
    for line in f:
        if p:
            if line[len(line)-2] == '"':
                p = False
            messages[-1]["text"] += line.replace('"', '').replace('\n', "")
        elif is_valid_time_string(line) and line != "":
            if line.split("\t")[2][0] == '"':
                p = True
            dic = {}
            dic["sender"] = line.split("\t")[1]
            dic["text"] = line.split("\t")[2].replace(
                '"', '').replace('\n', "")
            messages.append(dic)
    sender = True
    l = []
    dict = {"prompt": "", "completion": ""}
    for i in messages:
        if i["sender"] != "内藤剛汰":
            if sender:
                dict["prompt"]=dict["prompt"].replace("[スタンプ]","").replace("[写真]","")
                dict["completion"]=dict["completion"].replace("[スタンプ]","").replace("[写真]","")
                if dict["prompt"] != "" and dict["completion"] != "":
                    l.append(dict)
                dict = {"prompt": i["text"], "completion": ""}
            else:
                dict["prompt"] += "\n"+i["text"]
        elif i["sender"] == "内藤剛汰" and dict["prompt"] != "":
            if dict["completion"] == "":
                dict["completion"] = i["text"]
            else:
                dict["completion"] += "\n"+i["text"]
        sender = i["sender"] == "内藤剛汰"
    json.dump(l, e)