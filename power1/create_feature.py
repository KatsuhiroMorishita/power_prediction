# 特徴ベクトルと正解値をくっつけたファイルを作成する
import copy


data_store = []

with open("fusion_power.csv", "r", encoding="utf-8-sig") as fr:
	lines = fr.readlines()
	count = 0
	data = []                         # []はリスト。C言語でいう配列に似ている。
	for line in lines:                # 1行ずつ取り出す
		line = line.rstrip()          # 改行コード削除
		date, value = line.split(",") # 分割
		value = int(value)            # 文字列を整数化
		data.append(value)
		if len(data) >= 25:
			data_store.append(copy.copy(data)) # リストをコピー
			data.pop(0)               # 要素0番目を削除


with open("feature.csv", "w") as fw:
	for data in data_store:
		data = [str(x) for x in data] # 要素を文字列化
		data = ",".join(data)                # デリミタで要素同士を結合
		fw.write(data)
		fw.write("\n")