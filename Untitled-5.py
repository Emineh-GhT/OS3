
print("yek adad ra vared konid:")
adad=input()
l=len(adad)
sum=0
a=int(adad)

for i in range(l) :
    x=int(adad[i])
    sum=x**l+sum
    
if sum==a:
    print("yes")
else:
    print("no")