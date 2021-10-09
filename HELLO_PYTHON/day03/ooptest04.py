class Dog:
    def __init__(self):
        self.flag_bark = True
    def doMouseCover(self):
        self.flag_bark = False

class Bird:
    def __init__(self):
        self.fly_skill = 0
    def getOlder(self):
        self.fly_skill += 1

class GaeSae(Dog,Bird):
    def __init__(self):
        Dog.__init__(self)
        Bird.__init__(self)
    
if __name__ == '__main__':
    gs = GaeSae()
    print(gs.flag_bark)
    print(gs.fly_skill)
    gs.doMouseCover()
    gs.getOlder()
    print(gs.flag_bark)
    print(gs.fly_skill)
    