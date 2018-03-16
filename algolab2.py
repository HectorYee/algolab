arr = [2,3,5,1,4,7,9]
arr1 = [.3,.4,.1,.2,.6,.7,.9,.8,.7,.8]

arrB = []
for i in range(0, len(arr)):
    arrB.append(0)
print (arrB)

print (arr)

def bubble_sort(arr):
    for i in range(0, len(arr)-2):
        for j in range(len(arr)-1, i, -1):
            if arr[j] < arr[j-1]:
                temp = arr[j]
                arr[j] = arr[j-1]
                arr[j-1] = temp
    print (arr)

def counting_sort(arr, arrB, k):
    c =[]
    for i in range(0, k + 1):
        c.append(0)
    for j in range(0, len(arr)):
        c[arr[j]] += 1
    print (c)

    for i in range(1, k+1):
        c[i] = c[i] + c[i-1]
    print (c)

    print("B starts here")
    for j in range(len(arr)-1, -1, -1):
        arrB[c[arr[j]]-1] = arr[j]
        print(arrB)
        c[arr[j]] -= 1

    print (arrB)

def bucket_sort(arr):

    n = len(arr)
    bucket = [[]]*n
    print(bucket)
    for i in range(0, n):
        bucket[i] = []
    for i in range(0, n):
        temp = int(n * arr[i])
        bucket[temp].append(arr[i])
    for i in range(0, n):
        insertion_sort(bucket[i])

    index = 0
    for i in range(0, n):
        for j in bucket[i]:
            bucket[index] = j
            index += 1
    print (bucket)



def insertion_sort(arr):
    for i in range(1, len(arr)):
        key = arr[i]
        j = i-1
        while j >= 0 and arr[j] > key:
            arr[j+1] = arr[i]
            j = j - 1
        arr[j + 1] = key
    return arr





def shell_sort(arr):
    n = len(arr)
    sublistcount = n/2
    for gap in range(sublistcount):
        for








# bubble_sort(arr)
# counting_sort(arr,arrB,9)
# bucket_sort(arr1)
