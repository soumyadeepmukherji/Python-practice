def merge(custome_list, l, m, r): #--> l- first index value, m- middle point, r-end index value
    n1 = m - l + 1 #--> number of item on left side
    n2 = r - m     #--> number of item on right side

    L = [0] * (n1) #--> left side list
    R = [0] * (n2) #--> right side list

    for i in range(0,n1):   #--> Implement items on Left list
        L[i] = custome_list[l+i]

    for j in range(0,n2):   #--> Implement items on right list
        R[j] = custome_list[m+1+j]

    i,j,k = 0,0,l

    while i < n1 and j < n2:
        if L[i] <= R[j]:
            custome_list[k] = L[i]
            i+=1
        else:
            custome_list[k] = R[j]
            j+=1

        k+=1

    while i < n1:
        custome_list[k] = L[i]
        i+=1
        k+=1

    while j < n2:
        custome_list[k] = R[j]
        j+=1
        k+=1

def mergeSort(custome_list, l, r):
    if l < r:
        m = (l + (r-1))//2
        mergeSort(custome_list, l, m)
        mergeSort(custome_list, m+1, r)
        merge(custome_list, l, m, r)
    return custome_list