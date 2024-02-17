def contains_duplicate(array: list):
    seen = set()
    for num in nums:
        if num in seen:
            return True
        seen.add(num)
    return False

if __name__ == "__main__":
    nums = [1, 2, 3, 1]
    print(contains_duplicate(nums))