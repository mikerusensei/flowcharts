# Problem 83 - Remove Duplicates from Sorted List

Problem Link -> <https://leetcode.com/problems/remove-duplicates-from-sorted-list/description/>

## Flowchart

Flowchart approach in this problem

```mermaid
    flowchart TD
        start([start])
        head[/head/]
        temp["temp = head"]
        loop{"while temp and temp.next"}
        is_equal{"if temp.val == temp.next.val"}
        re_assign["temp.next = temp.next.next"]
        continue[continue]
        temp_re_assign["temp = temp.next"]
        return[return head]
        terminate([end])

        start --> head
        head --> temp
        temp --> loop
        loop -- True --> is_equal
        is_equal -- True --> re_assign
        re_assign --> continue
        continue --> loop

        is_equal -- False --> temp_re_assign
        temp_re_assign --> loop

        loop -- False --> return --> terminate
```