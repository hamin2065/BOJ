n = int(input())
arr = []
for i in range(n) : 
    start, end = map(int, input().split())
    arr.append((start, end))
    
arr.sort(key = lambda x : (x[1],x[0]))
classes = [arr[0]]
for i in range(1,n) : 
    if classes[-1][1] <= arr[i][0] :
        classes.append(arr[i])

print(len(classes))