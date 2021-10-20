
print("yek adad ra vared konid:")
adad=int(input())
t=0
i=1
while True:
    if adad==1:
        print("yes")
        break
    else:
        if adad%i==0:
            adad=adad/i
            t+=1
            i+=1
        else :
            t=0
            print("no")
            break