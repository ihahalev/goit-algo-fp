from LinkedList import LinkedList
from sort import merge, merge_sort

def extend(list1:LinkedList, list2:LinkedList, check_sorted = False) -> LinkedList:
    sorted1 = list1
    sorted2 = list2
    if check_sorted:
        isSorted = False
        for i in range(1,list1.length):
            isSorted = list1.get_by_index(i-1).data < list1.get_by_index(i).data
            if not isSorted:
                print("First linked list is not sorted, sorting")
                sorted1 = merge_sort(list1)
                break
        isSorted = False
        for i in range(1,list2.length):
            isSorted = list2.get_by_index(i-1).data < list2.get_by_index(i).data
            if not isSorted:
                print("Second linked list is not sorted, sorting")
                sorted2 = merge_sort(list2)
                break
    return merge(sorted1, sorted2)

if __name__ == "__main__":
    list1 = LinkedList()
    # Вставляємо вузли в початок
    list1.insert_at_beginning(55)
    list1.insert_at_beginning(20)
    list1.insert_at_beginning(15)

    list2 = LinkedList()
    # Вставляємо вузли в початок
    list2.insert_at_beginning(45)
    list2.insert_at_beginning(25)
    list2.insert_at_beginning(10)
    print("\nЗв'язний список 1:")
    list1.print_list()
    print("\nЗв'язний список 2:")
    list2.print_list()
    print("\nОб'єднання двох відсортованих зв'язних списків в один відсортований список:")
    extend(list1, list2).print_list()

    list1.insert_at_end(35)
    list2.insert_at_end(5)
    print("\nНевідсортований Зв'язний список 1:")
    list1.print_list()
    print("\nnНевідсортований Зв'язний список 2:")
    list2.print_list()
    print("\nОб'єднання двох невідсортованих зв'язних списків в один список:")
    extend(list1, list2).print_list()
    print("\nОб'єднання двох невідсортованих зв'язних списків в один відсортований список з перевіркою на відсортованість:")
    extend(list1, list2, True).print_list()