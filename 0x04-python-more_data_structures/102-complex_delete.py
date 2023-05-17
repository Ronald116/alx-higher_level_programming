def complex_delete(a_dictionary, value):
    # Create a copy of the original dictionary
    updated_dictionary = a_dictionary.copy[:]

    # Iterate through the items in the dictionary
    for key, val in a_dictionary.items():
        # Check if the value matches the specified value
        if val == value:
            # Delete the key from the copy of the dictionary
            del updated_dictionary[key]

    # Return the updated dictionary
    return updated_dictionary

