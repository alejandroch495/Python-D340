# Alejandro Chavez
# Chapter 9 extra credit
# Bug class

class Bug:
    pos = 0
    dir = 1
    def __init__(self,init_pos = 0):
        "Create bug at a position"
        self.pos = init_pos
        print(f'Initial position: {self.pos}')

    def move(self):
        "Move bug once"
        self.pos += self.dir
    
    def turn(self):
        "Turn bug"
        self.dir = -self.dir
    
    def getPosition(self):
        "Get position of bug"
        print(self.pos)

def main():
    # First bug
    # Expected end pos 9
    bug1 = Bug(10)
    bug1.move()
    bug1.move()
    bug1.turn()
    bug1.move()
    bug1.move()
    bug1.move()
    bug1.getPosition()

    # Second bug
    # Expected end pos -9
    bug2 = Bug()
    bug2.move()
    bug2.turn()
    bug2.move()
    bug2.move()
    bug2.move()
    bug2.move()
    bug2.move()
    bug2.move()
    bug2.move()
    bug2.move()
    bug2.move()
    bug2.move()
    bug2.move()
    bug2.move()
    bug2.move()
    bug2.move()
    bug2.turn()
    bug2.move()
    bug2.move()
    bug2.move()
    bug2.move()
    bug2.getPosition()

if __name__ == "__main__":
    main()



"""
Output
Bug 1
Initial position: 10
9

Bug 2
Initial position: 0
-9
"""