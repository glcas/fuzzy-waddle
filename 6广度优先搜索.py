import queue
import copy


def shortest(start, end, gragh):
    ''' find shortest way to the vex,return a list '''
    start, end = start - 1, end - 1
    visited = [0] * len(gragh)
    route = {i: [] for i in range(len(gragh))}
    que = queue.Queue()
    que.put(start)
    while visited[end] == 0 and que.qsize() != 0:
        now = que.get()
        visited[now] = 1
        for i in range(len(gragh)):
            if gragh[now][i] == 1 and visited[i] == 0:
                if route[i] == []:
                    route[i] = copy.deepcopy(route[now])
                    route[i].append(now + 1)
                que.put(i)
    return route[end]


def main():
    # test
    figure = [[0, 1, 0, 1, 0, 0, 0], [0, 0, 0, 1, 1, 0, 0],
              [1, 0, 0, 0, 0, 1, 0], [0, 0, 1, 0, 1, 1, 1],
              [0, 0, 0, 0, 0, 0, 1], [0, 0, 0, 0, 0, 0, 0],
              [0, 0, 0, 0, 0, 1, 0]]
    for i in range(len(figure)):
        for j in range(len(figure)):
            path = shortest(i + 1, j + 1, figure)
            if path == []:
                print('V{}->V{} No way'.format(i + 1, j + 1))
            else:
                for k in range(len(path)):
                    print('V{}->'.format(path[k]), end='')
                print('V{} lenth={}'.format(j + 1, len(path)))


if __name__ == "__main__":
    main()
"""
test result:
V1->V1 No way
V1->V2 lenth=1
V1->V4->V3 lenth=2
V1->V4 lenth=1
V1->V2->V5 lenth=2
V1->V4->V6 lenth=2
V1->V4->V7 lenth=2
V2->V4->V3->V1 lenth=3
V2->V2 No way
V2->V4->V3 lenth=2
V2->V4 lenth=1
V2->V5 lenth=1
V2->V4->V6 lenth=2
V2->V4->V7 lenth=2
V3->V1 lenth=1
V3->V1->V2 lenth=2
V3->V3 No way
V3->V1->V4 lenth=2
V3->V1->V2->V5 lenth=3
V3->V6 lenth=1
V3->V1->V4->V7 lenth=3
V4->V3->V1 lenth=2
V4->V3->V1->V2 lenth=3
V4->V3 lenth=1
V4->V4 No way
V4->V5 lenth=1
V4->V6 lenth=1
V4->V7 lenth=1
V5->V1 No way
V5->V2 No way
V5->V3 No way
V5->V4 No way
V5->V5 No way
V5->V7->V6 lenth=2
V5->V7 lenth=1
V6->V1 No way
V6->V2 No way
V6->V3 No way
V6->V4 No way
V6->V5 No way
V6->V6 No way
V6->V7 No way
V7->V1 No way
V7->V2 No way
V7->V3 No way
V7->V4 No way
V7->V5 No way
V7->V6 lenth=1
V7->V7 No way
"""
