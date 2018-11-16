from math import floor


class KeyGen:
    """
    KeyGen class to generate new keys upon entry of a new client to the server.
    """
    def __init__(self, large_prime):
        self.p = large_prime

    def generate_keys(self, current_list, list_length, generator):
        if list_length == 1:
            # if 1 client left, send key and p once more then return
            return
        else:
            # Split the list into left and right (left is smaller due to floor).
            left_length = split_length(list_length)
            right_length = list_length - left_length
            left = current_list[:left_length]
            right = current_list[left_length:]
            print(left)
            print(right)

            # for client in left
                # key and p used here

            # for client in right
                # key and p used here

            # generate_keys(left, left_length, right_key)
            # generate_keys(right, right_length, left_keys)


def split_length(list_length):
    return floor(list_length/2)


if __name__ == '__main__':
    """
    For testing purposes
    """
    # Initialize clients to be put into connected list

    connected = [1, 2]
    gen = 3
    k = KeyGen(71)
    k.generate_keys(connected, len(connected), gen)
