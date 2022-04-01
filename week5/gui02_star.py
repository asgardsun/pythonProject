import tkinter as tk

def star():
    n = int(en_input.get())
    texts= ''
    for i in range(1,n+1):
        for j in range(n-i,0,-1):
            texts = texts + ' '
        for star in range(1,2*i):
            texts = texts + '*'
        texts = texts + '\n'
    lbl_temp.configure(text=texts)

if __name__ == '__main__':
    w = tk.Tk()
    w.title('세번째 GUI 프로그램')
    w.geometry('300x400')

    #생성자
    en_input = tk.Entry(w)
    btn_star = tk.Button(w, text='star',command=star)
    lbl_temp = tk.Label(w, text='별찍기 프로그램')


    en_input.pack()
    btn_star.pack()
    lbl_temp.pack()
    w.mainloop()
