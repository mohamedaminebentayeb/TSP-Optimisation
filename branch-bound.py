from math import inf
A=[[0,1,0,0],[0,0,1,0],[0,0,0,1],[1,0,0,0]]
currentPath=[0]
currentPathValue=0
M=float(inf)
bestPath=[]
n=len(A)
adj=0
for i in range(n):
    if(A[i][0]>0) : adj+=1
i=0
while(len(currentPath)>0):
        if(len(currentPath)==n):
            if(A[currentPath[-1]][0]>0):
                currentPathValue+= A[currentPath[-1]][0]
                if(currentPathValue<M):
                    M=currentPathValue
                    bestPath=currentPath.copy()
                currentPathValue-=A[currentPath[-1]][0]
            currentPathValue-=A[currentPath[-2]][currentPath[-1]]
            i=currentPath.pop()+1
            if(A[i-1][0]>0) : adj+=1
        elif (adj==0):
            currentPathValue-=A[currentPath[-2]][currentPath[-1]]
            i=currentPath.pop()+1
            if(A[i-1][0]>0) : adj+=1
        else : 
            while(i<n): 
                if(not(i in currentPath)):
                        if(A[currentPath[-1]][i]>0):
                            currentPathValue+=A[currentPath[-1]][i]
                            if(currentPathValue<M):
                                currentPath.append(i)
                                if(A[i][0]>0) : adj-=1
                                i=0
                                break
                            else:
                                currentPathValue-=A[currentPath[-1]][i]
                i+=1
            if(i==n):
                    if(len(currentPath)>1):
                        currentPathValue-=A[currentPath[-2]][currentPath[-1]]
                    i=currentPath.pop()+1
                    if(A[i-1][0]>0) : adj+=1
print(bestPath)
print(M)
bestPath.append(0)
