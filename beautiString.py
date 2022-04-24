string = input()
splitedString = string.split(' ')
lowerString = string.lower().split(' ')
subCopy = splitedString.copy()


for i in range(len(splitedString)):
    for j in range(i+1, len(splitedString)):
        if lowerString[j] in lowerString[i]:
            if len(lowerString[i]) > len(lowerString[j]):
                subCopy.remove(splitedString[j])
            else:
                subCopy.remove(splitedString[i])


print(*subCopy, end=' ')
