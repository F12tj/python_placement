a=input("enter the string ")
print(a)
alp_len=len(a)
print(alp_len)
s=set()
for i in range(alp_len):
    if(i%2==0):
        s.add(a[i])
print(s)