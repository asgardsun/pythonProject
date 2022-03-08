#while

# k = 1
# while k<6:
#     print(k, end=' ')
#     k = k + 1

#FizzBuzz
#001 while
# n = 1
# while n <101 :
#     output = n
#     if(n%3 == 0) and (n%5 ==0):
#         print('FizzBuzz!')
#     elif n%3 == 0:
#         print('Fizz')
#     elif n%5 == 0:
#         print('Buzz')
#     else:
#         print(n)
#     n = n + 1

#002 for
# for n in range(1,101) :
#     output = n
#     if(n%3 == 0) and (n%5 ==0):
#         print('FizzBuzz!')
#     elif n%3 == 0:
#         print('Fizz')
#     elif n%5 == 0:
#         print('Buzz')
#     else:
#         print(n)
#     n = n + 1

# while True:
#     answer = input('런던, 파리, 서울 중 영국의 수도는?')
#     if answer == '런던':
#         print('정답입니다.')
#         break
#     elif answer == '파리':
#         print('파리는 프랑스의 수도인데용?')
#     elif answer == '서울':
#         print('서울은 한국의 수도인데용?')
#     else:
#         print('보기에서 골라라')

count = 0
while count < 6:
    count +=1
    if count ==3:
        continue # 반복의 처음으로 돌아가는 키워드
    print(count)