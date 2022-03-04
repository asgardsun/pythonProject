my_utube = ['악뮤', '볼빨사', '언더독', '피식대학', '빅뱅','제니']
ur_utube = my_utube[0:5]   #인덱스 0번부터 5번전까지
print(ur_utube)
del my_utube[-1]
print(my_utube)



a = [2,3,1,5]
#b = a -> #b와 같은 값을 가진다. 친구와 같은 사물함을 쓰는 개념으로 생각하면 됨.
#b = a[0:] #슬라이싱 -> 0은 시작 인덱스이며 :뒤에 빈칸은 끝까지 라는 의미
#b = a.copy()
b = list(a)
print('b : ', b)
b[-2] = 4
print('b: ',b)
print('a: ',a)
print(id(a), id(b))