def find_sum(array):
    converted_array = []

    for num in array:
        digit_sum = 0
        while num > 0:
            digit = num % 10
            digit_sum += digit
            num //= 10
        
        converted_array.append(digit_sum)

    for i in range(len(converted_array)):
        for j in range(i+1, len(converted_array)):
            if converted_array[i] == converted_array[j]:
                return (i, j)
    
    return (-1, -1)
        

print(find_sum([23, 19, 41, 34, 6, 33]))
print(find_sum([23, 19, 42, 34, 6, 33]))
print(find_sum([43, 19, 41, 35, 6, 3]))