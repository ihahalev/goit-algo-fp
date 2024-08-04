from LinkedList import LinkedList, Node, llist

def merge_sort(arr: LinkedList, classic=False):
    if arr.length <= 1:
        return arr

    mid = arr.length // 2
    left_half = arr.get_list_till(mid)
    right_half = arr.get_list_from(mid)
    if classic:
        merged = merge_classic(merge_sort(left_half, True), merge_sort(right_half, True))
        arr.head = merged[0]
        for i in range(len(merged)):
            if i+1 == len(merged):
                merged[i].next = None
            else:
                merged[i].next = merged[i+1]
        return arr
    return merge(merge_sort(left_half), merge_sort(right_half))

def merge(left:LinkedList, right:LinkedList):
    merged = LinkedList()
    left_index = 0
    right_index = 0

    # Спочатку об'єднайте менші елементи
    while left_index < left.length and right_index < right.length:
        left_data = left.get_by_index(left_index).data
        right_data = right.get_by_index(right_index).data
        if left_data <= right_data:
            merged.insert_at_end(left_data)
            left_index += 1
        else:
            merged.insert_at_end(right_data)
            right_index += 1

    # Якщо в лівій або правій половині залишилися елементи, 
    # додайте їх до результату
    while left_index < left.length:
        merged.insert_at_end(left.get_by_index(left_index).data)
        left_index += 1

    while right_index < right.length:
        merged.insert_at_end(right.get_by_index(right_index).data)
        right_index += 1

    return merged

def merge_classic(left:LinkedList, right:LinkedList) -> list[Node]:
    merged = []
    left_index = 0
    right_index = 0

    # Спочатку об'єднайте менші елементи
    while left_index < left.length and right_index < right.length:
        left_node = left.get_by_index(left_index)
        right_node = right.get_by_index(right_index)
        if left_node.data <= right_node.data:
            merged.append(left_node)
            left_index += 1
        else:
            merged.append(right_node)
            right_index += 1

    # Якщо в лівій або правій половині залишилися елементи, 
		# додайте їх до результату
    while left_index < left.length:
        merged.append(left.get_by_index(left_index))
        left_index += 1

    while right_index < right.length:
        merged.append(right.get_by_index(right_index))
        right_index += 1

    return merged

if __name__ == "__main__":
    print("Зв'язний список:")
    llist.print_list()
    print("Сортування зв'язного списоку зі створенням нового списку:")
    merge_sort(llist).print_list()
    print("Сортування зв'язного списоку класичним імплементуванням:")
    merge_sort(llist, True).print_list()
    llist.print_list()
