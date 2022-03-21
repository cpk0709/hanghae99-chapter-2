# def change(money) -> int:
#     cnt = 0
#
#     coin_types = [500,100,50,10]
#
#     for coin in coin_types:
#
#         cnt += money // coin
#         money %= coin
#
#     return cnt
#
#
# result = change(1260)
# print(result)

#####

# arr = [1,2,3]
#
# for i in range(2,len(arr)):
#     print(arr[i])

class MyQueue:
    def __init__(self):
        self.input = []
        self.output = []

    def push(self, x):
        self.input.append(x)

    def pop(self):
        self.peek()
        return self.output.pop()

    def peek(self):
        # output이 없으면 모두 재입력
        if not self.output:
            while self.input:
                self.output.append(self.input.pop())
        return self.output[-1]

    def empty(self):
        return self.input == [] and self.output == []


test = MyQueue()

test.push(1)
test.push(2)
test.push(3)
test.push(4)

print(test.pop())

