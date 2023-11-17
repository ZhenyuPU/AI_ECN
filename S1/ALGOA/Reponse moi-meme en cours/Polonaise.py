def is_digit(item):
    if item.isdigit():
        return True
    return False

def polonaise_inversee(L: str):
    operation = ['+', '-', '*', '/']
    stack = []
    num = ''
    num_op = 0
    for item in L:
        if is_digit(item):
            num += item
        elif item == ' ':
            if num:
                stack.append(num)
                num = ''
        elif item in operation:
            if len(stack) <= 1 and num_op == 0:
                print(item)
                num_op += 1
                continue
            elif len(stack) <= 1 and num_op > 0:
                num_op = 0
                stack.append(num)
            a = int(stack.pop())
            b = int(stack.pop())
            if item == '+':
                stack.append(b + a)
            elif item == '-':
                stack.append(b - a)
            elif item == '*':
                stack.append(b * a)
            elif item == '/':
                stack.append(b / a)

    return stack

L = '12 34 + 8 5 - *4+'
print(polonaise_inversee(L))