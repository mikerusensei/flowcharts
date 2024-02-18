def remove_duplicate(head):
    temp = head
    while temp and temp.next:
        if temp.val == temp.next.val:
            temp.next = temp.next.next
            continue
        temp = temp.next
    return head

if __name__ == "__main__":
    given_nums = [1, 1, 2, 3, 4, 3]
    print(remove_duplicate(given_nums))