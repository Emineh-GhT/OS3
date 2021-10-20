
x=1
i=1
while x>0:
    if i==1:
        print("adad mored nazar khod ra vared konid : ")
        araye=[int (x)for x in input ("***** dar payan enter bezanid ***** ").split()]
        l=int (len(araye))
        i=1
        f=0
        while i < l:
            if(araye[i] <= araye[i - 1]):
               f = 1
            i += 1
        if (f==0) :
            print ("yes")
        else :
            print ("no")
        break