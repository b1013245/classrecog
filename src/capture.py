# 動画のある時点でのフレームキャプチャする


import cv2 as cv
import io, sys
from enum import IntEnum

# 日本語出力のための設定
sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8')

_movie_path = '/Users/Asami/Documents/Data_Kaneshige/実験1回目/Movie/'
_midi_path = '/Users/Asami/Documents/keystrokedata/midi_data/ex1/'

class Midi(IntEnum):
    note = 0 
    pitch = 1
    front = 2
    left = 3
    right = 4
    

def read_video(path):
    vc = cv.VideoCapture(path)
#    print("Read " + path)
    return vc



# 打鍵再生時刻をまとめたファイルの読み込み
def read_times(path):
    file = open(path, 'r')
    lines = file.readlines()
    times = [line.split(",") for line in lines]
    file.close()
    return times
    
    
# 画像を必要な領域部分だけにリサイズする
def resize_img():
    print('Resized an image.')



def write(vc, key_num, pos, dir):
    fps = vc.get(cv.CAP_PROP_FPS)
    # キャプチャするフレーム
    frame = int(float(pos) * fps)
    vc.set(cv.CAP_PROP_POS_FRAMES, frame)
    name = str(key_num) + ".jpg"
    cv.imwrite(dir + name, vc.read()[1])



def capture(play_name, angle):
    key_num = 2
    
    times = read_times(_midi_path + play_name + "MIDI.txt")
    vc = read_video(_movie_path + play_name + angle + ".mp4")
    write(vc, key_num, times[key_num][Midi.left.value], "img/"+play_name+angle+"/")
    