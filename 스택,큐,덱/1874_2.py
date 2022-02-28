from collections import deque
from sys import stdin

n = int(input())
st = [0]
nums = deque([i+1 for i in range(n)])
cal = []

for _ in range(n) : 
    a = int(stdin.readline())
    b = len(nums)
    if a == st[-1] : 
        st.pop()
        cal.append('-')
    else : 
        for _ in range(b):
            if nums[0] <= a :
                st.append(nums[0])
                nums.popleft()
                cal.append('+')
            else : 
                break
        if st[-1] != a : 
            print("NO")
            exit()
        else : 
            st.pop()
            cal.append('-')
            
print("\n".join(cal))
