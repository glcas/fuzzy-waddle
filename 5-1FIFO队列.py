import random


class myQueue:
    """ create a queue by list init methods """

    def __init__(self):
        self.que = []

    def put(self, x):
        self.que.append(x)

    def get(self):
        if len(self.que) != 0:
            t = self.que[0]
            self.que.pop(0)
            return t

    def top(self):
        return self.que[0]

    def qempty(self):
        """ return T or F """
        if len(self.que) == 0:
            return True
        else:
            return False

    def dele(self):
        """ clean all items """
        self.que.clear()

    def qsize(self):
        return len(self.que)


def str2int(s):
    try:
        s = int(s)
        return s
    except ValueError:
        s = input('请输入整数：')
        return str2int(s)


def funMyQueue():  # include conduction
    """ create a lenth-limited queue by array """

    def create(n):
        queue = [[0 for i in range(n)]
                 for i in range(2)]  # [1][0] for front, [1][1]for rear
        queue[1][
            1] = -1  # by this way, front=rear=0 after the first item appears
        return queue

    def qsize(queue):
        """ how many items """
        return queue[1][1] - queue[1][0] + 1

    def put(queue, data):
        """ convey a list, put items into my queue, if succeed return True, return False instead """
        if len(data) > len(queue[0]) - qsize(queue):
            return False
        else:
            if len(data) > len(queue[0]) - queue[1][1] - 1:
                queue[0] = queue[0][queue[1][0]:queue[1][1] +
                                    1] + [0] * (len(queue[0]) - qsize(queue))
                queue[1][0], queue[1][1] = 0, queue[1][1] - queue[1][0]
            for i in range(len(data)):
                queue[1][1] += 1
                queue[0][queue[1][1]] = data[i]
            return True

    def get(queue):
        """ get items from the queue """
        g = queue[0][queue[1][0]]
        queue[0][queue[1][0]] = 0
        queue[1][0] += 1
        return g

    def isqempty(queue):
        """ if is empty return True, return False instead """
        if qsize(queue) == 0:
            return True
        else:
            return False

    def dele(queue):
        queue[0] = [0] * len(queue[0])
        queue[1][0] = 0
        queue[1][1] = -1

    n = str2int(input('enter the lenth of the queue: '))
    que = create(n)
    print('put them:')
    data = []
    for i in range(8):
        x = random.randint(1, 100)
        print(x)
        data.append(x)
    while put(que, data) is False:
        n = str2int(
            input('Your queue is not long enough, try another lenth: '))
        que = create(n)
    print('------')
    print('the top of my queue is: {}'.format(que[0][que[1][0]]))
    print('now get items from the queue:')
    for i in range(n):
        while qsize(que) > 0:
            print(get(que))
    print('now put them:')
    data.clear()
    for i in range(10):
        x = random.random() * 10
        print(x)
        data.append(x)
    while put(que, data) is False:
        n = str2int(
            input('Your queue is not long enough, try another lenth: '))
        que = create(n)
    print('Is the queue empty? {}'.format(isqempty(que)))
    dele(que)
    print('After deleting, is the queue empty? {}'.format(isqempty(que)))


def main():
    print('1.test my queue class:\nput them:')
    que = myQueue()
    for i in range(8):
        x = random.randint(1, 100)
        print(x)
        que.put(x)
    print('the top of my queue is: %d' % que.top())
    print('now get items from the queue:')
    for i in range(10):
        while que.qsize() != 0:
            print(que.get())
    print('now put them:')
    for i in range(6):
        x = random.random() * 10
        print(x)
        que.put(x)
    print('Is the queue empty? {}'.format(que.qempty()))
    que.dele()
    print('After deleting, is the queue empty? {}'.format(que.qempty()))
    print('2.test funMyQueue')
    funMyQueue()


if __name__ == "__main__":
    main()
