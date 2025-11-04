
# def printList(n):
#     for i in range(len(n)):
#         print(n[i])

#     return 1



# n = [2, 5, 23, 5,5, 2,1]

# res = printList(n)
# # res = 1

# print(res)



# def addSum(a, b):
#     sum = a + b
#     return sum


# print(addSum(8, 10))
# print(addSum(2, 0))
# print(addSum(2, 3))
# print(addSum(6, 0))
# print(addSum(2, 13))


# def missingNumber(n, arr):

#     total = n *  (n + 1) // 2
#     missing_num = total - sum(arr)

#     return missing_num

# n = 10
# arr = [1, 2, 4, 3, 5, 6, 7, 10, 8]

# print(missingNumber(n, arr))


# def sumOfDigits(n):

#     sum = 0
#     while(n != 0):
#         remainder = n % 10
#         sum += remainder
#         n //= 10

#     return sum

# n = 999
# print(sumOfDigits(n))



# def factorial(n):

#     fact = 1

#     for i in range(1, n+1):
#         fact *= i

#     return fact

# n = 3
# print(factorial(n))


# Permutation....



# def factorial(n):

#     fact = 1

#     for i in range(1, n+1):
#         fact *= i

#     return fact

# n = 5
# r = 2
# num = factorial(n)
# denom = factorial(n - r)
# prem = num // denom

# print(prem)



# Combination...

# def factorial(n):

#     fact = 1

#     for i in range(1, n+1):
#         fact *= i

#     return fact

# n = 5
# r = 2
# num = factorial(n)
# denom = factorial(n - r) * factorial(r)
# combination = num // denom

# print(combination)



# # # printinh numbers from 1 to N

# def printNum(n):

#     if(n == 0):
#         return 1

#     printNum(n - 1)
#     print(n)

# n = 5
# printNum(n)


# # Sum of n natural numbers.

# def addSum(n):

#     if(n == 0):
#         return 0
#     return n + addSum(n - 1)


# n = 5
# res = addSum(n)
# print(res)



# Recursive Function to reverse a String

# def revStr(s):

#     if(len(s) == 0):
#         return s
    
#     print(f"Inside the fn {s}")

#     return s[-1] + revStr(s[:-1])

# s = 'Shivam'
# n = 6

# print(f"Outside the fn {revStr(s)}")

# arr = [3,24, 5, 64, 775, 4]

# print(max(arr))


# def maxNum(nums):

#     if(len(nums) == 1):
#         return nums[0]

#     maxValue = maxNum(nums[1:])

#     if(nums[0] > maxValue):
#         return nums[0]
#     else:
#         return maxValue


# nums = [4 , 32, 1, 45, 44, 1111, 9099]
# print(maxNum(nums))



def f(x):
    if(x == 2):
        return 1
    
    else:
        print("+")
        f(x - 1)

x = 6
print(f(x))

