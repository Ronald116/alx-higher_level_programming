#!/usr/bin/python3

if __name__ == "__main__":
    """A Program that prints the addition of all arguments."""
  
    import sys

    len_av = 0
    for i in range(len(sys.argv) - 1):
        len_av += int(sys.argv[i + 1])
    print("{}".format(len_av))
