import queue


def bigTrans(x):
    x = trans(x)
    while x == -1:
        x = trans(input('Please enter a proper expression:'))
    return x


def operate(stackTempOperator, stackReversedPolish, cons, op):
    if stackTempOperator.qsize() == 0:
        stackTempOperator.put(op)
    else:
        top = stackTempOperator.get()
        if top == '(':
            stackTempOperator.put(top)
            stackTempOperator.put(op)
        elif cons == '*/' and top in ('+', '-'):
            stackTempOperator.put(top)
            stackTempOperator.put(op)
        else:
            stackReversedPolish.put(top)
            return operate(stackTempOperator, stackReversedPolish, cons, op)


def trans(x):
    """ return a reversed Polish notation, return -1 when illegal, the last pos for +or- """
    x = [n for n in x]
    conx = [0] * len(x)
    err, unused = False, []
    if len(x) == 1:
        err = True
    i = -1
    while i < len(x) - 1:
        i += 1
        try:
            x[i] = int(x[i])
        except ValueError:
            if i == 0:
                if x[i] in ('-', '+'):
                    x.insert(i, 0)
                    conx.insert(i, 0)
                elif x[i] == '(':
                    conx[i] = '('
                    unused.append(1)
                else:
                    err = True
                    break
            else:
                if x[i] in ('*', '/'):
                    conx[i] = '*/'
                    if conx[i - 1] not in (0, ')'):
                        err = True
                        break
                elif x[i] in ('+', '-'):
                    conx[i] = '+-'
                    if x[i - 1] == '(':
                        x.insert(i, 0)
                        conx.insert(i, 0)
                    elif conx[i - 1] not in (0, ')'):
                        err = True
                        break
                elif x[i] == '(':
                    conx[i] = '('
                    unused.append(1)
                    if x[i - 1] not in ('+', '-', '*', '/'):
                        err = True
                        break
                elif x[i] == ')':
                    conx[i] = ')'
                    if len(unused) != 0:
                        unused.pop()
                    else:
                        err = True
                        break
                    if conx[i - 1] not in (0, ')'):
                        err = True
                        break
                elif x[i] == '.':
                    conx[i] = '.'
                    if conx[i - 1] != 0:
                        err = True
                        break
                else:
                    err = True
                    break
    if conx == [0] * len(x) or len(unused) != 0:
        err = True
    if x[-1] != ')' and type(x[-1]) != int:
        err = True
    if err is True:
        return -1
    else:
        stackReversedPolish = queue.LifoQueue()
        stackTempOperator = queue.LifoQueue()
        for i in range(len(conx)):
            if conx[i] == 0:
                if i != 0 and conx[i - 1] in (0, '.'):
                    continue
                elif i == len(conx) - 1:
                    number = x[i]
                else:
                    j = i + 1
                    while conx[j] in (0, '.'):
                        j += 1
                        if j == len(conx):
                            break
                    number = x[i:j]
                    s = 0
                    if '.' in number:
                        intNum = number[:number.index('.')]
                        floatNum = number[number.index('.') + 1:]
                        for i in range(len(intNum)):
                            s += intNum[i] * 10**(len(intNum) - i - 1)
                        for i in range(len(floatNum)):
                            s += floatNum[i] * 0.1**(i + 1)
                    else:
                        for i in range(len(number)):
                            s += number[i] * 10**(len(number) - i - 1)
                    number = s
                stackReversedPolish.put(number)
            elif conx[i] in ('+-', '*/'):
                operate(stackTempOperator, stackReversedPolish, conx[i], x[i])
            elif conx[i] == '.':
                pass
            elif conx[i] == '(':
                stackTempOperator.put(x[i])
            else:
                top = stackTempOperator.get()
                while top != '(':
                    stackReversedPolish.put(top)
                    top = stackTempOperator.get()
        while stackTempOperator.qsize() != 0:
            stackReversedPolish.put(stackTempOperator.get())
        notation = []
        while stackReversedPolish.qsize() != 0:
            notation.append(stackReversedPolish.get())
        notation.reverse()
        return notation


def calculate(reversedPolishNotation):
    """ calculate the reversed Polish notation """
    numStack = queue.LifoQueue()
    err = False
    for x in reversedPolishNotation:
        if type(x) in (int, float):
            numStack.put(x)
        else:
            b = numStack.get()
            a = numStack.get()
            if x == '+':
                ans = a + b
                numStack.put(ans)
            elif x == '-':
                ans = a - b
                numStack.put(ans)
            elif x == '*':
                ans = a * b
                numStack.put(ans)
            else:
                try:
                    ans = a / b
                    numStack.put(ans)
                except ZeroDivisionError:
                    err = True
                    break
    if err is True:
        expr = bigTrans(
            input(
                'In your expression, zero comes to divisor.\nTry to enter another instead:'
            ))
        return calculate(expr)
    else:
        result = numStack.get()
        return result


def main():
    """ 全部为小括号，含小数负数"""
    exp = bigTrans(input('Enter the expression:'))
    res = calculate(exp)
    print('The answer is: %.3f' % res)


if __name__ == "__main__":
    main()
