#조건문
#조건에 따라 코드 실행여부를 결정하는 구문

#if True :   #True값에 1이나 22, -22가 들어가도 '항상 실행이' 출력된다. 하지만 if 0 : 을 입력하면 else 값이 출력된다.
#    print('항상 실행')
#else:
#    print('실행 될 일이 없음')

#age = int(input('나이가 어떻게 되세요?'))
#if int(age) >= 19:
#if age >= 19:
#    print('입장 가능합니다')
#else:
#    print('입장 불가합니다')

#논리연산자 (feat. 비교연산자)
# x = 5
# print(x<2 and x>1)
# print(x!=2 and x>1)
#
# print(not(x==2))

age = int(input('나이가 어떻게 되세요?'))
with_parents = input('보호자와 같이 오셨나요? 네/아니오')

if (age >= 15) or (with_parents == '네'):
    print("15세 이상 관람가 입장 가능")
else :
    print('입장 불가')