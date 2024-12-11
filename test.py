#9. Write a Python program to remove duplicate elements from a list.

def remove_duplicates(input_list):
    return list(set(input_list))

input_list = [1, 2, 2, 3, 4, 4, 5, 6, 6]
print("Original List: ", input_list)
print("List without duplicates: ", remove_duplicates(input_list))
