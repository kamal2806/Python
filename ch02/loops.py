words = ['one','two','three','four','five']

for i in words:
    print(i,end=' ')

print()

n = 0
while(n<5):
    print(words[n],end=' ')
    n += 1

print()

a,b = 0,1
while b < 1000:
    print(b,end=' ',flush=True)
    a,b = b,a+b

print()