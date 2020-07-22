class Test:
    def __init__(self, a = None):
        if a == None:
            print('No arg constructor')
        else:
            print('Arg constructor')

test0 = Test()
test1 = Test('a')
