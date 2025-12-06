# Author : Soumyadeep Mukherjee
# Title : Selection Sort Algorithem

def selectSort(sList):
    for i in range(len(sList)):
        min_ind = i                       # Initial Index
        for j in range(i+1, len(sList)):  # Find the min value 
            if sList[min_ind] > sList[j]: # Compare min value with initial value
                min_ind = j
        sList[i],sList[min_ind] = sList[min_ind],sList[i] # If initial value is greater than min value Swap the postion

    print(sList)

selectSort([6,2,3,4,7,11,1,16,12,9,13])
