#for i in range(5):
#    print(i)


#a = ["Mary", "had", "a", "little", "lamb"]
#for i in range(len(a)):
 #   print(i, a[i])

for n in range(2, 10):
    for x in range(2, n):
        if n%x ==0:
            print(n, 'equals to', x, '*', n//x)
            break
        else:
            print(n, "is prime number")
