# #expr# &  | ! ()

# (#e1# & #e2#) |(!#e3# & #e4#)

from stack import Stack
# '(#abc# & #324#) | (!#def# & #789#)'

def match(exprs, line, fn):
    stack = Stack()
    is_expr = False
    expr = []
    for c in exprs:
        if c == '#':
            if not is_expr:
                is_expr = True
            else:
                is_expr = False
                v = fn(line, ''.join(expr))
                expr = []
                if stack.top is None:
                    stack.push(v)
                    continue
                s = stack.pop()
                if s == '!':
                    v = not v
                    if stack.top is None:
                        stack.push(v)
                        continue
                    s = stack.pop()
                if s == '&':
                    if isinstance(stack.top.value, bool):
                        v = stack.pop() and v
                        stack.push(v)
                    else:
                        raise Exception('wrong expr')
                elif s == '|':
                    if isinstance(stack.top.value, bool):
                        v = stack.pop() or v
                        stack.push(v)
                    else:
                        raise Exception('wrong expr')
                elif s == '(':
                    stack.push(s)
                    stack.push(v)
                else:
                    raise Exception('wrong expr')
        else:
            if is_expr:
                expr.append(c)
            else:
                if c in '(&!|':
                    stack.push(c)
                elif c.strip() == '':
                    pass
                elif c == ')':
                    v = stack.pop()
                    if not isinstance(v, bool):
                        raise Exception('wrong expr')
                    s = stack.pop()
                    if s == '!':
                        v = not v
                        s = stack.pop()
                    if s == '(':
                        stack.push(v)
                    else:
                        raise Exception('wrong expr')
                else:
                    raise Exception('wrong expr')

    while stack.top:
        v = stack.pop()
        if not isinstance(v, bool):
            raise Exception('wrong expr')
        s = stack.pop()
        if s == '!':
            v = not v
            s = stack.pop()
        if s == '&':
            v2 = stack.pop()
            if not isinstance(v2, bool):
                raise Exception('wrong expr')
            v = v and v2
        elif s == '|':
            v2 = stack.pop()
            if not isinstance(v2, bool):
                raise Exception('wrong expr')
            v = v or v2
        else:
            raise Exception('wrong expr')
        if stack.top is None:
            return v
        else:
            stack.push(v)

if __name__ == '__main__':
    import re
    line = 'abc 123 def 456 asd 789'
    exprs = '(#abc# & #324#) | (!#def# & #789#)' # False

    def callback(line, expr):
        return re.match(expr, line) is not None

    print(match(exprs, line, callback))

#TODO 优化两个程序， 使其模块化