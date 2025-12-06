# Author : Soumyadeep Mukherjee
# Topic: Bubble Sort Algorithem

# This is for Increasing Order
def bubbleSort(cList):         # --> Create function
    for i in range(len(cList)-1):      
        for j in range(len(cList)-i-1):
            if cList[j] > cList[j+1]:   # --> Check the largest value
                cList[j],cList[j+1] = cList[j+1],cList[j]  # --> Swap the value if condition applied

    print(cList)

bubbleSort([9,11,8,2,7,1,6,22,5,10,15])