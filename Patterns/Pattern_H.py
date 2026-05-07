m = int(input("Enter the number of rows:\t"))      #put minimum 7    
n = int(input("Enter the number of columns:\t"))   #put minimum 6  
if (m%2 == 0):                                      
    m += 1
for i in range(1 , m+1):
    for j in range(1 , n+1):
        if (j==1 or j==2 or j==n or j==n-1 or i==int(m/2)+1):    
            print("*",end=" ")
        else:
            print(" ",end=" ") 
    print()