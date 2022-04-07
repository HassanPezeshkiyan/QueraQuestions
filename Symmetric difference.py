data1 = input("Enter values with , for seperate: ")
data2 = input("Enter values with , for seperate: ")
data3 = input("Enter values with , for seperate: ")

data1 = [int(i) for i in data1.split(',')]
data2 = [int(i) for i in data2.split(',')]
data3 = [int(i) for i in data3.split(',')]

x1 = [i for i in data1 if i not in data2]
x2 = [i for i in data2 if i not in data1]
x1 = list(set(x1))
x2 = list(set(x2))
data1data2Delta = x1 + x2
x3 = [i for i in data3 if i not in data1data2Delta]
x4 = [i for i in data1data2Delta if i not in data3]
x3 = list(set(x3))
x4 = list(set(x4))
finalDelta = x3 + x4

print(sorted(finalDelta))
