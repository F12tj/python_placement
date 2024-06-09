def get_list_input(list_num):
    # Get input for the specified list number
    input_str = input(f"Enter the values for list {list_num}, separated by spaces: ")
    return input_str.split()

def swap_lists(list1, list2):
    # Swap the contents of list1 and list2
    return list2, list1

def main():
    num_of_lists = int(input("Enter the number of lists: "))
    lists = []

    # Collect the values for each list
    for i in range(num_of_lists):
        lists.append(get_list_input(i + 1))

    # Swap the lists pairwise
    for i in range(0, len(lists) - 1, 2):
        lists[i], lists[i + 1] = swap_lists(lists[i], lists[i + 1])

    # Print the swapped lists
    for i, lst in enumerate(lists):
        print(f"List {i + 1} after swapping: {' '.join(lst)}")

if __name__ == "__main__":
    main()
