

from stack import Stack

func_map = {
    '+': lambda x, y: x+y,
    '*': lambda x, y: x*y,
    '/': lambda x, y: x/y,
    '-': lambda x, y: x-y
}

# (3 + 4) * 5 / ((2+3) *3)
def cacl(expr):
    stack = Stack()
    for c in expr:
        if c in '(+-*/':
            stack.push(c)
        elif c.strip() == '':
            pass
        else:
            if c != ')':
                c = int(c)
                if stack.top.value in '+-/*':
                    s = stack.pop()
                    if not isinstance(stack.top.value, (int, float)):
                        raise Exception('wrong expr')
                    v = stack.pop()
                    v = func_map[s](v, c)
                    stack.push(v)
                else:
                    stack.push(c)
            if c == ')':
                if isinstance(stack.top.value, (int, float)):
                    v = stack.pop()
                    if stack.top.value == '(':
                        stack.pop()
                        stack.push(v)
                    else:
                        raise Exception('wrong expr')
                else:
                    raise Exception('wrong expr')
    while stack.top:
        c = stack.pop()
        if not isinstance(c, (int, float)):
            raise Exception('wrong expr')
        if stack.top.value in '+-/*':
            s = stack.pop()
            if not isinstance(stack.top.value, (int, float)):
                raise Exception('wrong expr')
            v = stack.pop()
            v = func_map[s](v, c)
            if stack.top is None:
                return v
            stack.push(v)
        else:
            raise Exception('wrong expr')

if __name__ == '__main__':
    print(cacl('(3 + 4) * 5 / ((2+3) *3)'))

#TODO 实现带优先级的算术表达式解析