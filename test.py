a = [1,2,3,4]
b = [4,5,6,7]
count = 0
for (x,y) in zip(a,b):
    count += 1
    print(x)

print(count)
