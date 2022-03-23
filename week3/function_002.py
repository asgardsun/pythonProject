#함수 (Function cont)

#factorial

def factorial_recursion(n):
    """
    팩토리얼 by 재귀
    f(n) = n * n-1 * n-2 * n-3...
    f(3) = 3 * f(2)
         = 3 * 2 * f(1)
         = 3 * 2 * 1 * f(0)         ->f(0)은 reutrun 1이 된다.
    """
    if n == 0:
        return 1
    else:
        return n * factorial_loop(n-1)
def factorial_loop(n):
    """
    팩토리얼 by 반복문
    """
    result =1
    for i in range(1, n+1):
        result = result * i
    return result
print(factorial_loop(4))
print(factorial_loop(5))


