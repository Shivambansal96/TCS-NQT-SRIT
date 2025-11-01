# # # 1) Difference between sum of odd and even elements.
# # num = input()

# # evenSum = 0   # 18
# # oddSum = 0    # 21

# # for i in range(len(num)):

# #     if(i % 2 == 0):
# #         evenSum += int(num[i])

# #     else:
# #         oddSum += int(num[i])

# # diff = abs(evenSum - oddSum)
# # print(diff)
# # print(type(diff))




# # # # freq Count
# # # METHOD 1

# # name = 'aabbcdde'

# # for i in range(len(name)):
# #     count = name.count(name[i])

# #     if(count == 1):
# #         print(name[i])
# #         break



# # # # METHOD 1

# # name = 'aabbcdde'
# # # myDict = {}
# # # myDict['name'] = "Shivam"
# # # print(myDict)

# # freq = {}

# # for i in name:
# #     if i not in freq:
# #         freq[i] = 1
    
# #     else:
# #         freq[i] += 1

# # for i, j in freq.items():

# #     if(j == 1):
# #         print(i)
# #         break

# # # # #METHOD 3
# # from collections import Counter

# # name = 'aabbcdde'

# # frq = dict(Counter(name).items())

# # # print(frq)

# # for i, j in frq.items():
# #     if(j == 1):
# #         print(i)
# #         break

# # # # #3) Array Rearrangement

# # arr = [1, 8, 5, 9, 2]
# # # arr = [1, 2, 5, 8, 9]
# # # firstPart = [1, 2, 5]
# # # secondPart = [8, 9]

# # arr.sort()

# # mid = len(arr)//2

# # result = arr[:mid + 1] + arr[:mid:-1]

# # print(result)

# # if(i == '(' or i == "{" or i == "[")
# # name = '((((((((()(((()))))))))))))'
# name = '(()))'
# count = 0
# for i in name:
#     if(i == "("):
#         count += 1
#     elif(i == ")"):
#         count -= 1

# print(abs(count))


# ## 6) Capitalize 
# # Method 1


# name = 'my name is shivam'

# arr = name.split()

# new = []

# for i in arr:
#     new.append(i.capitalize())

# result = " ".join(new)
# print(result)


# # Method 2


name = 'my name is shivam'

result = ""

for i in range(len(name)):

    if(i == 0 or name[i-1] == " "):
        result += name[i].upper()

    else:
        result += name[i]


print(result)