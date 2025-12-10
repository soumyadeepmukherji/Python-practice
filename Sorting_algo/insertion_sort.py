def insertionSort(cList):
    for i in range(1, len(cList)):
        key = cList[i]
        j = i-1
        while j>=0 and key < cList[j]:
            cList[j+1] = cList[j]
            j -= 1
            
        cList[j+1] = key
    print(cList)

insertionSort([9,2,5,1,11])
