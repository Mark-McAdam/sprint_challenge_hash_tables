def get_indices_of_item_weights(weights, length, limit):
    """ 
    * A brute-force solution would involve two nested loops, yielding a
    quadratic-runtime solution. How can we use a hash table in order to
    implement a solution with a better runtime?

    * Think about what we can store in the hash table in order to help us to
    solve this problem more efficiently. 

    * What if we store each weight in the input list as keys? What would be
    a useful thing to store as the value for each key? 

    * If we store each weight's list index as its value, we can then check
    to see if the hash table contains an entry for `limit - weight`. If it
    does, then we've found the two items whose weights sum up to the
    `limit`!    

    This reminds me of the problem called Two Sum which is the first problem on Leetcode
    """
    # Your code here

    # hash table to cache weights with indices
    hash_table = {}

    # indicies list
    ind_list = []

    # case 1 - not two values to add list of 1 number
    if len(weights) == 1:
        # return None no match
        return None

    # case 2 - only two values to add together
    elif len(weights) == 2:
        # return index list
        return (1, 0)
    # case 3 - more than two values to add
    # this is what the problem is about
    else:
        for i, j in enumerate(weights):

            # set key to weight, value to index
            hash_table[j] = i

        # iterate through the weights
        for i in weights:
            # if limit -i is in hash_table
            if limit - i in hash_table:

                # append to indicies list
                ind_list.append(hash_table[i])

        if ind_list[1] > ind_list[0]:
            # fancy swap them
            ind_list[0], ind_list[1] = ind_list[1], ind_list[0]

        # put answer into the expected format to pass test
        answer = tuple(ind_list)

        # return the answer
        return answer

    # not a match case
    return None


if __name__ == "__main__":

    weights_3 = [4, 6, 10, 15, 16]
    answer_3 = get_indices_of_item_weights(weights_3, 5, 21)

    print(answer_3)
    # self.assertTrue(answer_3[0] == 3)
    # self.assertTrue(answer_3[1] == 1)

    weights_4 = [12, 6, 7, 14, 19, 3, 0, 25, 40]
    answer_4 = get_indices_of_item_weights(weights_4, 9, 7)

    print(answer_4)
    # self.assertTrue(answer_4[0] == 6)
    # self.assertTrue(answer_4[1] == 2)
