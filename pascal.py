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


t = BuildTriangle(0)
# for i in t:
#     print(*i)


def CalculatePower(power):
    triangle = BuildTriangle(power+1)
    s = 0
    for i in triangle[power]:
        s += i
    return s


# print(CalculatePower(1))

def CalculateCoefficent(x, y, highCoefficent):
    triangle = BuildTriangle(highCoefficent+1)
    string = [f"{x}^{highCoefficent}"]
    counter = highCoefficent-1
    decounter = 1
    for i in triangle[highCoefficent]:
        if i != 1:
            if counter and decounter != 1:
                test = f"{i}*{x}^{counter}*{y}^{decounter}"
            if counter == 1:
                test = f"{i}*{x}*{y}^{decounter}"
            if decounter == 1:
                test = f"{i}*{x}^{counter}*{y}"
            counter -= 1
            decounter += 1
            string.append(test)
    string.append(f"{y}^{highCoefficent}")
    return string


x = CalculateCoefficent('x', 'y', 6)

print(*x,sep=' + ', end=' ')
