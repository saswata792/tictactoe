a=[['1','2','3'],['4','5','6'],['7','8','9']]
c=[0,0,0,0,0,0,0,0]
d=[0,0,0,0,0,0,0,0]
def win():
        global a
        for i in range(len(a)):
            for j in range(len(a[i])-1):
                if(a[i][j]!=a[i][j+1]):
                    break
            else:
                return(1)
        if(a[0][0]==a[1][1] and a[1][1]==a[2][2]):
            return(1)
        
        if(a[0][2]==a[1][1] and a[1][1]==a[2][0]):
            return(1)
        for i in range(len(a)):
            for j in range(len(a[i])-1):
                if(a[j][i]!=a[j+1][i]):
                    break
            else:
                return(1)
def count():
    global a,c,d
    c=[0,0,0,0,0,0,0,0]
    d=[0,0,0,0,0,0,0,0]
  #row  
    for i in range(len(a)):
        
        for j in range(len(a[i])):
                       
                       if(a[i][j]=='x'):
                           d[i]+=1
                       elif(a[i][j]=='o'):
                           c[i]+=1
   #coloumn
        for i in range(len(a)):
            for j in range(len(a[i])):
                if(a[j][i]=='x'):
                    d[i+3]+=1
                elif(a[j][i]=='o'):
                    c[i+3]+=1
    #diagonal
        for i in range(len(a)):
            if(a[i][i]=='x'):
                d[6]+=1
            elif(a[i][i]=='o'):
                c[6]+=1
            elif(a[i][2-i]=='x'):
                d[7]+=1
            elif(a[i][2-i]=='o'):
                c[7]+=1
def intelli():
    global a,c,d
    count()
    
    for i in range(len(c)):
        
        
        if(c[i]==2):
            if(i<=2):
                for j in range(3):
                    if(a[i][j]!='o'):
                        return(a[i][j])
                    
                        
                        
            elif(i<=5):
                for j in range(3):
                    if(a[j][i-3]!='o'):
                        return(a[j][i-3])
                        
                        
            elif(i==6):
                for j in range(3):
                    if(a[j][j]!='o'):
                        return(a[j][j])
                        
                        
            elif(i==7):
                for j in range(3):
                    if(a[j][2-j]!='o'):
                        return(a[j][2-j])
    for i in range(len(d)):
        if(d[i]==2):
            if(i<=2):
                for j in range(3):
                    if(a[i][j]!='x' and a[i][j]!='o'):
                        return(a[i][j])
                    
                        
                        
            elif(i<=5):
                for j in range(3):
                    if(a[j][i-3]!='x' and a[j][i-3]!='o'):
                        return(a[j][i-3])
                        
                        
            elif(i==6):
                for j in range(3):
                    if(a[j][j]!='x' and a[j][j]!='o'):
                        return(a[j][j])
                        
                        
            elif(i==7):
                for j in range(3):
                    if(a[j][2-j]!='x' and a[j][2-j]!='o'):
                        return(a[j][2-j])
            
                        
                        
    if(a[1][1]!='x' and a[1][1]!='o'):
        return(a[1][1])
        
        
        
    else:
        for i in range(0,3,2):
            if(a[i][i]!='x' and a[i][i]!='o'):
                return(a[i][i])
            
                
        else:
            for i in range(0,3,2):
                if(a[i][2-i]!='x' and a[i][2-i]!='o'):
                    return(a[i][2-i])
                    
                    
        for i in range(0,2):
            if(a[i][1-i]!='x' and a[i][1-i]!='o'):
                return(a[i][1-i])
                
                
        else:
            for i in range(1,3):
                
                if(a[i][3-i]!='x' and a[i][3-i]!='o'):
                    return(a[i][3-i])
def tictactoe():
    global a,c,d
    n=0
    p=int(input("kaka eka khelbe na jorae khelbe,1 or 2 : "))
    while(1):
        
        
        if(p==1):
            
            if(n%2==0):
                 p1=input("hey!enter your bid first one: ")
                 for i in range(len(a)):
                     for j in range(len(a[i])):
                         if(a[i][j]==p1):
                             a[i][j]='x'
                     
                 if(n>3):
                     q=win()
                     if(q==1):
                         print("p1 wins after",n,"call")
                         break
            else:
                p2=input("hey!enter your bid second one: ")
                for i in range(len(a)):
                      for j in range(len(a[i])):
                          if(a[i][j]==p2):
                              a[i][j]='o'
                if(n>4):
                    q=win()
                    if(q==1):
                        print("p2 wins after",n,"call")
                        break
            n=n+1
            for i in a:
                for j in i:
                    print(j,end=" ")
        elif(p==2):
            if(n%2==0):
                 p1=input("hey!enter your bid first one: ")
                 for i in range(len(a)):
                     for j in range(len(a[i])):
                         if(a[i][j]==p1):
                             a[i][j]='x'
                 if(n>3):
                     
                     q=win()
                     if(q==1):
                         print("p1 wins after",n,"call")
                         break
            else:
                
                p2=intelli()
                print("\ncomputer choose: ",p2)
                for i in range(3):
                    for j in range(3):
                        if(a[i][j]==p2):
                            
                            a[i][j]='o'
                        
                    
                if(n>3):
                     q=win()
                     if(q==1):
                         print("computer wins after",n,"call")
                         break
            
            n=n+1
            for i in range(3):
                for j in range(3):
                    print(a[i][j],end=" ")
                print()
                    
tictactoe()                   
                           
                    
                           
    
    
    
    