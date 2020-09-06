import time
t=time.time()
def askput(question,num,listing):
        ans="k"
        while not(ans=="y" or ans=="n"):
            ans = input(question)
        i=0
        k = len(listing)
        if ans == "y":
            while i<k-1:
                if listing[i]%num>0:
                    listing.pop(i)
                    k-=1
                else:
                    i=i+1
        else:
            while i<k-1:
                if listing[i]%num==0:
                    listing.pop(i)
                    k-=1
                else:
                    i=i+1
        return listing
def guess_a_number(a,c,amount):
    divisible=[2,3,5,7,11,13,19,23]
    list_ans=[]
    for i in range(a,c+1):
        list_ans.append(i)
    count=0
    ans = True
    while ans == True:
        list_ans = askput(("is it divisible by "+str(divisible[count])+"?: (y/n)"),divisible[count],list_ans)
        count+=1
        if count == len(divisible)-1 or len(list_ans)<=amount:
            ans = False
    print(list_ans)
        
    
guess_a_number(10,50,2)
print("total time takes"+str(time.time()-t))
    
            
        
            
                    
    
