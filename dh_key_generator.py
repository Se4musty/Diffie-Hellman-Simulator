from math import floor
from temporary_client import Client


def split_length(list_length):
    return floor(list_length/2)


def secret_comparison(clients):
    prev = clients[0]
    for client in clients:
        if client.shared_secret != prev.shared_secret:
            return False
        prev = client
    return True


class KeyGen:
    """
    KeyGen class to generate new keys upon entry of a new client to the server.
    """
    def __init__(self, large_prime):
        self.p = large_prime

    def generate_keys(self, current_list, list_length, generator):
        if list_length == 1:
            # if 1 client left, send key and p once more then return
            current_list[0].calculate_key(generator, self.p)
            return
        else:
            # Split the list into left and right (left is smaller due to floor).
            left_length = split_length(list_length)
            right_length = list_length - left_length

            left = current_list[:left_length]
            right = current_list[left_length:]

            # set resultant keys to begin as the generator.
            left_key = generator
            right_key = generator

            # Loop through both halves of the current list to create a shared key on each half.
            for client in left:
                # send key and p to client, and receive their calculated key.
                left_key = client.calculate_key(left_key, self.p)

            for client in right:
                # send key and p to client, and receive their calculated key.
                right_key = client.calculate_key(right_key, self.p)

            # Recurse through left and right halves until secret_key has been created.
            self.generate_keys(left, left_length, right_key)
            self.generate_keys(right, right_length, left_key)


if __name__ == '__main__':
    """
    For testing purposes
    """
    # Initialize clients to be put into connected list
    connected = []
    for i in range(2):
        connected.append(Client())
    print(connected[0].private_key)
    # connected = [1, 2]
    k = KeyGen(71)
    k.generate_keys(connected, len(connected), 3)

    # Once secret keys are calculated, check if they are the same
    if secret_comparison(connected):
        print("Secret key {}, was correctly calculated for all clients!".format(connected[0].shared_secret))
    else:
        print("Secret key wasn't correctly calculated")
