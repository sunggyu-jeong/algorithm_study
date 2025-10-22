inputList = input().split(" ")
targetList = input().split(" ")
filterList = (int(v) for v in targetList if int(v) < int(inputList[1]))
print(*filterList)