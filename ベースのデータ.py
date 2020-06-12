""" 任意の文字列と連番を振った、背景色と画像の大きさを指定した複数個のファイルを
1つのフォルダ内に出力し、クリスタPROでも複数ページの作品を疑似的に扱えるようにしたい
最終的に__main__とかGUI付けて操作しやすくしたりとかしたい"""


import cv2
import numpy as np


HEIGHT = 100
WIGTH = 200
PICTURE = np.zeros((HEIGHT, WIGTH, 3))
PICTURE += 255


PAGE = 3 # 繰り返したい数(総ページ数) 数字しか入らないようにする
FILE = "name" # フォルダ名 英語かローマ字しか使えないようにする
TITLE = "test" # タイトル 同上

# 指定したページの数だけ以下の処理を繰り返し、画像を生成する
for i in range(1, PAGE+1):
    FILE_NAME = r"C:\Users\User\Documents\Python Scripts\200610_pic" + "\\" + FILE + "_" + TITLE + "_" + str(i) + ".png"
    cv2.imwrite(FILE_NAME, PICTURE)
