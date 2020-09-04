def intersection(arrays):
    """
    YOUR CODE HERE
    """
    # Your code here
    # Find the intersection between multiple lists of integers.

    # Hash Table to store the integers
    integer_hash = {}

    # for the list of integers in the arrays

    # changed to array in arrays to avoid casting as a list
    # I had for list in arrays
    for array in arrays:

        # for the integer in the array - changed from list to work
        for integer in array:

            # if the integer is not already in our hash table
            if integer not in integer_hash:
                integer_hash[integer] = 1

                # print(integer_hash[integer])
            # if integer is in the hash table
            # increment
            else:
                integer_hash[integer] += 1

    length = len(arrays)
    print(f"Length {length}")

    # list to hold the intersection
    # renamed to overlap to avoid name collision
    overlap = []

    for item in list(integer_hash.items()):
        if item[1] == length:
            print(f"Item to append {item[0]}")
            overlap.append(item[0])

    return overlap


# this was such a silly oversight.
# I had tried naming a variable.

if __name__ == "__main__":
    arrays = []

    arrays.append(list(range(1000000, 2000000)) + [1, 2, 3])
    arrays.append(list(range(2000000, 3000000)) + [1, 2, 3])
    arrays.append(list(range(3000000, 4000000)) + [1, 2, 3])

    print(intersection(arrays))
