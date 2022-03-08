#조건문 count.

# age = int(input('나이 : '))
#
# if 0 <= age < 8 :
#     print('어린이 요금 : 5000원')
# elif 8< age < 19:
#     print('청소년 요금 : 9000원')
# elif age >= 19:
#     print('성인 요금 : 11000원')
# else :
#     print('정확한 나이를 입력하세요')

# age = int(input('나이 : '))
# price = 0
#
# if 0 <= age < 8 :
#     price = 5000
# elif 8< age < 19:
#     price = 9000
# elif age >= 19:
#     price = 11000
# else :
#     print('정확한 나이를 입력하세요')
#
# print('요금은 ' + str(price) + '원 입니다')

#002
# options = ['콜라', '치즈토핑', '버섯', '치즈크러스터']
# if '버섯' in options:
#     print('버섯 추가합니다')
# elif '페페로니' in options:
#     print('페페로니를 추가합니다.')
# elif '치즈토핑' in options:
#     print('치즈토핑을 추가합니다.')
#
# print('\n피자 주문이 완료되었습니다.')

#반복문 003
for i in range(5) : #인수가 하나 일때는 시작 값은 0부터 시작 5전까지
    print(i, end=' ')
print() #줄 바꿈용
for j in range(2,5): #2는 시작 값
    print(j, end=' ')
print()
for k in range(1,5,2): #1은 시작 값, 5는 끝값, 2는 증감(step)
    print(k, end=' ')
