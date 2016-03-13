def gen():
    c = 0
    while True:
        yield 0
        c += 1
        if c > 3:
            raise GeneratorExit()

for x in gen():
    print(x)
