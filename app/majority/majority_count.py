import sys

'''Given a sequence of elements checks if there is an element which appears more
than half times (n/2), i.e. the majority element. Input a list of sequence of n not
negative integers. Output 1 if the sequence has an element that appears mare then
n/2 times, and 0 otherwise.
>>> get_majority_element([2,3,9,2,2], 0, 4)
1
>>> get_majority_element([1,2,3,4], 0, 3)
0
>>> get_majority_element([1,2,3,1], 0, 3)
0
'''


def get_majority_element(array, l, r):
    if len(array) == 1:
        return array[0]
    votes = sorted_votes(array, l, r)
    half = len(votes) // 2
    count = 1
    for i in range(1, len(votes)):
        if votes[i - 1] == votes[i]:
            count = count + 1
            if count > half:
                return votes[i]
        else:
            if (len(votes) - count) > half:
                return votes[i]
            else:
                return 'One and Product Two '


def sorted_votes(array, l, r):
    if len(array) == 1:
        return array

    if r > l:
        q = (l + r) // 2
        sorted_votes(array, l, q)
        sorted_votes(array, q + 1, r)
        merge(array, l, r, q)
    return array


def merge(array, l, r, q):
    low = []
    high = []

    for x in range(l, q + 1):
        low.append(array[x])
    for x in range(q + 1, r + 1):
        high.append(array[x])
    i = 0
    j = 0
    k = l

    while i < len(low) and j < len(high):
        if low[i] <= high[j]:
            array[k] = low[i]
            i = i + 1
            k = k + 1
        else:
            array[k] = high[j]
            j = j + 1
            k = k + 1
    if i < len(low):
        for x in range(i, len(low)):
            array[k] = low[x]
            k = k + 1
    else:
        for x in range(j, len(high)):
            array[k] = high[x]
            k = k + 1


if __name__ == '__main__':
    input = sys.stdin.read()
    n, *a = list(map(int, input.split()))
    if get_majority_element(a, 0, n) != -1:
        print(1)
    else:
        print(0)
