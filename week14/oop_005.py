#super() 함수

class Hero:
    def __init__(self):
        print('오버워치')
        self.name = '빈헬름'

class Reinhardt(Hero):
    def __init__(self):
        print('라인하르트')
        super().__init__()  #super는 부모클래스를 의미한다.
        print('이름은', self.name)
r = Reinhardt()
