#This function will shift forward by whatever number
def shift(num, tobeshifted):
    #Adding in the alphabets that I'm using.
    lower = 'abcdefghijklmnopqrstuvwxyz'
    upper = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
    aftershift = ''
    for i in range(len(tobeshifted)):
        didshift = False
        for j in range(len(lower)):
            if lower[j] == tobeshifted[i]:
                aftershift += lower[(j+num)%26] #If it's there, shift forward by num
                didshift = True
                #print("I did a thing.") #This was used in debugging
                break
            elif upper[j] == tobeshifted[i]: #We're assuming uppercase == lowercase
                aftershift += upper[(j+num)%26] #Same deal here. Shift forward by num
                didshift = True
                #print("I did another thing") #This was used in debugging.
                break
        if not didshift: #If not found, need to add original thing back.
            aftershift += tobeshifted[i]
    return aftershift

theshift = 13 #Shifting by 13 for nice easy cypher
print('Type quit to exit')

while(True):
    thingtoshift = input()
    if thingtoshift == 'quit': #Exit if you see quit
        break
    print(shift(theshift,thingtoshift)) #Print the shifted value.
