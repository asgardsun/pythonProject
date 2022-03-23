#dictionary (cont)

#update
# fruits = {'apple' : '사과',
#           'watermelon' : '수박',
#           'strawberry' : '딸기',
#           'kiwi' : '키위',
#           'banana' : '바나나'}
# #keys
# print(fruits.keys())
#
# #values
# print(fruits.values())
# print(fruits.items())

# #반복문을 통한 dictionary 출력
# for k in fruits.values() :
#     print(k)
#
# for k in fruits:    #keys 값이 출력
#     print(k)


#음식 추천 프로그램 0.1
# alcohol_foods = {'맥주' : '치킨',
#                '와인' : '치즈',
#                '고량주': '짬뽕',
#                '소주' : '골뱅이소면'}
# alchol = input('주문하실 술(맥주/와인/소주/고량주)은? ')
#
# if alchol in alcohol_foods.keys():
#     print('{0}에 어울리는 안주는 {1}입니다.'.format(alchol, alcohol_foods[alchol]))

#음식 추천 프로그램 0.2
# alcohol_foods = {'맥주' : '치킨',
#                '와인' : '치즈',
#                '고량주': '짬뽕',
#                '소주' : '골뱅이소면'}
# while True:
#     alchol = input('주문하실 술(맥주/와인/소주/고량주/결제)은? ')
#     if alchol == '결제' :
#         break
#     if alchol in alcohol_foods.keys():
#         print('{0}에 어울리는 안주는 {1}입니다.'.format(alchol, alcohol_foods[alchol]))
#     else :
#         print('{0}는 판매하지 않습니다. 메뉴에서 골라주세요~'.format(alchol))

#안주 추천 프로그램 0.3
# import random
#
# alcohol_foods = {'맥주' : '치킨',
#                '와인' : '치즈',
#                '고량주': '짬뽕',
#                '소주' : '골뱅이소면'}
# while True:
#     alchol = input('주문하실 술(맥주/와인/소주/고량주/랜덤/결제)은? ')
#     if alchol == '결제' :
#         break
#     if alchol in alcohol_foods.keys():
#         print('{0}에 어울리는 안주는 {1}입니다.'.format(alchol, alcohol_foods[alchol]))
#     elif alchol == '랜덤' :
#         print(random.choice(list(alcohol_foods)))
#     else :
#         print('{0}는 판매하지 않습니다. 메뉴에서 골라주세요~'.format(alchol))

alcohol_foods = {'맥주' : '치킨',
               '와인' : '치즈',
               '고량주': '짬뽕',
               '소주' : '골뱅이소면'}
#copy()
copy_alcohol = alcohol_foods.copy()
copy_alcohol['소주'] = '두부김치'
print(copy_alcohol)
print(alcohol_foods)



