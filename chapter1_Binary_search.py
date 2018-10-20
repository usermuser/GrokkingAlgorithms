''' Code from book
def binary_search(list, item):
    low = 0
    high = len(list)-1

    while low <= high :
        mid = (low + high)
        guess = list[mid]
        if guess == item:
            return mid
        if guess > item:
            high = mid - 1
        else:
            low = mid + 1
    return None

my_list = [1, 3, 5, 7, 9]
binary_search(my_list, 3) # => 1
binary_search(my_list, -1) # => None
'''

# My code
def binary_search(list, item):
    low = 0
    high = len(list)

    while low <= high:
        mid = (high + low) // 2
        guess = list[mid]
        if guess == item:
            return mid
        if guess > item:
            high = mid
        else:
            low = mid
    return None


alist = [1,3,5,7,9]

print(binary_search(alist, 1))
print(binary_search(alist, 9))
print(binary_search(alist, 2))





