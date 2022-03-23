#dictionary

#리스트와 비슷하나 순서를 따지지 않는다.
#키와 값이 pair가 원소가 된다.

# fruits = {'apple' : '사과', 'watermelon' : '수박'}
# print(fruits['watermelon'])
# print(fruits)
# fruits['kiwi'] = '키위'   #삽입 or 수정
# print(fruits)


#list에 dictionary 넣기
# test1 = [['python',3], ['english',2], ['dance',1]]
# print(test1[1][0])
# print(dict(test1))
#
# test2 = ['ab','cd','ef']
# print(test2[1][0])
# print(dict(test2))

#update()
fruits = {'apple' : '사과', 'watermelon' : '수박'}
fruits['banana'] = '바나나'

others = {'strawberry' : '딸기', 'kiwi' : '키위'}
fruits.update(others)
print(fruits)

#del
del fruits['apple'] #지정한곳 삭제 (원소 한개 삭제)
print(fruits)
fruits.clear()  #clear : 모든 원소들 삭제
print(fruits)


