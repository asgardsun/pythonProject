#리스트
#리스트는 특성 순서가 있는 항목의 모음
#대괄호와 쉼표 기호를 사용한다.

#리스트 생성
#ex1) empty_lists = []
#ex2) empty_lists = list()

empty_lists = list()
subjects = ['eng', 'python', 'java']
print(empty_lists)
print(subjects)
print(type(empty_lists))
print(type(subjects))

#리스트 인덱싱
print(subjects[1])
print(subjects[-2])

#리스트 추가, 삽입
subjects.append('C++')
subjects.insert(2, 'math')
print(subjects)

#리스트 원소 수정
subjects[3] = 'assembly'
print(subjects)

#리스트 원소 삭제
#del subjects[-1]
#subjects.pop()  #pop() 맨 뒤의 원소 삭제
#subjects.pop(1) #1번 인덱스에 있는 원소 삭제
subjects.remove('C++')  #원소 이름을 직접 작성 or 중복된 원소의 이름을 삭제
print(subjects)