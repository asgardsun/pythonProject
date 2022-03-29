#file io

#파일 객체 = open(파일경로 , 읽기 모드)
#w : 쓰기 , r : 읽기, a : 이어쓰기
#파일을 닫을때 파일객체.close()

#파일쓰기
fp = open('war_flower.txt','w')
print('고니',file=fp) #실제 쓰기
print('정마담',file=fp)
print('아귀',file=fp)
fp.write('너부리')
fp.close()

#파일읽기
fp = open('wf.txt','r')
lines = fp.readlines()  #파일을 1행 단위의 리스트 원소로 리턴
#print(lines)
for line in lines:
    #print(line.rstrip('\n'))    #줄바꿈 제거
    print(line[0:-1])

#with
with open('wf.txt') as fp:
    lines = fp.readlines()  #파일을 1행 단위의 리스트 원소로 리턴
    for line in lines:
        print(line[:-1])
# for line in fp:
#     print(line,end='')

fp.close()