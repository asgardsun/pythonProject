#반복문 count
#for 변수 in range(변수 시작값, 끝값, 증감값)

#짝수 출력
# for n in range(2,11,2) :
#     print(n)

# for n in range(1,11):
#     if n % 2 ==0:
#         print(n)

#step에 감소식으로 인한 짝수출력
# for n in range(10, 1, -2):
#     print(n)

#문자열의 문자 출력
# words = 'I love python'
# for word in words :
#     print(word)

#리스트 원소 출력
#1 제일 파이썬스러운 문법
words = ['I', 'love', 'python']
for word in words:
    print(word, end=' ')
print()

#2
#for i in range(0,3,1):
for i in range(len(words)):     #어느 구간을 따로 출력을 할때에 표현한다
    print(words[i], end =' ')
