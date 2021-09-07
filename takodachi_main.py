from tkinter import *
from tkinter import messagebox
from tkinter import ttk

win = Tk()
win.title("TAKODACHI")

'''
넣을 기능

1. 홀로라이브 유툽 라이브 스트리밍 크롤링
2. 홀로라이브 키리누키 채널에서 크롤링
3. 홀로라이브 공식 채널에서 노래 아카이브 크롤링
3-1. 캐릭터별 분류 (졸업생 제외)

4. 언어 변경 KR / EN / JP

5. 홀로라이브 공식 트윗 크롤링
'''

config = Menu(win)
win.config(menu=config)

def language_change():
    messagebox.showinfo("언어 변경","언어 변경을 하고 싶다.")

config_menu = Menu(config)
config.add_cascade(label="설정", menu = config_menu)
config_menu.add_command(label="언어 변경", command=language_change)
config_menu.add_separator()

config_menu.add_command(label="선호 캐릭터")

win.mainloop()