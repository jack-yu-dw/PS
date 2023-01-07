# p.197 부품 찾기

def binary_search(array, target, start, end):
    while start <= end:
        mid = (start + end) // 2
        if array[mid] == target:
            return 'yes'
        elif array[mid] > target:
            end = mid - 1
        else:
            start = mid + 1
    return 'no'

n = int(input())
item = list(map(int, input().split()))
item.sort()

m = int(input())
requests  = list(map(int, input().split()))
for request in requests:
    print(binary_search(item, request, 0, n-1), end=' ')
