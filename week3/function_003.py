#함수 (Function cont.)

#fibonacci
#성능 상의 문제가 있다. - > 해결방법 중 하나는 메모화
def fibo_recursion(n):
    """
    피보나치 수열
    f(1) = 1
    f(2) = 1
    f(n) = f(n-1) + f(n-2)
    f(3) = f(2) + f(1)
         = 1 + 1
    f(4) = f(3) + f(2)
    """

    if n==1 :
        return 1
    if n==2 :
        return 1
    else:
        return fibo_recursion(n-1) + fibo_recursion(n-2)

# for k in range(1,8):
#     print('피보나치 {0}: {1}'.format(k,fibo_recursion(k)))

#함수의 매개변수로 함수 전달하기
# def print_hi(hi):
#     for k in range(5):
#         hi()
#
# def hi():
#     print('hello~')
#
# print_hi(hi)


#map(함수, 순환가능한 자료구조)
#순환 가능한 자료구조 : 리스트, 딕셔너리, 문자열, range

def square(n):
    return n*n

def odd(n):
    return n % 2 == 1

result = []
for k in range(1,6):
    result.append(square(k))
print(result)

#print(list(map(square, [1,2,3,4,5])))


#filter(함수, 순환 가능한 자료구조)
print(list(filter(odd, [1,2,3,4,5])))