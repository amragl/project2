def print_max(a,b):
    if a>b:
        print(a,'is maximun')
    elif a==b:
        print (a,'is equal to',b)
    else:
        print(b,'is maximun')

#directly pass literal values
print_max(3,4)

x=5
y=5

# pass variable as arguments
print_max(x,y)
