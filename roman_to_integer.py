def roman_to_int():
    r = str(input("enter your roman number  "))
    sol = {'I':1,'V':5,'X':10,'L':50,'C':100,'D':500,'M':1000}
    final_ans = 0
    r = r.upper()
    for i in r:        
        final_ans = final_ans+sol.get(i)    
    a = 0
    b = 1
    if len(r) > 1:
        for i in range(len(r) - 1):
            if sol.get(r[a]) < sol.get(r[b]):
                final_ans = final_ans + (-2) * sol.get(r[a])
            a = a+1
            b = b+1
    print(final_ans)
roman_to_int()
