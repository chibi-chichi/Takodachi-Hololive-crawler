from tkinter import *
from tkinter import messagebox
from tkinter import ttk
import channel_info as ch

'''
넣을 기능

1. 홀로라이브 유툽 라이브 스트리밍 크롤링
2. 홀로라이브 키리누키 채널에서 크롤링
3. 홀로라이브 공식 채널에서 노래 아카이브 크롤링
3-1. 캐릭터별 분류 (졸업생 제외)

4. 언어 변경 KR / EN / JP

5. 홀로라이브 공식 트윗 크롤링
'''


# 언어 변경 기능
def language_change():
    messagebox.showinfo("언어 변경", "언어 변경을 하고 싶다.")


count = 0


def count_up(button):
    global count
    count += 1
    button.config(text=str(count))


# 와! 기존 프레임에서 새로운 프레임 띄우기! 이런게 있네
# https://www.delftstack.com/ko/howto/python-tkinter/how-to-switch-frames-in-tkinter/
class TakoDachiApp(Tk):
    def __init__(self):
        Tk.__init__(self)
        self.title("TAKODACHI")
        # 초기 화면 크기 설정 (1280X720)
        self.geometry("1280x720")
        # 창 크기 조절 (X축, Y축)
        self.resizable(False, False)
        self._frame = None
        self.switch_frame(StartPage)

    # 프레임 스위치 기능 (기존의 프레임을 지우고 새 프레임을 생성)
    def switch_frame(self, frame_class):
        new_frame = frame_class(self)
        if self._frame is not None:
            self._frame.destroy()
        self._frame = new_frame
        self._frame.pack()


# 처음 실행 페이지
class StartPage(Frame):
    def __init__(self, master):
        Frame.__init__(self, master)
        Label(self, text="Start page", font=('Helvetica', 18, "bold")).pack(side="top", fill="x", pady=5)
        Button(self, text="Go to page one",
               command=lambda: master.switch_frame(PageOne)).pack()
        Button(self, text="Go to page two",
               command=lambda: master.switch_frame(PageTwo)).pack()
        Button(self, text="Go to page three",
               command=lambda: master.switch_frame(PageThree)).pack()


# 타코다치 페이지
class PageOne(Frame):
    def __init__(self, master):
        Frame.__init__(self, master)
        Frame.configure(self, bg='blue')
        Label(self, text="타코 페이지 입니다!", font=('Helvetica', 18, "bold")).pack(side="top", fill="x", pady=5)
        Button(self, text="Go back to start page",
               command=lambda: master.switch_frame(StartPage)).pack()


# 스이쨩 페이지
class PageTwo(Frame):
    def __init__(self, master):
        Frame.__init__(self, master)
        Frame.configure(self, bg='red')
        Label(self, text="스이쨩 페이지 입니다!", font=('Helvetica', 18, "bold")).pack(side="top", fill="x", pady=5)
        Button(self, text="Go back to start page",
               command=lambda: master.switch_frame(StartPage)).pack()


# 칼리 페이지
class PageThree(Frame):
    def __init__(self, master):
        Frame.__init__(self, master)
        Frame.configure(self, bg='green')
        Label(self, text="칼리 페이지 입니다!", font=('Helvetica', 18, "bold")).pack(side="top", fill="x", pady=5)
        Button(self, text="Go back to start page",
               command=lambda: master.switch_frame(StartPage)).pack()


# 프로그램이 종료될 때 까지 실행
if __name__ == "__main__":
    app = TakoDachiApp()
    app.mainloop()
