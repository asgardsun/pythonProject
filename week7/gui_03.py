
#
# w = tk.Tk()
# w.title('세 번째 GUI 프로그램')
#
# #이미지 준비
# p1 = tk.PhotoImage(file='michael.PNG')
# p2 = tk.PhotoImage(file='franklin.PNG')
# p3 = tk.PhotoImage(file='trevor.PNG')
#
# #레이블 및 버튼에 사용할 이미지 바인딩
# lbl_disp1 = tk.Label(w,image=p1)
# lbl_disp2 = tk.Label(w,image=p2)
# btn_disp3 = tk.Button(w,image=p3)
#
# #위젯 배치
# lbl_disp1.pack(side='left')
# lbl_disp2.pack(side='left')
# btn_disp3.pack()
#
# w.mainloop()
#

import tkinter as tk
from tkinter import messagebox
# from tkinter import ttk
def popup():
    #messagebox.askokcancel("클릭","버튼이 눌렸습니다.")
    #messagebox.showerror("클릭")
    #messagebox.showInfo("클릭","버튼일 눌렸습니다.")
    if checked.get() ==0:
        lbl_display.configure(text="체크버튼 off")
        messagebox.showinfo("언체크됨","체크버튼 OFF")
    elif checked.get() == 1:
        lbl_display.configure(text="체크버튼 on")
        messagebox.showinfo("언체크됨","체크버튼 ON")
    else:
        messagebox.showerror("오류","실행될 일 없음")



# w = tk.Tk()
# w.title('세 번째 GUI 프로그램')
#
# #이미지 준비
# p1 = tk.PhotoImage(file='michael.PNG')
# p2 = tk.PhotoImage(file='franklin.PNG')
# p3 = tk.PhotoImage(file='trevor.PNG')
#
# #레이블 및 버튼에 사용할 이미지 바인딩
# lbl_disp1 = tk.Label(w,image=p1)
# lbl_disp2 = tk.Label(w,image=p2)
# btn_disp3 = tk.Button(w,image=p3, command=popup)
#
# #위젯 배치
# lbl_disp1.pack(side='left')
# lbl_disp2.pack(side='left')
# btn_disp3.pack()



w = tk.Tk()
w.title('체크버튼 실습')
w.geometry('300x400')
#checked = 0  -> 기본정수이며 , get()함수 등을 사용할 수 없다.
#checked = tk.IntVar()       ##IntVar()은 Java의 Integer와 같은 클랙스 객체 개념이다. tk.DoubleVar(), tk.BooleanVar(), tk.StringVar()이 있다.
checked = tk.BooleanVar()   #논리형 변수 객체 지정

cb_an_off = tk.Checkbutton(w, text='출석체크', variable=checked, command=popup)
lbl_display = tk.Label(w,text='')

cb_an_off.pack()
lbl_display.pack()

w.mainloop()

