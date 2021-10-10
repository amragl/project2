
y = input('enter your grade: ')

if (y.isnumeric()):
    x = int(y)
    if (x>=0 and x < 40):
        print ('F')
    elif x < 50:
        print ('D')
    elif x < 60:
        print ('C')
    elif x < 70:
        print ('B')
    elif x > 71:
        print ('A')
    else:
        print ('not valid')
else:
    print('not valid')


