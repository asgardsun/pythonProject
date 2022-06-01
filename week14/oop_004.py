#Duck typing

class Cat:
    def sound(self):
        print("냐옹")

class Dog:
    def sound(self):
        print("멍멍")
    def test(self):
        print("저는 멍멍인데요?")

# d = Dog()
# c = Cat()
#
# animals = [d,c]
#
# for animal in animals:
#     animal.sound()

#private 변수
class Diva:
    def __init__(self,name="디바"):
        # self.name = name
        self.__name = name  #private 멤버 변수 선언

    def getName(self):
        return self.__name

    def setName(self,in_name):
        self.__name = in_name


d1 = Diva()
d2 = Diva('송하나')

print(d1.getName())
d1.setName('박하나')
print(d2.getName())
print(d1.getName())
