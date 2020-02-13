#sample59.py


class bird:
    def fly(self):
        raise NotImplementedError
        pass
    pass

# BIRD = bird()
# BIRD.fly()

#---------------------------------------#
class littlebird(bird):
    def fly(self):
        print('flying....') #OOP의 polymorphism
        pass
    pass #end class


BIRD = littlebird()
BIRD.fly()