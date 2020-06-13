"""
B5のサイズは 3541 x 2508 px モノクロなら解像度600dpi
ただし、B5の本にするためにはA4サイズの紙に書く必要がある
A4のサイズは 4093 x 2894 px

B5を選んだらA4サイズを出力するようにする。
製本を予定しているか本当にB5のデータが欲しいのか聞く？
やること
# 各Entryの初期値をB5かA4にする
# このコードがある場所のパスを取得して使用するか、もっと便利な方法を見つける
"""
import os
import tkinter as tk
from tkinter import filedialog
import cv2
import numpy as np



###################################################################################
def a():
    """
    各Entryに入力された値を全て.txtに記録する
    B5サイズ等のプリセットもこのテキストファイルに保存しとく？
    """
    HEIBOX.get() # HEIBOXの中身を取ってくる
    たかさ = int(HEIBOX.get()) # HEIBOXの中身をHEIGHTに入れる
    WIGBOX.get()
    はば = int(WIGBOX.get())
    PAGEBOX.get()
    ぺーじ = int(PAGEBOX.get())
    TITLE = (TITBOX.get())
    たいとる = TITLE

    s = [たかさ, はば, ぺーじ, たいとる]
    path = os.getcwd()
    with open(path, mode="a", encoding="utf-8") as f:
        f.write("\n".join(s))


###################################################################################

# メニューバー仮設定
#def first():
    #pass
def second():
    pass
def third():
    pass
def four():
    pass

def folderselect():
    """
    フォルダ指定をする関数。
    メニューバーのファイルボタン内と、ボタンか起動するたびポップアップ？
    """
    #iDir = os.path.abspath(os.path.dirname(__file__))     #GUI表示でのデフォルトパスを指定
    iDir = "C:\\pg" 
    global PATH
    PATH = filedialog.askdirectory(initialdir=iDir)   #指定したファイル名を取得する (キャンセル時は空文字)
    var.set(str(PATH))
    #print(PATH)
    #if folder != "":
        #tk.messagebox.showinfo(Label='folder', command=folder)



def generate(self):
    """
    入力された値を元に画像生成をする。生成！ボタンの中身
    """
    HEIBOX.get() # HEIBOXの中身を取ってくる
    HEIGHT = int(HEIBOX.get()) # HEIBOXの中身をHEIGHTに入れる
    WIGBOX.get()
    WIGTH = int(WIGBOX.get())
    PAGEBOX.get()
    PAGE = int(PAGEBOX.get())
    TITLE = (TITBOX.get())

    PICTURE = np.zeros((HEIGHT, WIGTH, 3))
    PICTURE += 255

    # 指定したページの数だけ以下の処理を繰り返し、画像を生成する
    for i in range(1, PAGE+1):
        # パスも入力できるように
        FILE_NAME = PATH + "\\" + str(TITLE) + "_" + str(i) + ".png"
        cv2.imwrite(FILE_NAME, PICTURE)

def DeleteEntryValue(self):
    #エントリーの中身を削除
    HEIBOX.delete(0, tk.END)
    WIGBOX.delete(0, tk.END)
    PAGEBOX.delete(0, tk.END)
    TITBOX.delete(0, tk.END)

def _b5size(self): # 既に値が入ってる場合は高さ幅だけ消してB5のサイズを入れる
    """
    既に値が入ってる場合は高さ幅だけ消して、高さと幅のEntryにB5のサイズを入れる。
    B5サイズボタンの中身。
    """
    HEIBOX.delete(0, tk.END)
    HEIBOX.insert(tk.END, int(3541))
    WIGBOX.delete(0, tk.END)
    WIGBOX.insert(tk.END, int(2508))

###################################################################################

# GUI設定
FRM = tk.Tk()
FRM.geometry("300x250") # 横x縦
FRM.title("GUIだよ")

MENU = tk.Menu(FRM)
FILEMENU = tk.Menu(MENU, tearoff=0)
FILEMENU.add_command(label="フォルダを指定", command=folderselect)
FILEMENU.add_separator()
FILEMENU.add_command(label="second", command=second)
FILEMENU.add_command(label="third", command=third)
FILEMENU.add_command(label="four", command=four)
FILEMENU.add_command(label="終了(X)", command=FRM.quit)
MENU.add_cascade(label="ファイル", menu=FILEMENU)


# メイン部分設定
LABEL1 = tk.Label(text="このプログラムを置いたフォルダ内に、\nタイトルと連番付きのPNG画像が生成されます。")
LABEL1.pack()
LABEL3 = tk.Label(text="最初にどのフォルダに画像ファイルを生成するか選択してください")
LABEL3.pack()

var = tk.StringVar()
LABEL4 = tk.Label(FRM, textvariable=var)
LABEL4.pack()

lab_he = tk.Label(text="縦")
lab_he.grid
HEIBOX = tk.Entry()
HEIBOX.pack()
WIGBOX = tk.Entry()
WIGBOX.pack()
PAGEBOX = tk.Entry()
PAGEBOX.pack()
TITBOX = tk.Entry()
TITBOX.pack()


BTN1 = tk.Button(FRM, text="生成！")
BTN1.bind("<Button-1>", generate) # 左クリックで入力
BTN1.bind("<Button-3>", DeleteEntryValue) # 右クリックでEntry内を削除
BTN1.pack()

BTN2 = tk.Button(FRM, text="B5サイズ")
BTN2.bind("<Button-1>", _b5size) # 左クリックで入力
BTN2.pack()

BTN3 = tk.Button(FRM, text="保存")
BTN3.bind("<Button-1>", a)
BTN3.pack()

LABEL2 = tk.Label(text="左クリックで生成開始\n右クリックで入力内容の削除")
LABEL2.pack()

###################################################################################


FRM.config(menu=MENU)
FRM.mainloop()
