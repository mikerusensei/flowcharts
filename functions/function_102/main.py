def find_sum(array):
    added_array = []

    for num in array:
        digit_sum = 0
        while num > 0:
            digit = num % 10
            digit_sum += digit
            num //= 10
        
        added_array.append(digit_sum)

    for i in range(len(added_array)):
        for j in range(i+1, len(added_array)):
            if added_array[i] == added_array[j]:
                return (i, j)
    
    return (-1, -1)
        

print(find_sum([23, 19, 41, 34, 6, 33]))
print(find_sum([23, 19, 42, 34, 6, 33]))
print(find_sum([43, 19, 41, 35, 6, 3]))