def BuildTriangle(row):
    triangle = []
    for i in range(1, row+2):
        l = []
        C = 1
        for j in range(1, i+1):
            l.append(C)
            C = C * (i - j) // j
        triangle.append(l)
    return triangle


def CalculatePower(power):
    triangle = BuildTriangle(power+1)
    s = 0
    for i in triangle[power]:
        s += i
    return s


def CalculateCoefficent(x, y, highCoefficent):
    triangle = BuildTriangle(highCoefficent+1)
    if highCoefficent != 1 or highCoefficent != 0:
        string = [f"{x}^{highCoefficent}"]
        counter = highCoefficent-1
        decounter = 1
        for i in triangle[highCoefficent]:
            if i != 1:
                if counter > 1 and decounter > 1:
                    test = f"{i}*{x}^{counter}*{y}^{decounter}"
                if counter == 1 and decounter > 1:
                    test = f"{i}*{x}*{y}^{decounter}"
                if decounter == 1 and counter > 1:
                    test = f"{i}*{x}^{counter}*{y}"
                if decounter == 1 and counter == 1:
                    test = f"{i}*{x}*{y}"
                counter -= 1
                decounter += 1
                string.append(test)
        string.append(f"{y}^{highCoefficent}")
    if highCoefficent == 1:
        string = [f"{x}"]
        string.append(f"{y}")
    if highCoefficent == 0:
        string = [1, 1]
    return string


def CalculatePath(k):
    # m = [[1 for i in range(k)] for j in range(k)]
    m = []
    for i in range(k):
        l = []
        for j in range(k):
            l.append(1)
        m.append(l)
    for i in range(1, k):
        for j in range(1, k):
            m[i][j] = m[i][j-1] + m[i-1][j]
    return m


inputValue1 = input().split(' ')
inputValue2 = input().split(' ')

t = BuildTriangle(int(inputValue1[0]))
for i in t:
    print(*i)

print('\n')

print(CalculatePower(int(inputValue1[1])))

x = CalculateCoefficent(inputValue2[0], inputValue2[1], int(inputValue2[2]))
print(*x, sep=' + ', end=' ')

print('\n')

p = CalculatePath(int(inputValue1[2]))
for i in p:
    print(*i, sep=',')
