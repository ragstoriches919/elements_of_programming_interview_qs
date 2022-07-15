# They made a new variable every time in the while loop

def remove_duplicates(L):
    it = L

    while it:
        next_distinct = it.next
        while it.data == next_distinct.data and next_distinct:
            next_distinct = next_distinct.next
        it.next = next_distinct
        it = next_distinct

    return L

