def has_negatives(a):
    """
    For an input list of integers, we wish to know which positive numbers 
    have corresponding negative numbers in the list.    """
    # Your code here

    # Hash table to hold value
    hash_table = {}

    # we receive a list of values from the test case

    # iterate through the list a
    for i in a:

        # put the list into our hash table
        # set key to non zero non negative number,
        # set value to same for fast lookup later
        hash_table[i] = i

    # case 1 - if item is 0 ignore it
    for i in a:
        if i == 0:
            return None

    # case 2 - if the item is negative ignore it

    # elif i == negative ?
    # ignore

    # case 3 - if item is greater than 0 and not negative -
    # redundant greater than 0 is not negative
    # but is has a key in dictionary that
    # matches negative equivalent the number
    # append that number to the result

    # result is a list of values with corresponding
    # negative valueto pass the test
    result = []

    return result


if __name__ == "__main__":
    # For this test we are expecting -4 to be returned
    print(has_negatives([-1, -2, 1, 2, 3, 4, -4]))
