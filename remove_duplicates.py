numbers: list[int] = [1, 1, 2]


def remove_duplicates(nums: list[int]) -> int:
    assert len(nums) > 0

    for num in nums:
        if num == nums[len(nums) - 1]:
            print(nums[0])

    # return number of unique elements
    return len(nums)


if __name__ == '__main__':
    remove_duplicates(nums=numbers)
