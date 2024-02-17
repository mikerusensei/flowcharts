# Function 101 __[Consecutive Characters]__

Create a function that wound return the index of consecutive characters in a string.
Use `Queue Data Structures` 

### Example
* Given a string "111abccc2deff33g"
    * It should return __[[0, 2], [5, 7], [11, 12], [13, 14]]__
* Given a string "abcdef"
    * It should return __[]__

## Flowchart for this Function
```mermaid
    flowchart TD
       start([Start])
       string[/string/]
       result["result = []"]
       con_count["consecutive_count = 0"]
       list_str["queue = List(string)"]
       previous["previous = queue.pop(0)"]
       iterator["i = 0"]
       loop{"while len(queue)"}
       next["next = queue.pop(0)"]
       is_equal{"if previous == next"}
       add_con_count["consecutive_count += 1"]
       re_assign["previous = next"]
       add_i["i += 1"]
       check_inside{"if consecutive_count > 0"}
       append_inside["result.append([i - consecutive_count, i])"]
       reset_con_count["consecutive_count = 0"]
       check_outside{"if consecutive_count > 0"}
       append_outside["result.append([i - consecutive_count, i])"]
       return_result["return result"]
       terminate([End])
   
   
       start --> string
       string --> result
       result --> con_count
       con_count --> list_str
       list_str --> previous
       previous --> iterator
       iterator --> loop
       loop -- True --> next
       next --> is_equal
       is_equal -- True --> add_con_count
       add_con_count --> re_assign
       is_equal -- False --> check_inside
       check_inside -- True --> append_inside
       check_inside -- False --> reset_con_count
       append_inside --> reset_con_count
       reset_con_count --> re_assign
       re_assign --> add_i
       add_i --> loop
       loop -- False --> check_outside
       check_outside -- True --> append_outside
       check_outside -- False --> return_result
       append_outside --> return_result
       return_result --> terminate
```
