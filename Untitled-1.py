
import random

asami=['sajad','emineh','ali','asal','arezou','sara','anahid','soode','tina','tara','sam','alireza','reza','maryam','mina','mahmood','sahar','fariba','jalal','samaneh','narges','arash','kourosh','shima','shahrzad','shahnaz','hanye','hedye','toktam']


index=random.randint(0,len(asami)-1)
word=asami[index]
joon=len(word)

utc=[]
''' print - for evry '''
print("/n ********** qarare yek esm hads bezanid **********")
while True:
    t_=0
    for char in word:
        if char in utc:
            print(char,end="")
        else:
            t_+=1
            print("-",end="")
    if t_==0:
        print("\n ********** shoma barande shodid :) ********** ")
        break
        
    uc=input("\n ********** yek harf vared konid... ********** ")  
    
    if uc in word:
        utc.append(uc)
        print('✔')
    else :
        joon-=1
        print('❌')
        
   
    if joon ==0 :
        print("********** motaasefane shoma bazande shodid :( ********** ")
        break