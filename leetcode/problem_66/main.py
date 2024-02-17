# Problem 66 Plus One Leetcode
# by: mikerusensei
# 02/17/2024

def plus_one(array):
    result = []
    converted_array = ""

    while len(array):
        num = array.pop(0)
        converted_array += str(num)
    
    converted_int = int(converted_array) + 1

    while converted_int > 0:
        digit = converted_int % 10
        result.insert(0, digit)
        converted_int //= 10

    return result

if __name__ == "__main__":
    digits = [1, 2, 3]
    digits_1 = [1, 9, 9, 9]

    print(plus_one(digits))
    print(plus_one(digits_1))