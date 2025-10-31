# # Remove vowels from the String

# name = input()  # Shivam

# for i in name:

#     if(i != 'a' and i != 'e' and i != "o" and i != 'u' and i != 'i'):
#         print(i, end="")

# # # Remove duplicates after merging 2 arrays.

# arr1 = [1, 2, 3, 4, 5]
# arr2 = [2, 6, 8, 10]

# arr3 = arr1 + arr2
# # print(arr3)
# l = []

# for i in arr3:
#     if arr3.count(i)==1:
#         l.append(i)

# print(f'Elements = {l}')
# print(f'Total = {len(l)}')


# # # Print name in reverse using loops.

# name = "Shivam"

# for i in range(5, -1, -1):
#     print(name[i], end="")


# # # Reverse a number

# n = int(input("Enter a number = "))
# reversedNum = 0
# while(n != 0):
#     lastDigit = n % 10               # 3
#     reversedNum = reversedNum * 10 + lastDigit      # 123
#     n//=10                                        # 3


# print(reversedNum)


# # Sort the alternate elements in the array

# arr = [5, 1, 4, 7, 9]
# arr1 = []
# for i in range(len(arr)):

#     if(i % 2 == 0):
#         arr1.append(arr[i])

# arr1.sort()
# print(arr1)



# # # Print non-common elements in both the arrays.

# arr1 = [1, 2, 3, 4]
# arr2 = [4, 5, 6, 7]
# arr3 = arr1 + arr2

# setA = set(arr1)
# setB = set(arr2)

# setC = setA.union(setB)
# interSection = setA.intersection(setB)
# print(setC.difference(interSection))
# print(setC.symmetric_difference(interSection))


# # #  Sort the elements in an array and then print the B-alternate numbers

# arr = [5, 1, 3, 2, 7]

# arr.sort()                 # 1 2 3 5 7

# for i in range(len(arr)):

#     if(i % 2 == 0):
#         print(arr[i], end=" ")
