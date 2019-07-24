import queue
import random


class myQueue:
    def __init__(self):
        self.que = []
        self.qsize = len(self.que)

    def put(self, x):
        self.que.append(x)

    def get(self):
        self.qsize = len(self.que)
        if self.qsize != 0:
            t = self.que[0]
            self.que.pop(0)
            return t
        else:
            print('The queue is empty!')

    def top(self):
        return self.que[0]

    def qempty(self):
        if self.qsize == 0:
            return True
        else:
            return False

    def dele(self):
        self.que.clear()


def funMyQueue(n):
    que = [0 for i in range(n)]
    front, rear = 0, 0
    for i in range(n):
        x = random.randint(1, 100)
        print(x)
        que[i] = x
        rear += 1
    print('------')
    while front - rear < 0:
        g = que[front]
        print(g)
        front += 1


def itqueue(n):
    que = queue.Queue()
    for i in range(n):
        x = random.randint(1, 100)
        print(x)
        que.put(x)
    print('------')
    while que.qsize() != 0:
        g = que.get()
        print(g)


def main():
    que = myQueue()
    for i in range(8):
        x = random.randint(1, 100)
        print(x)
        que.put(x)
    print('------')
    print(que.top())
    for i in range(10):
        print(que.get())


if __name__ == "__main__":
    main()
