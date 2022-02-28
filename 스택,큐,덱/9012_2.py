def check(str) : 
    st = []
    for i in str : 
        if i == "(" :
            st.append(i)
        else :
            try : 
                st.pop()
            except : 
                return "NO"
    if len(st) > 0 : return "NO"
    else : return "YES"
n = int(input())

for _ in range(n) :
    print(check(input()))    
    