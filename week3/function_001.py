#함수 (Function)
#한 가지 작업을 수행하도록 디자인된 코드 블럭 or 코드의 집합
#
# def test(name) :
#     print("hi " + name)
#     return "이름을 출력함"
#
# test('파이썬')
# print((test('C++')))
#
# def minus(a, b):
#     """
#     두 수의 차를 구하는 함수
#     """
#     return a - b
#
# print(minus(8,3))
# help(minus)

#가변 매개변수 : *values 뒤에 변수 하나가 올수 없으며, *test같은 또다른 가변 매개변수는 올 수없다.
# def print_even(times, *values):
#     for value in values:
#         print(times * value)
#
# print_even(2, -9, 11, 7, 100 ,6)


#기본 매개변수
def print_default(value, times=3): #default 값이 3이지만  print_even(5,2)로 하면 times는 2로 변경된다.
        print(times * value)
print_default(5,2)