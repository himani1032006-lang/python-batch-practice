s="aaabcde"
ch={}
for i in s:
    for i in ch:
        if i in ch:
            ch[i]=ch[i]+1
        else:
            ch[i]=ch[i]
print(ch[i])