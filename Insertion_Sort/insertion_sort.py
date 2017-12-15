def insertionSort(A):
   for index in range(1,len(A)):

     key = A[index]
     position = index

     while position>0 and A[position-1]>key:
         A[position]=A[position-1]
         position = position-1

     A[position]=key

A = [3, 6, 2, 8, 5, 7, 11, 9, 0]
insertionSort(A)
print(A)
