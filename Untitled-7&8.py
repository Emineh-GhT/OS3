
def bmm(x,y):
    z = 1
    if x > y:
        a = y
    else:
        a = x
    for i in range(a, 1, -1):
        if ((x % i == 0) and (y % i == 0)):
            z = i
            break
    print(z)

def kmm (x,y):

    z = x * y
    if x < y:
        a = y
    else:
        a = x
    for i in range(a, x*y, a):
        if ((i % x == 0) and (i % y == 0)):
            z = i
            break
    print(z)

i=1
while True:
    print("***** bmm (1) | kmm(2) ? *****")
    i=int(input())
    if i==1 :
        print ("do adad vared konid : ")
        x= int(input())
        y= int(input())
        bmm(x,y)  

    if i==2:
        print("do adad vared konid : ")
        x= int(input())
        y= int(input())
        kmm(x,y)           
        break      