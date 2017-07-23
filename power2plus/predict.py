#!usr/bin/python3
# -*- coding: utf-8 -*-
#----------------------------------------
# name: predict
# purpose: ランダムフォレストを用いて、学習成果を検証する。
# memo: 1列目を読み飛ばします。列名はないものとします。
# author: Katsuhiro MORISHITA, 森下功啓
# created: 2015-08-08
# lisence: MIT
#----------------------------------------
import pandas
import pickle
from sklearn.ensemble import RandomForestRegressor



def read_training_data(teaching_file_path):
	""" 学習に必要な教師データを読み出す
	"""
	data = pandas.read_csv(teaching_file_path, na_values='None', header=None)
	data = data.dropna()

	#print(data)
	features = (data.iloc[:, 1:-1]).values # transform to ndarray
	labels = (data.iloc[:, -1:]).values
	labels = [flatten for inner in labels for flatten in inner] # transform 2次元 to 1次元 ぽいこと
	#print(labels)
	return (features, labels)


def predict(clf, test_data):
	""" 引数で渡された日付の特徴量を作成して、渡された学習済みの学習器に入力して識別結果を返す
	"""
	features, labels = test_data

	results = []
	for feature in features:
		test = clf.predict(feature)
		results.append(test[0])  # 答えはリストになっているので、0を指定する

	# 予測結果を保存
	with open("result_temp.csv", "w") as fw:
		fw.write("real value,Predicted value\n")
		for predict_result, label in zip(results, labels):
			fw.write(str(label))
			fw.write(",")
			fw.write(str(predict_result))
			fw.write("\n")



def main():
	# 機械学習オブジェクトを生成
	clf = RandomForestRegressor()
	with open('entry_temp.pickle', 'rb') as f:# 学習成果を読み出す
		clf = pickle.load(f)               # オブジェクト復元

	# テストデータの読み込み
	test_data = read_training_data("feature_for_verify.csv")
	predict(clf, test_data)

if __name__ == '__main__':
	main()