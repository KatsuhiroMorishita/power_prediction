# waveファイルを作る
import math
import wave
import struct

values = []
with open("fusion_power.csv", "r", encoding="utf-8-sig") as fr:
	lines = fr.readlines()
	for line in lines:
		date, value = line.rstrip().split(",")
		values.append(float(value))
_max = max(values)
amp = 32767.0 / _max * 1.0         # multiplier for amplitude
values = [x * amp for x in values] # 振幅調整


frate = 11025                      # framerate as a float
wav_file = wave.open("WaveTest.wav", "wb")
wav_file.setnchannels(1)
wav_file.setsampwidth(2)
wav_file.setframerate(frate)

for x in values:
    # write the audio frames to file
    wav_file.writeframes(struct.pack('h', int(x)))