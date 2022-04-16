

import tkinter as tk
# from tkinter import ttk
def popup():
    if selected.get() == 0:
        lbl_display.configure(image=p1)
    elif selected.get() == 1:
        lbl_display.configure(image=p2)
    else:
        lbl_display.configure(image=p3)

w = tk.Tk()
w.title('라디오 버튼 실습')
w.geometry('500x700')


p1 = tk.PhotoImage(file='michael.PNG')
p2 = tk.PhotoImage(file='franklin.PNG')
p3 = tk.PhotoImage(file='trevor.PNG')

selected = tk.IntVar()
rb_1 = tk.Radiobutton(w,text='마이클',command=popup, variable=selected, value=0)
rb_2 = tk.Radiobutton(w,text='프랭클',command=popup, variable=selected, value=1)
rb_3 = tk.Radiobutton(w,text='트레버',command=popup, variable=selected, value=2)

lbl_display = tk.Label(w,text='선택할 플레이어는? ')
lbl_display.configure(image=p1)


#lbl_display.pack()
# rb_1.pack()
# rb_2.pack()
# rb_3.pack()
rb_1.grid(row=0,column=0)
rb_2.grid(row=0,column=1)
rb_3.grid(row=0,column=2)
lbl_display.grid(row=1, column=0, columnspan=3)

w.mainloop()

