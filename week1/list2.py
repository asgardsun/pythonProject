#list 02

#list 원소 삭제
subject = ['eng', 'python', 'java','C++']
print(subject)
#print(subject.remove('python')) -> 결과값 None
print(subject.pop(1)) #-> 결과값 python
print(subject)
# -> remove 함수는 바로 삭제를 하지만 pop 함수는 삭제하려고 하는 원소 값을 리턴 후 삭제

#list의 위치 출력
print(subject.index('java'))

#list 원소의 값 세기
subject.append('java')
subject.append('java')
print(subject.count('java'))

#in 키워드
print('python' in subject) # 결과값 False
print('java' in subject) # 결과값 True

#list 원소의 개수 리턴
print(len(subject))

#list를 문자열로 바꿔주는 함수 join()

subject_string  ='/'.join(subject)
print(subject_string)

#문자열을 list로 바꿔주는 함수 split()
subject_lists = subject_string.split('/')   #/라는 문자를 구분기호로 기준으로 잡는다.
print(subject_lists)

#list 원소 정렬
#subject.sort()  #오름차순 정렬 (사전순)
subject.sort(reverse=True) #내림차순 정렬 (사전순)
print(subject)

list_a =[2,3,1]
list_coppy = sorted(list_a) #원본 원소값들을 그대로 두고 복사본으로 정렬을 할때 : sorted
print(list_a)
print(list_coppy)

