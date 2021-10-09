class Animal:
    def __init__(self):
        self.age = 1
        print("Animal:__init__")

    def getOlder(self):
        self.age += 1
        
    def __del__(self):
        print("Animal:__del__")
        
# if __name__ == '__main__':
#     a = Animal()
#     print(a.age)
#
#     a.getOlder()
#     print(a.age)
#     print()

class Human(Animal) :
    def __init__(self):
        super().__init__()
        self.logical = 0
        print("Human:__init__")

    def goDdit(self):
        self.logical += 100
        
    def __del__(self):
        print("Human:__del__")
        
 
if __name__ == '__main__':
    h = Human()
    print(h.age)
    print(h.logical)
    h.getOlder()
    h.goDdit()
    print(h.age)
    print(h.logical)