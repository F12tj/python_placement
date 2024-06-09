def get_list_input(list_num):
    input_str = input(f"Enter the values for list {list_num}, separated by spaces: ")
    return input_str.split()

def swap_lists(list1, list2):
    return list2, list1

def main():
    num_of_lists = int(input("Enter the number of lists: "))
    lists = []

    for i in range(num_of_lists):
        lists.append(get_list_input(i + 1))

    for i in range(0, len(lists) - 1, 2):
        lists[i], lists[i + 1] = swap_lists(lists[i], lists[i + 1])

    if num_of_lists % 2 != 0:
        print(f"List {num_of_lists} cannot be swapped because there is no list to swap with.")
 
    for i, lst in enumerate(lists):
        print(f"List {i + 1} after swapping: {' '.join(lst)}")

if __name__ == "__main__":
    main()
