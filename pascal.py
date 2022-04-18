def BuildTriangle(row):
    triangle = []
    for i in range(row+2):
        l = [1]
        C = 1
        for j in range(1, i+1):
            C = C * (i - j) // j
            l.append(C)
        triangle.append(l[:len(l)-1])
    return triangle[1:]


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
                if counter and decounter > 1:
                    test = f"{i}*{x}^{counter}*{y}^{decounter}"
                if counter == 1 or counter == 0:
                    test = f"{i}*{x}*{y}^{decounter}"
                if decounter == 1 or decounter == 0:
                    test = f"{i}*{x}^{counter}*{y}"
                if counter == 1 or decounter == 1:
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
    m = [[1 for i in range(k)] for j in range(k)]
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
