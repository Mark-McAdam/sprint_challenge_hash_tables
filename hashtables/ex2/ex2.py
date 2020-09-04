#  Hint:  You may not need all of these.  Remove the unused functions.
class Ticket:
    def __init__(self, source, destination):
        self.source = source
        self.destination = destination


def reconstruct_trip(tickets, length):
    """
    YOUR CODE HERE
    """
    # Your code here
    # First flight has destination with source: None

    # Final flight has source with destination: None

    # hash table to store the route.
    hash_table = {}

    for ticket in tickets:
        hash_table[ticket.source] = ticket.destination
        # print(hash_table)

    # Return the reconstructed route
    # in the form of a list of strings with
    # the entire route in correct order

    # print(hash_table)

    # make a list to hold the route

    route = [hash_table["NONE"]]

    # print(route[-1])
    while route[-1] != "NONE":
        route.append(hash_table[route[-1]])

    # TODO uncomment when its working
    return route
    # print(route)


if __name__ == "__main__":
    ticket_1 = Ticket("NONE", "PDX")
    ticket_2 = Ticket("PDX", "DCA")
    ticket_3 = Ticket("DCA", "NONE")

    tickets = [ticket_1, ticket_2, ticket_3]

    # expected = ["PDX", "DCA", "NONE"]
    result = reconstruct_trip(tickets, 3)

    # its returning
    # {'NONE': 'PDX', 'PDX': 'DCA', 'DCA': 'NONE'}
    # need to trim off the rest

    # route with key of none gives us pdx in the list
    # go backwards through list while

