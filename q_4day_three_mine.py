class Card:
    def __init__(self,num,next):
        self.num = num
        self.next = next

class CardStack:
    def __init__(self):
        # self.bottom = None
        self.top = None

    def push(self,num):
        numValue = num
        numMinus = num-1
        for _ in range(num-1):
            self.last = Card(numValue-numMinus,self.last)
            numMinus += -1




a1 = CardStack()
a1.push(6)
# for _ in range(5):
#     next = a1.last
#     string = ""
