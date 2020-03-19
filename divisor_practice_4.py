Number = int(input('Enter a positive Intiger'))
x=[]
for i in range(1,Number+1):
    if Number%i ==0:
        x.append(i)
print(x)
