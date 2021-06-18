import random
import time

def naive_search(l, target):
    for i in range(len(l)):
        if l[i] == target:
            return i
    return -1

def binary_search(l, target, low=None, high=None):
    if low is None:
        low = 0
    if high is None:
        high = len(l) - 1
    if high < low:
        return -1
    midpoint = (low + high) // 2
    if l[midpoint] == target:
        return midpoint
    elif l[midpoint] > target:
        return binary_search(l, target, low, midpoint - 1)
    else:
        return binary_search(l, target, midpoint + 1, high)

def binary_search2(l, target):
    low = 0
    high = len(l) -1
    while low <= high:
        mid = (low + high) // 2
        if l[mid] == target:
            return mid
        elif l[mid] > target:
            high = mid - 1
        else:
            low = mid + 1
    return -1


if __name__ == '__main__':
    l = [1, 3, 4, 6, 7, 8, 10, 13, 15, 18, 19]
    target = 15
    print(naive_search(l, target))
    print(binary_search(l, target))
    print(binary_search2(l, target))
    
    print("\n\n\n")

    length = 10000
    sorted_list = set()
    while len(sorted_list) < length:
        sorted_list.add(random.randint(-3 * length, 3 * length))
    sorted_list = sorted(list(sorted_list))

    target = random.randint(-3 * length, 3 * length)

    start = time.time()
    for target in sorted_list:
        naive_search(sorted_list, target)
    end = time.time()
    print("Naive search time: ", (end - start), "seconds")

    start = time.time()
    for target in sorted_list:
        binary_search(sorted_list, target)
    end = time.time()
    print("Binary (recursive) search time: ", (end - start), "seconds")

    start = time.time()
    for target in sorted_list:
        binary_search2(sorted_list, target)
    end = time.time()
    print("Binary (while loop) search time: ", (end - start), "seconds")
