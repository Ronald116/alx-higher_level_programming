#!/usr/bin/python3

if __name__ == "__main__":
    """Print all names defined by compiled module hidden_4 module."""
    import hidden_4

    name_list = dir(hidden_4)
    for name in name_list:
        if name_list[:2] != "__":
            print(name_list)
