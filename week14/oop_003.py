#Interitance (상속)

class Animal:
    count = 0
    def __init__(self,name):
        self.name = name
        Animal.count +=1
    def move(self):
        print('이동합니다.')

    def speak(self):
        pass

    #클래스 메서드 선언을위해 데커레이터
    @classmethod
    def animals(cls):
        print('집에서 키우는 동물은 총 {0}마리 입니다.'.format(Animal.count))

class Kitten(Animal):
    def speak(self):
        print('야옹')

class Puppy(Animal):
    def speak(self):
        print('멍멍')
d1 = Puppy("쫑")
k1 = Kitten("나비")
print(Animal.animals())

print(k1.name + "가",end=' ')
k1.move()
k1.speak()

print(d1.name + "이",end=' ')
d1.move()
