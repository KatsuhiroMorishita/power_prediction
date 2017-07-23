# FFTしたら周期構造が見やすいかと思ったけど、そうでもなかった。対数をとったほうが良いみたい。
# http://kiito.hatenablog.com/entry/2013/12/08/211908
import pyaudio
import wave
import numpy as np
import matplotlib.pyplot as plt
import time

plt.figure()

input_filename = 'WaveTest.wav'
buffer_size = 32768
wav_file = wave.open ( input_filename , 'rb' )
p = pyaudio.PyAudio ()
stream = p.open (
                 format = p.get_format_from_width ( wav_file . getsampwidth ()) ,
                 channels = wav_file.getnchannels () ,
                 rate = wav_file.getframerate () ,
                 output = True
                 )
remain = wav_file.getnframes ()
while remain > 0:
    buf = wav_file.readframes ( min ( buffer_size , remain ))
    stream.write(buf)
    #print(type(buf))
    data_fft = np.fft.fft(list(buf))
    print(type(data_fft))
    #print(data_fft)
    plt.plot(np.real(data_fft), label="real part")
    plt.plot(np.imag(data_fft), label="imaginary part")
    plt.grid()
    plt.legend(loc="best")
    plt.show()
    remain -= buffer_size

stream.close ()
p.terminate ()
wav_file.close ()