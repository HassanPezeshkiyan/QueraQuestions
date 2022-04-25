string = input()
splitedString = string.split(' ')
duplicateCopy = splitedString.copy()


for i in range(len(splitedString)):
    for j in range(i+1, len(splitedString)):
        if splitedString[i] == splitedString[j]:
            duplicateCopy.remove(splitedString[i])

subCopy = duplicateCopy.copy()

for i in range(len(duplicateCopy)):
    for j in range(i+1, len(duplicateCopy)):
        if duplicateCopy[i].lower() in duplicateCopy[j].lower() or duplicateCopy[j].lower() in duplicateCopy[i].lower() and duplicateCopy[i] in subCopy:
            if len(duplicateCopy[i]) > len(duplicateCopy[j]):
                subCopy.remove(duplicateCopy[j])
            else:
                subCopy.remove(duplicateCopy[i])

for i in subCopy:
    print(i, end=' ')
