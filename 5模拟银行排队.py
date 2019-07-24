import random
import time as Time


def str2int(s):
    try:
        s = int(s)
        return s
    except ValueError:
        s = input('请输入整数：')
        return str2int(s)


def searchMin(List):
    min_ = 0
    for i in range(len(List) - 1):
        if List[min_] > List[i + 1]:
            min_ = i + 1
    return min_


class consumer:
    def __init__(self, arriveTime, needTime):
        self.arriveTime = arriveTime
        self.needTime = needTime


def main():
    """ 一队人 分窗口 输出大家的平均等待时间"""
    numWin = str2int(input('the number of windows:'))
    numCon = str2int(input('the number of consumers:'))
    t0 = Time.process_time()  # 计时开始
    conList = [
        consumer(random.random() * 60,
                 random.random() * 7 + 3) for i in range(numCon)
    ]
    conList.sort(key=lambda x: x.arriveTime)
    t1 = Time.process_time()
    for i in range(numCon):
        print('No.{} arrived at %.2f, need %.2f.'.format(i + 1) %
              (conList[i].arriveTime, conList[i].needTime))
    print('----------------------')  # test info
    t2 = Time.process_time()
    time = conList[0].arriveTime
    waiTime = [0] * numCon
    winUsingTime = [conList[0].needTime] + [0] * (numWin - 1)  # from now time
    for i in range(numCon - 1):
        i += 1
        minWin = searchMin(winUsingTime)  # the number of min left time
        time += winUsingTime[minWin]
        winUsingTime = [
            winUsingTime[j] - winUsingTime[minWin] for j in range(numWin)
        ]
        if conList[i].arriveTime <= time:
            waiTime[i] = time - conList[i].arriveTime
        else:
            winUsingTime = [
                winUsingTime[j] - (conList[i].arriveTime - time)
                for j in range(numWin)
            ]
            for j in range(numWin):
                if winUsingTime[j] < 0:
                    winUsingTime[j] = 0
            time = conList[i].arriveTime
        winUsingTime[minWin] = conList[i].needTime
    averWaiTime = sum(waiTime) / numCon
    t3 = Time.process_time()
    for i in range(numCon):
        print('No.{} wait for %.2f.'.format(i + 1) % waiTime[i])
    print('Average waiting time: %.2f.' % averWaiTime)
    print('using %fs' % (t3 - t2 + t1 - t0))


if __name__ == "__main__":
    main()
