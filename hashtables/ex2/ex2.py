#  Hint:  You may not need all of these.  Remove the unused functions.
from hashtables import (HashTable,
                        hash_table_insert,
                        hash_table_remove,
                        hash_table_retrieve,
                        hash_table_resize)


class Ticket:
    def __init__(self, source, destination):
        self.source = source
        self.destination = destination


def reconstruct_trip(tickets, length):
    hashtable = HashTable(length)
    route = []

    """
    YOUR CODE HERE
    """
    for ticket in tickets:
        key = ticket.source
        value = ticket.destination
        hash_table_insert(hashtable, key, value)
    
    travel_destination = hash_table_retrieve(hashtable, "NONE")
    
    while travel_destination  is not 'NONE':
        route.append(travel_destination)
        travel_destination = hash_table_retrieve(hashtable, travel_destination)
    
    return route