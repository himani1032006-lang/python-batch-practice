s="aaabcde"
ch={}
for i in s:
     if i in ch:
        ch[i]=ch[i]+1
     else:
        ch[i]=1
print(ch)