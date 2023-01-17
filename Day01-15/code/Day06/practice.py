def foo():
    b = 'hello'

    # Python中可以在函数内部再定义函数
    def bar():
        c = True
        nonlocal b
        b = 'bye'
        global a
        a = 500
        print(a)
        print(b)
        print(c)

    bar()
    # print(c)  # NameError: name 'c' is not defined
    print(f'b: {b}')
    print(f'a in foo: {a}')


if __name__ == '__main__':
    a = 100
    # print(b)  # NameError: name 'b' is not defined
    foo()
    print(f'a in main: {a}')