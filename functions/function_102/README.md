# Function 102 [Equal Sum]
Create a `flowchart` for a function that would identify the `indexes` of the `first pair` of the numbers in an array having an equal sum. 
The program must treat the `numbers` `as numbers` `not as string.`

### Example:
* Given an array of [23, 19, 41, 34, 6, 33]
    * the function should return `(0, 2)`.
* Given an array of [23, 19, 42, 34, 6, 33]
    * the function should return `(2, 4)`.
* Given an array of [43, 19, 41, 35, 6, 3]
    * the function should return `(-1, -1)`.

## Flowchart for this function
```mermaid
    flowchart TD
        start([start])
        array[/array/]
        added_array["added_array = []"]
        for_num{"for num in array:"}
        digit_sum["digit_sum = 0"]
        while_num{"while num > 0:"}
        digit["digit = num % 10"]
        add_digit_sum["digit_sum += digit"]
        div_num["num //= 10"]
        append["added_array.append(digit_sum)"]
        for_i{"for i in range(len(added_array)):"}
        for_j{"for j in range(i + 1, len(added_array)):"}
        if{"if added_array[i] == added_array[j]:"}
        return["return (i, j)"]
        negative["return (-1, -1)"]
        terminate([end])

        start --> array
        array --> added_array
        added_array --> for_num
        for_num -- True --> digit_sum
        digit_sum --> while_num
        while_num -- True --> digit
        digit --> add_digit_sum
        add_digit_sum --> div_num
        div_num --> while_num
        append --> for_num
        while_num -- False --> append
        for_num -- False --> for_i
        for_i --> True --> for_j
        for_j -- True --> if
        if -- True --> return
        return --> terminate
        if -- False --> for_J
        for_j -- False --> for_i
        for_i -- False --> negative
        negative --> terminate
```
