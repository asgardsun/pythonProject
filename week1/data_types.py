#자료형
#문자열 함수
words = 'Life is too short, \n You need \t Python'
temp1 = words.title()   #각 단어의 첫 글자를 대문자로
temp2 = words.lower()   #모두 소문자로
temp3 = words.upper()   #모두 대문자로
print(temp1)

#strip() -> 공백제거, 불필요한 문자 삭제
trim1 = 'python'
trim2 = '&&python@&&'
print(trim1, end= '**') #줄 바꿈 없이 연결 해주는것 end
print(trim2.strip('&'))

#str()
print('1' + "hi")
print(str(1) + "hi")

#int()
a = '1'
b = 2
print(int(a) + b)
print(a + str(b))
