

class KeyGen:
    """
    KeyGen class to generate new keys upon entry of a new client to the server.
    """
    def __init__(self, large_prime, generator):
        self.p = large_prime
        self.g = generator

    def generate_keys(self, current_list, list_length):
        if list_length == 1:
            # Exit condition
            return 1
        else:
            # Split the list into left and right (left is smaller due to floor).
            left = current_list[:list_length // 2]
            right = current_list[list_length // 2:]
            print(left)
            print(right)


if __name__ == '__main__':
    """
    For testing purposes
    """
    # Start with 1 client
    k = KeyGen(71, 3)
    clients = [1, 2]
    k.generate_keys(clients, len(clients))
