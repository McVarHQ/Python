unsortedData = [9,1,12,11,0,15,8,4,2,11,11,0,6,11,15,1,15,7,11,24,6,7,2,9,8]
def sortAsc(unsortedData):
    for n in range(len(unsortedData)-1, 0, -1):
        for i in range(n):
            if unsortedData[i] > unsortedData[i + 1]:
                unsortedData[i], unsortedData[i + 1] = unsortedData[i + 1], unsortedData[i]
                #print(unsortedData)

    sortedData = unsortedData
    return sortedData

def sortDes(unsortedData):
    for n in range(len(unsortedData)-1, 0, -1):
        for i in range(n):
            if unsortedData[i] < unsortedData[i + 1]:
                unsortedData[i], unsortedData[i + 1] = unsortedData[i + 1], unsortedData[i]
                #print(unsortedData)

    sortedData = unsortedData
    return sortedData

unsortedData = [9,1,12,11,0,15,8,4,2,11,11,0,6,11,15,1,15,7,11,24,6,7,2,9,8]
print(len(unsortedData))
sortedData_Asc = sortAsc(unsortedData)
print(sortedData_Asc)

sortedData_Des = sortDes(unsortedData)
print(sortedData_Des)
