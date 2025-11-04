
def find_missing(lst):
    n = len(lst) + 1                # Expected total count of numbers
    total = n * (n + 1) // 2        # Sum of 1..n using the arithmetic series formula
    return total - sum(lst)         # Difference gives the missing number




n = [1, 2, 4, 5]
res = find_missing(n)
print(res)
