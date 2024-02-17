# Create a function that wound return the index of consecutive 
# characters in a string. Use Queue Data Structures
# by: mikerusensei
# 02/17/2024

def count_consecutive(string:str):
    result = []
    consecutive_count = 0
    queue = list(string)

    previous = queue.pop(0)
    i = 0

    while len(queue):
        next = queue.pop(0)

        if previous == next:
            consecutive_count += 1
        else:
            if consecutive_count > 0:
                result.append([i - consecutive_count, i])
            
            consecutive_count = 0

        previous = next
        i += 1

    if consecutive_count > 0:
        result.append([i - consecutive_count, i])

    return result

if __name__ == "__main__":
    given_string = "111abccc2deff33g"
    print(count_consecutive(given_string))