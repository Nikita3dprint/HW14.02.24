s = 55 * '0' + '1'
while '1' in s:
    if '10' in s:
        s = s.replace('10', '001', 1)
    else:
        s = s.replace('1', '00', 1)
print(s.count('0'))
