# 特徴ベクトルと正解値をくっつけたファイルを作成する
import copy
from datetime import timedelta as td
from datetime import datetime as dt

import timeKM



temperature_store = {}

with open("amedas_47893kouchi.csv", "r", encoding="utf-8-sig") as fr:
	lines = fr.readlines()
	for line in lines:                # 1行ずつ取り出す
		line = line.rstrip()          # 改行コード削除
		field = line.split(",") # 分割
		date = timeKM.getTime(field[0])
		value = 9999
		if field[5].replace(".","",1).isdigit(): # 数値化可能か確認
			value = float(field[5])                # 文字列を数値化
		temperature_store[date] = value




data_store = {}

with open("fusion_power.csv", "r", encoding="utf-8-sig") as fr:
	lines = fr.readlines()
	for line in lines:                # 1行ずつ取り出す
		line = line.rstrip()          # 改行コード削除
		date, value = line.split(",") # 分割
		date = timeKM.getTime(date)
		value = int(value)            # 文字列を整数化
		data_store[date] = value


def get_season(_date):
	""" 日付けをシーズン化したもの
	元旦から数えて第何週かを返す。
	"""
	return int((_date - dt(_date.year, 1, 1)).total_seconds() / (7 * 24 * 3600))

def get_data_aday(_date, data):
	_date = dt(_date.year, _date.month, _date.day)
	ans = []
	for i in range(24):
		__date = _date + td(hours=i)
		if __date not in data:
			return None
		ans.append(data[__date])
	return ans


def create_feature(data, target_datetime):
	_feature = []
	_feature += [get_season(target_datetime)]       # 通週
	_feature += [target_datetime.weekday()]         # 曜日
	_feature += [target_datetime.hour]              # 時間
	_t = target_datetime - td(days=3)
	if _t in temperature_store:
		_feature += [temperature_store[_t]] # 気温
	else:
		return None
	hoge = get_data_aday(target_datetime - td(days=3), data)
	if hoge == None:
		return None
	_feature += hoge
	return _feature


date_times = sorted(data_store.keys())
with open("feature.csv", "w") as fw:
	for _date in date_times:
		value = data_store[_date]
		feature = create_feature(data_store, _date)
		if feature == None:
			continue
		teacher = copy.copy(feature) + [value]
		teacher_str_array = [str(x) for x in teacher] # 要素を文字列化
		teacher_str = ",".join(teacher_str_array)     # デリミタで要素同士を結合
		fw.write(str(_date))
		fw.write(",")
		fw.write(teacher_str)
		fw.write("\n")