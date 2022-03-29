#exception handling

# a = input()
# b = input()
#
# if a.isdigit() and b.isdigit():
#     print(int(a+b))
# else:
#     print(a+b)

#try:
#예외가 발생할 가능성이 있는 코드
#except:
#예외가 발생했을 때 실행할 코드
#else:
#예외가 발생하지 않았을때 실행할 코드
#finally
#무조건 실행
try:
    c = list()
    c.append('사과')
    a = int(input())
    b = int(input())
    print(a/b)
    print(c[0])
except ZeroDivisionError:
    print('분모에 0이 올 수 없습니다.')
except ValueError:
    print('입력된 수는 정수가 아닙니다.')
except IndexError:
    print('리스트 인덱스 에러가 발생했습니다.')
except:
    print('무언가 에러가 발생했습니다.')
else:
    print('정상적으로 처리')
finally:
    print('예외 발생 여부에 상관없이 항상 실행')