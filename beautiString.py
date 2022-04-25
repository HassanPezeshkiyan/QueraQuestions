string = input()
splitedString = string.split(' ')
duplicateCopy = splitedString.copy()


for i in range(len(splitedString)):
    for j in range(i+1, len(splitedString)):
        if splitedString[i] == splitedString[j]:
            duplicateCopy.remove(splitedString[i])

for i in range(len(duplicateCopy)):
    for j in range(i+1, len(duplicateCopy)):
        if duplicateCopy[i].lower() in duplicateCopy[j].lower() or duplicateCopy[j].lower() in duplicateCopy[i].lower():
            if len(duplicateCopy[i]) > len(duplicateCopy[j]):
                duplicateCopy[j] = '#'
            else:
                duplicateCopy[j] = '#'

for i in duplicateCopy:
    if i != '#':
        print(i, end=" ")
