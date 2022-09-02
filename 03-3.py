import sys

input = sys.stdin.readline

n = int(input())
num_list = list(map(int, input().split()))
good_num_count = 0

num_list.sort()

for i in range(n):
    good_num = num_list[i]
    x = 0
    y = n-1
    while i < j:
        if (num_list[x] + num_list[y]) == good_num:
            if x != i and y != i:
                good_num_count += 1
                break
            elif x == i:
                x += 1
            elif y == i:
                y -= 1
        elif num_list[x] + num_list[y] < good_num:
            x += 1
        else:
            y -= 1

print(good_num_count)