#!/usr/bin/python3

def search_replace(my_list, search, replace):

    # Create a new list to store the replaced elements
    result = []

    # Iterate through the elements of the input list
    for element in my_list:
        # Check if the current element matches the search element
        if element == search:
            # Replace the element with the new element
            result.append(replace)
        else:
            # Keep the original element
            result.append(element)

    return result
