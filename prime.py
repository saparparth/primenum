num=int(input("enter num"))
c=0
for i in range(1,num+1):
    if(num % i == 0):
        c+=1
if(c == 2):
    print(num," is prime ")
else:
    print(num,"not prime")
    
            
