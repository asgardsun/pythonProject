

import tkinter as tk
from tkinter import messagebox
# from tkinter import ttk

#전역변수
photos = ['michael.PNG','franklin.PNG','trevor.PNG']
idx = 0


def click_next():
    global idx  #idx를 전역변수로 잡아준다
    idx +=1
    if idx>len(photos)-1:
        idx=0
    p1 = tk.PhotoImage(file=photos[idx])
    lbl_page.configure(text=f'{idx+1}/{len(photos)} ')
    lbl_photo.configure(image=p1)
    lbl_photo.image = p1

def click_prev():
    global idx  # idx를 전역변수로 잡아준다
    idx -= 1
    if idx <0 :
        idx = len(photos)-1
    p1 = tk.PhotoImage(file=photos[idx])
    lbl_page.configure(text=f'{idx+1}/{len(photos)} ')
    lbl_photo.configure(image=p1)
    lbl_photo.image = p1

def pg_dw(ev):
    click_next()
def pg_up(ev):
    click_prev()

def click_photo(ev):
    messagebox.showinfo("좌표", f'({ev.x}, {ev.y})')

w = tk.Tk()
w.title('포토뷰어 v0.1')
w.geometry('500x700')

w.bind('<a>',pg_up) #이전 a키를 입력했을때 이전
w.bind('<d>',pg_dw) #이전 d키를 입력했을때 다음



p1 = tk.PhotoImage(file='michael.PNG')
lbl_photo = tk.Label(w, image=p1)
lbl_page = tk.Label(w, text=f'{idx+1}/{len(photos)} ')
btn_next = tk.Button(w, text="다음==>",command=click_next)
btn_prev = tk.Button(w, text="<==이전",command=click_prev)

lbl_photo.bind('<Button 1>',click_photo)

lbl_photo.grid(row=0, column=0, columnspan=3)
btn_next.grid(row=1,column=2,sticky=tk.W)
lbl_page.grid(row=1,column=1)
btn_prev.grid(row=1,column=0,sticky=tk.E)


w.mainloop()

