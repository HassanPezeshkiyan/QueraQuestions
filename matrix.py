lst1 = []
lst2 = []

flag = True
flag2 = True

while flag:
    m1 = input()
    if m1 == '*':
        flag = False
    else:
        m1 = m1.split(' ')
        t = []
        for i in m1:
            try:
                t.append(int(i))
            except:
                pass
        lst1.append(t)

while flag2:
    m2 = input()
    if m2 == '=':
        flag2 = False
    else:
        m2 = m2.split(' ')
        t = []
        for i in m2:
            try:
                t.append(int(i))
            except:
                pass
        lst2.append(t)

print(lst1)
print(lst2)

lLst1 = (len(lst1), len(lst1[0]))
lLst2 = (len(lst2), len(lst2[0]))

result = []
for i in range(len(lst1)):
    t = []
    for j in range(len(lst2[0])):
        t.append(0)
    result.append(t)

if lLst1[1] == lLst2[0]:
    for i in range(lLst1[0]):
        for j in range(lLst2[1]):
            for k in range(lLst2[0]):
                result[i][j] += lst1[i][k] * lst2[k][j]
    print(result)
else:
    print("Error")
