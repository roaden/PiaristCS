def textline(foo, bar):
    print(' ', end='')
    for i in range(len(foo)):
        print(bar, end='')
    print()

def textbox(foo):
    textline(foo, '_')
    print('<', end='')
    print(foo, end='')
    print('>')
    textline(foo, '-')

bar = input("What me say?!?!\n")
textbox(bar)

fin = open('stickpony.txt')

for line in fin:
    print(line, end='')
