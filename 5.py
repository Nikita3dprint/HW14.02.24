mn = 10000000000
for n in range(1, 200):
    b = bin(n)[2:]
    if n % 2 == 0:
        b = '1' + b + '0'
    else:
        b = '11' + b + '11'
    r = int(b, 2)
    if r > 225:
        print(r)
        if r < mn:
            mn = r
print(mn)
