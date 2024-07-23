#num=int(input("Enter the nth term of fibonacci:"))
#F1=0
#F2=1
#if num==1:
    #print(F1)
#else:
    #for i in range(2,num):
        #sum=F1+F2
        #F1=F2
        #F2=sum
    #print(F2)

  



num=int(input("Enter the nth term of fibonacci:"))
def calculate(num):
    if num<=0:
        return"none"
    elif num==1:
        return 0
    elif num==2:
        return 1
    
    sequence=[0,1]

    for i in range(2,num):
        sequence.append(sequence[i-1]+sequence[i-2])
    return sequence[-1]
n=calculate(num)
print(n)