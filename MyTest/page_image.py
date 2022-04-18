

import tkinter as tk
from tkinter import messagebox
# from tkinter import ttk

#전역변수
photos = ['image/michael.PNG','image/franklin.PNG','image/trevor.PNG']

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

def click_pick(ev):
    messagebox.askokcancel("클릭", "챔피언을 선택하시겠습니까?")
    messagebox.showerror("showerror")
    # for value in character.keys():
    #     lbl_display.configure(text='{0}을 선택하셨습니다.'.format(value))
    if photos[idx]==photos[0]:
        lbl_display.configure(text='michael을 선택하셨습니다.')
        print('{0}을 선택하셨습니다.'.format(photos[idx]), file=fp)
    elif photos[idx]==photos[1]:
        lbl_display.configure(text='franklin 선택하셨습니다.')
        print('{0}을 선택하셨습니다.'.format(photos[idx]), file=fp)
    elif photos[idx]==photos[2]:
        lbl_display.configure(text='trevor 선택하셨습니다.')
        print('{0}을 선택하셨습니다.'.format(photos[idx]), file=fp)


#파일
fp = open('log.txt','a')   #파일 불러오기
print('\n', '-' * 20, file=fp)  #선으로 구분
fp.close()  #log.txt 파일 close

if __name__ == '__main__':
    w = tk.Tk()
    w.title('포토뷰어 v0.1')
    w.geometry('400x600')

    w.bind('<Left>',pg_up) #왼쪽 방향키를 입력했을때 이전
    w.bind('<Right>',pg_dw) #오른 d키를 입력했을때 다음

    # w.bind('<a>',pg_up) #이전 a키를 입력했을때 이전
    # w.bind('<b>',pg_dw) #이전 d키를 입력했을쪽



    p1 = tk.PhotoImage(file='image/michael.PNG')
    lbl_display = tk.Label(w,text='챔피언을 선택해주세요', font=("돋움체",20))
    lbl_result  = tk.Label(w,text='')   #챔피언 결과창
    lbl_photo = tk.Label(w, image=p1)
    lbl_page = tk.Label(w, text=f'{idx+1}/{len(photos)} ')
    btn_next = tk.Button(w, text="다음==>",command=click_next, fg='gray',bg='gray')
    btn_prev = tk.Button(w, text="<==이전",command=click_prev,fg='gray',bg='gray')

    #lbl_photo.bind('<Button 1>',click_photo)    #마우스 왼쪽 버튼을 누를때
    lbl_photo.bind('<Button>',click_pick)

    # lbl_photo.grid(row=0, column=0, columnspan=3)
    # btn_next.grid(row=1,column=2,sticky=tk.W)
    # lbl_page.grid(row=1,column=1)
    # btn_prev.grid(row=1,column=0,sticky=tk.E)
    lbl_display.grid(row=0, column=1)
    lbl_photo.grid(row=1, column=0, columnspan=3)
    btn_next.grid(row=2,column=2,sticky=tk.W)   #다음 페이지
    lbl_page.grid(row=2,column=1)
    btn_prev.grid(row=2,column=0,sticky=tk.E)   #이전 페이지
    lbl_result.grid(row=3, column=1)        #챔피언 결과창
    fp = open('log.txt', 'a')  # log 파일 append로 불러오기

    w.mainloop()

    fp.close()


