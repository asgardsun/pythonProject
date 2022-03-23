#tuple
#immutable(불변) -> 상수의 리스트라고 할 수 있다.
#튜플의 원소를 정의한 후에는 insert, update, delete 불가

subjects = ('python', 'c++', 'english', 'math') #packing
for subject in subjects :
    print(subject)

kim, han, tom, lee = subjects #unpacking
print(kim, tom , han)

a = input()
b = input()
# t = b
# b = a
# a = t
a, b = b, a #packing과 unpacking을 동시에 수행
print(a, b)