def fibo(num) : 
    for i in range(2,num+1) : 
        arr_0.append(arr_0[-1]+arr_0[-2])
        arr_1.append(arr_1[-1]+arr_1[-2])
    print(arr_0[num],arr_1[num])

T = int(input())

arr_0 = [1,0]
arr_1 = [0,1]

for _ in range(T) :
    fibo(int(input()))
    