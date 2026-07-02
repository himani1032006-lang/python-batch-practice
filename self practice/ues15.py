def star(n):
    for i in range(1,n+1):
        for j in range(,-1,-1):
           print("*", end=" ")    # same line pe print
        print()

print(star(3))