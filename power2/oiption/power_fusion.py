# power_fusion
# purpose: 電力需要データファイルを結合する
# author: Katsuhiro Morishita
# platform: Python3
# created: 2016-01-07
# linsence: MIT
import glob

file_list = glob.glob("juyo*.csv")
print(file_list)


with open("fusion_power.csv", "w", encoding="utf-8-sig") as fw:
	for fname in file_list:
		with open(fname, "r", encoding="shift_jis") as fr:
			lines = fr.readlines()
			for line in lines:
				if "DATE" in line:
					continue
				if "" == line.rstrip():
					continue
				date, time, value = line.split(",")
				line = date + " " + time + ":0" + "," + value # 日付と時刻を半角スペースで結合する
				fw.write(line)
#with open("")