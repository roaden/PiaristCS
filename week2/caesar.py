def shift(num, tobeshifted):
    lower = 'abcdefghijklmnopqrstuvwxyz'
    upper = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
    aftershift = ''
    for i in range(len(tobeshifted)):
        didshift = False
        for j in range(len(lower)):
            if lower[j] == tobeshifted[i]:
                aftershift += lower[(j+num)%26]
                didshift = True
                print("I did a thing.")
                break
            elif upper[j] == tobeshifted[i]:
                aftershift += upper[(j+num)%26]
                didshift = True
                print("I did another thing")
                break
        if not didshift:
            aftershift += tobeshifted[i]
    return aftershift

theshift = 13
print('Type quit to exit')

while(True):
    thingtoshift = input()
    if thingtoshift == 'quit':
        break
    print(shift(theshift,thingtoshift))
