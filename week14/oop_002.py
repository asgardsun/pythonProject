#OOP Part 1
#Class & Object

#메서드(함수), 속성(멤버변수)

class Puppy:
    #특수 메서드 -> 생성자 메서드
    def __init__(self,name, age):
        """ 강아지의 이름과 나이를 초기화"""
        self.name = name #멤버변수
        self.age = age

    #메서드
    def wait(self):
        """강아지 대기 시키기"""
        print(self.name + " 기다려!")
        """강아지 앉아"""
    def sit(self):
        print('{0} 앉아!!'.format(self.name))

    #get, set 메서드
    def set_age(self,n):
        self.age =n

    def get_age(self):
        return self.age


#객체 생성
p1 = Puppy('zzong',2)
p2 = Puppy('happy',1)

print('{0}의 나이는 {1}입니다.'.format(p1.name, p1.age))
print('{0}의 나이는 {1}입니다.'.format(p2.name, p2.age))

# p2.wait()
# p2.sit()

#메서드를 통해 값 바꾸기
p1.set_age(3)
p2.set_age(2)

print('{0}의 나이는 {1}입니다.'.format(p1.name, p1.get_age()))
print('{0}의 나이는 {1}입니다.'.format(p2.name, p2.get_age()))