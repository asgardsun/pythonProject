#극장 매표관리 프로그램 v0.1
# ages = []
# price = 0
# humans = int(input('관람객 : '))
# for i in range(humans):
#     ages.append(int(input('나이: ')))
#
# for age in ages:
#     if 0 <= age < 8 :
#         price +=5000
#     elif 8< age < 19:
#         price +=9000
#     elif age >= 19:
#         price +=11000
#     else :
#         print('정확한 나이를 입력하세요')
# print('요금은 ' + str(price) + '원 입니다')


##극장 매표관리 프로그램 v0.2
ages = []
price = 0
kids = 0
mids = 0
adults = 0
humans = int(input('관람객 : '))
for i in range(humans):
    ages.append(int(input('나이: ')))

for age in ages:
    if 0 <= age < 8 :
        price +=5000
        kids +=1
    elif 8 <= age < 19:
        price +=9000
        mids +=1
    elif age >= 19:
        price +=11000
        adults +=1
    else :
        print('정확한 나이를 입력하세요')
print("-"*40)
#print('총 인원 : '+ str(humans) + '명')
#print('어린이 : '+ str(kids) + '명', '청소년 : ' + str(mids) +'명' ,'성인 : ' + str(adults)+ '명')
# print('요금 :' + str(price) + '원')

print('총 인원 : {0}명 (어린이 : {1}, 청소년 : {2}, 성인 : {3})'.format(humans,kids,mids,adults))
print('요금:{0}원'.format(price)) #price 값을 {0}에 대입
#print('요금 : %d원' % price)
