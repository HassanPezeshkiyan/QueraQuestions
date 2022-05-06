data = input().split('/')

dataMatrix = []
for i in data:
    tempList = []
    for j in i.split(','):
        tempList.append(int(j))
    dataMatrix.append(tempList)


for i in range(len(dataMatrix)):
    for j in range(i+1, len(dataMatrix)):
        if dataMatrix[i][len(dataMatrix[i])-1] < dataMatrix[j][len(dataMatrix[j])-1]:
            dataMatrix[i], dataMatrix[j] = dataMatrix[j], dataMatrix[i]
        elif dataMatrix[i][len(dataMatrix[i])-1] == dataMatrix[j][len(dataMatrix[j])-1]:
            if dataMatrix[i][4] < dataMatrix[j][4]:
                dataMatrix[i], dataMatrix[j] = dataMatrix[j], dataMatrix[i]
            elif dataMatrix[i][4] == dataMatrix[j][4]:
                if dataMatrix[i][len(dataMatrix[i])-2] < dataMatrix[j][len(dataMatrix[j])-2]:
                    dataMatrix[i], dataMatrix[j] = dataMatrix[j], dataMatrix[i]


for i in dataMatrix:
    print(*i, end='\n')

