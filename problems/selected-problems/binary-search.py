from typing import List


def count_numbers(sorted_li: List[int], less_than: int) -> int:
    n = len(sorted_li)
    if not sorted_li:
        return 0
    if n == 1:
        return 1 if sorted_li[0] < less_than else 0
    if sorted_li[0] >= less_than:
        return 0
    if sorted_li[n - 1] < less_than:
        return n
    l = 0
    r = n - 1
    while l < r - 1:
        mid = (l + r) // 2
        if sorted_li[mid] < less_than:
            l = mid
        else:
            r = mid
    return l + 1


if __name__ == "__main__":
    sorted_list = [1, 3, 5, 7]
    print(count_numbers(sorted_list, 4))  # should print 2
