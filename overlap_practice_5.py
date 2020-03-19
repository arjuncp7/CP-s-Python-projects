a = [1,2,4,5,7,8,9,0,12,23,34,65,14,13]
b=[1,2,4,6,8,99,0,12]
x = []
for i in a:
    for j in b:
        if i==j:
            x.append(i)
print(x)
