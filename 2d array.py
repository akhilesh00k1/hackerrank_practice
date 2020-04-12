
#n=int(input())#no of rows and columns
#square matrix
def oneway(n):
    matrix=[]
    for row in range(n):
        line=[]
        for column in range(n):
            line.append(int(input()))
        matrix.append(line )
    return matrix
def otherway(n):
    matrix=[]
    for row in range(n):
        line=[int(i) for i in input().strip().split(" ")]
        matrix.append(line)  
    return matrix  
def lrdiagonalsum(matrix):
    pass
def lrrldiagonalsum(arr):
    l2r=[]
    n=len(arr)
    r2l=[]

    for  i in range(len(arr)):
        for j in range(len(arr[i])):
            if i==j:
                l2r.append(arr[i][j])
            elif j==n:
                r2l.append(arr[i][j])
                n-=1
    return abs(sum(l2r)+sum(r2l))

arr=[[1,2,3],[4,5,6],[7,8,9]]
print(lrrldiagonalsum(arr))
        
