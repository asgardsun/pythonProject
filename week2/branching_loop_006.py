#list comprehension

# numbers = []
# for k in range(0,10,2):
#     numbers.append(k * k)
# print(numbers)

# numbers = [k * k for k in range(0,10,2)]
# print(numbers)

##극장 매표관리 프로그램 v0.3
# ages = []
# price = 0
# kids = 0
# mids = 0
# adults = 0
# humans = int(input('관람객 : '))
# for i in range(humans):
#     ages.append(int(input('나이: ')))

# 리스트변수이름 = [표현식 for 반복변수명 in 순환코드]
# ages = [int(input('나이: ')) for i in range(humans)]
# for age in ages:
#     if 0 <= age < 8 :
#         price +=5000
#         kids +=1
#     elif 8 <= age < 19:
#         price +=9000
#         mids +=1
#     elif age >= 19:
#         price +=11000
#         adults +=1
#     else :
#         print('정확한 나이를 입력하세요')
# print("-"*40)
# print('총 인원 : {0}명 (어린이 : {1}, 청소년 : {2}, 성인 : {3})'.format(humans,kids,mids,adults))
# print('요금:{0}원'.format(price))

# n = [x for x in range(1,11) if x % 3 == 0]
# print(n)

# n = []
# for x in range(1,11) :
#     if x % 3 ==0:
#         n.append(x)
# print(n)at

# artists = ['악뮤', '빅뱅', '블사', '릴러말즈']
# copy_artists = [ artist for artist in artists if artist != '빅뱅']
# print(artists)
# print(copy_artists)



import random
#주사위
# dice = random.randint(1,6)
# print(dice)

lotto = []
while(len(lotto) < 6) :
    lotto.append(random.randint(1,45))
    lotto = list(set(lotto)) #set함수는 중복허용 불가.
print(sorted(lotto))
