from typing import List, Tuple


def find_two_sum(numbers: List[int], target_sum: int) -> Tuple[int, int]:
    """
    :param numbers: (list of ints) The list of numbers.
    :param target_sum: (int) The required target sum.
    :returns: (a tuple of 2 ints) The indices of the two elements whose sum is equal to target_sum
    """
    seen = {}
    idx = 0
    for num in numbers:
        req_num = target_sum - num
        if req_num in seen:
            return seen[req_num], idx
        seen[num] = idx # num will be req_num in the future
        idx += 1
    return None


if __name__ == "__main__":
    print(find_two_sum([3, 1, 5, 7, 5, 9], 10))
